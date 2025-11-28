def planner_agent(user_query, dataset_summary):
    """
    Planner Agent:
    Breaks down the query into ordered tasks with confidence scores.
    """

    return {
        "query": user_query,
        "goal": "Diagnose performance changes and generate creative recommendations",
        "tasks": [
            {
                "id": "task_1",
                "title": "Data Loading & Validation",
                "description": "Load CSV, validate columns, check missing values, parse dates.",
                "inputs": ["dataset_path"],
                "outputs": ["clean_df", "validation_report"],
                "confidence": 0.95
            },
            {
                "id": "task_2",
                "title": "Performance Summary",
                "description": "Summaries for ROAS, CTR, spend, impressions, clicks.",
                "inputs": ["clean_df"],
                "outputs": ["performance_tables", "trend_summaries"],
                "confidence": 0.92
            },
            {
                "id": "task_3",
                "title": "Insight Generation",
                "description": "Generate hypotheses explaining performance changes.",
                "inputs": ["performance_tables"],
                "outputs": ["hypotheses"],
                "confidence": 0.87
            },
            {
                "id": "task_4",
                "title": "Hypothesis Evaluation",
                "description": "Test hypotheses with quantitative metrics.",
                "inputs": ["hypotheses", "clean_df"],
                "outputs": ["validated_insights", "confidence_scores"],
                "confidence": 0.89
            },
            {
                "id": "task_5",
                "title": "Creative Recommendation Generator",
                "description": "Produce new creative ideas for low CTR campaigns.",
                "inputs": ["clean_df"],
                "outputs": ["creative_recommendations"],
                "confidence": 0.91
            },
            {
                "id": "task_6",
                "title": "Final Report Assembly",
                "description": "Combine all insights and creatives into final report.",
                "inputs": ["validated_insights", "creative_recommendations"],
                "outputs": ["final_report"],
                "confidence": 0.93
            }
        ],
        "retry_logic": {
            "low_confidence_threshold": 0.6,
            "on_low_confidence": "re-run sampling or request additional data"
        }
    }
