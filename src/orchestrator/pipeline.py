import pandas as pd
from pathlib import Path

from src.agents.planner import planner_agent
from src.agents.data_agent import data_agent_load_and_summarize
from src.agents.insight_agent import insight_agent_generate_insights
from src.agents.evaluator_agent import evaluator_agent
from src.agents.creative_agent import creative_generator_agent

from src.utils.io import save_json, load_yaml
from src.utils.jsonsafe import make_json_safe

def run_pipeline(user_query, config_path="config/config.yaml"):
    """
    Main orchestrator for the multi-agent system.
    """

    # Load config
    cfg = load_yaml(config_path)
    data_path = cfg["paths"]["data_path"]
    output_dir = cfg["paths"]["output_dir"]
    logs_dir = cfg["paths"]["logs_dir"]

    Path(output_dir).mkdir(exist_ok=True, parents=True)
    Path(logs_dir).mkdir(exist_ok=True, parents=True)

    # --- Step 1: Planner ---
    plan = planner_agent(user_query, {})

    # --- Step 2: Data Agent ---
    data_result = data_agent_load_and_summarize(data_path)
    if data_result["status"] != "success":
        save_json(data_result, f"{logs_dir}/error_log.json")
        return data_result

    # --- Step 3: Insight Agent ---
    insights = insight_agent_generate_insights(data_result["summary"])

    # --- Step 4: Evaluator Agent ---
    evaluated = evaluator_agent(insights, data_result["summary"])

    # --- Step 5: Creative Agent ---
    full_df = pd.read_csv(data_path, parse_dates=["date"])
    creatives = creative_generator_agent(data_result["summary"], full_df)

    # --- Step 6: Combine Final Report ---
    final_report = {
        "user_query": user_query,
        "planner": plan,
        "data_summary": data_result["summary"],
        "insights": insights,
        "evaluated_hypotheses": evaluated,
        "creative_recommendations": creatives
    }

    # Save outputs
    save_json(final_report, f"{output_dir}/final_report.json")
    save_json(insights, f"{output_dir}/insights.json")
    save_json(creatives, f"{output_dir}/creatives.json")

    # Save execution log
    save_json({"status": "ok", "message": "Pipeline executed"}, f"{logs_dir}/run_log.json")

    return final_report
