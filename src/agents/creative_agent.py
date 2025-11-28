import pandas as pd

def creative_generator_agent(data_summary, full_df):
    """
    Creative Generator Agent:
    Generates improved creative ideas for low CTR campaigns.
    """

    campaign_summary = pd.DataFrame(data_summary["campaign_summary"])
    low_ctr_campaigns = campaign_summary.sort_values("ctr").head(5)["campaign_name"].tolist()

    recommendations = []

    for campaign in low_ctr_campaigns:
        df_campaign = full_df[full_df["campaign_name"] == campaign]

        if df_campaign.empty:
            recommendations.append({
                "campaign_name": campaign,
                "current_theme": "N/A",
                "issues_detected": ["No creative messages found"],
                "new_headlines": [],
                "new_messages": [],
                "new_ctas": []
            })
            continue

        messages = df_campaign["creative_message"].dropna().tolist()
        combined_text = " ".join(messages).lower()

        # Theme extraction
        themes = []
        if "comfort" in combined_text: themes.append("comfort")
        if "premium" in combined_text: themes.append("premium quality")
        if "soft" in combined_text: themes.append("softness")
        if "sale" in combined_text or "discount" in combined_text: themes.append("offers/discounts")
        if "breathable" in combined_text: themes.append("breathable fabric")

        current_theme = ", ".join(themes) if themes else "generic / unclear theme"

        # Detect issues
        issues = []
        if not "comfort" in combined_text:
            issues.append("Missing comfort angle")
        if not ("sale" in combined_text or "discount" in combined_text):
            issues.append("No urgency or promotional hook")
        if len(set(messages)) < 3:
            issues.append("Limited creative variation")

        # Generate new creative directions
        new_headlines = [
            "Feel Comfort All Day — Designed for Daily Wear",
            "Your New Everyday Essential: Soft, Premium, Breathable",
            "Comfort Meets Style — Try the Upgrade",
            "Experience Softness Like Never Before"
        ]

        new_messages = [
            "Discover all-day softness with breathable, high-quality fabric.",
            "Made for movement — perfect comfort from morning to night.",
            "Engineered for everyday wear with premium materials.",
            "Feel confident and comfortable in every moment."
        ]

        new_ctas = [
            "Shop Now",
            "Try It Today",
            "Feel the Comfort",
            "Limited Offer — Buy Now"
        ]

        recommendations.append({
            "campaign_name": campaign,
            "current_theme": current_theme,
            "issues_detected": issues,
            "new_headlines": new_headlines,
            "new_messages": new_messages,
            "new_ctas": new_ctas
        })

    return {"creative_recommendations": recommendations}
