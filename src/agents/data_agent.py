import pandas as pd

def data_agent_load_and_summarize(csv_path):
    """
    Data Agent:
    Loads the dataset, validates required columns, and produces summaries.
    Returns a dict with status, validation_report, and summary tables (as lists of records).
    """

    try:
        df = pd.read_csv(csv_path, parse_dates=['date'])
    except Exception as e:
        return {"status": "error", "message": f"Failed to load CSV: {str(e)}"}

    required_cols = [
        "campaign_name", "adset_name", "date", "spend", "impressions", "clicks", "ctr",
        "purchases", "revenue", "roas", "creative_type", "creative_message",
        "audience_type", "platform", "country"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        return {"status": "error", "message": f"Missing columns: {missing}"}

    validation = {
        "rows": int(len(df)),
        "missing_values": {k: int(v) for k, v in df.isna().sum().to_dict().items()},
        "duplicates": int(df.duplicated().sum()),
        "dtypes": {k: str(v) for k, v in df.dtypes.astype(str).to_dict().items()},
    }

    # Campaign-level aggregation
    campaign_summary = df.groupby("campaign_name").agg(
        spend=("spend", "sum"),
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        ctr=("ctr", "mean"),
        purchases=("purchases", "sum"),
        revenue=("revenue", "sum"),
        roas=("roas", "mean")
    ).reset_index()

    # Daily aggregation
    daily_summary = df.groupby("date").agg(
        spend=("spend", "sum"),
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        ctr=("ctr", "mean"),
        purchases=("purchases", "sum"),
        revenue=("revenue", "sum"),
        roas=("roas", "mean")
    ).reset_index()

    creative_summary = df.groupby("creative_type").agg(
        ctr=("ctr", "mean"),
        roas=("roas", "mean"),
        clicks=("clicks", "sum")
    ).reset_index()

    audience_summary = df.groupby("audience_type").agg(
        ctr=("ctr", "mean"),
        roas=("roas", "mean"),
        impressions=("impressions", "sum")
    ).reset_index()

    low_ctr = campaign_summary.sort_values("ctr").head(10)
    low_roas = campaign_summary.sort_values("roas").head(10)

    return {
        "status": "success",
        "validation_report": validation,
        "summary": {
            "campaign_summary": campaign_summary.to_dict(orient="records"),
            "daily_summary": daily_summary.to_dict(orient="records"),
            "creative_summary": creative_summary.to_dict(orient="records"),
            "audience_summary": audience_summary.to_dict(orient="records"),
            "low_ctr_campaigns": low_ctr.to_dict(orient="records"),
            "low_roas_segments": low_roas.to_dict(orient="records"),
        }
    }
