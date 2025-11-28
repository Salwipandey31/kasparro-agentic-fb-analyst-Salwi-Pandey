import pandas as pd
import numpy as np

def insight_agent_generate_insights(data_summary):
    """
    Insight Agent:
    Reads summaries from the Data Agent and produces data-driven hypotheses.
    """

    # Convert summary lists back to DataFrames
    daily = pd.DataFrame(data_summary["daily_summary"])
    campaign = pd.DataFrame(data_summary["campaign_summary"])
    creative = pd.DataFrame(data_summary["creative_summary"])
    audience = pd.DataFrame(data_summary["audience_summary"])

    hypotheses = []

    # --- Hypothesis 1: ROAS drop ---
    if len(daily) > 8:
        daily_sorted = daily.sort_values("date")
        roas_before = daily_sorted["roas"].iloc[-8:-4].mean()
        roas_after = daily_sorted["roas"].iloc[-4:].mean()
        delta = float(roas_after - roas_before)

        if delta < 0:
            hypotheses.append({
                "id": "H1",
                "reason": "Recent ROAS decline detected.",
                "evidence": {
                    "roas_before": float(roas_before),
                    "roas_after": float(roas_after),
                    "delta": delta
                },
                "confidence": 0.85
            })

    # --- Hypothesis 2: CTR drop → creative fatigue ---
    if len(daily) > 8:
        ctr_before = daily["ctr"].iloc[-8:-4].mean()
        ctr_after = daily["ctr"].iloc[-4:].mean()
        delta_ctr = float(ctr_after - ctr_before)

        if delta_ctr < 0:
            hypotheses.append({
                "id": "H2",
                "reason": "CTR decline suggests possible creative fatigue.",
                "evidence": {
                    "ctr_before": float(ctr_before),
                    "ctr_after": float(ctr_after),
                    "delta": delta_ctr
                },
                "confidence": 0.82
            })

    # --- Hypothesis 3: Creative type underperformance ---
    worst_creatives = creative.sort_values("roas").head(3)
    for _, row in worst_creatives.iterrows():
        hypotheses.append({
            "id": f"H_creative_{row['creative_type']}",
            "reason": f"Creative type '{row['creative_type']}' underperforms.",
            "evidence": {
                "ctr": float(row["ctr"]),
                "roas": float(row["roas"])
            },
            "confidence": 0.75
        })

    # --- Hypothesis 4: Audience variation ---
    if len(audience) >= 2:
        audience_sorted = audience.sort_values("roas")
        worst = audience_sorted.iloc[0]
        best = audience_sorted.iloc[-1]

        hypotheses.append({
            "id": "H_audience",
            "reason": "Audience ROAS varies significantly.",
            "evidence": {
                "worst_audience": worst["audience_type"],
                "worst_roas": float(worst["roas"]),
                "best_audience": best["audience_type"],
                "best_roas": float(best["roas"])
            },
            "confidence": 0.79
        })

    return {"hypotheses": hypotheses}
