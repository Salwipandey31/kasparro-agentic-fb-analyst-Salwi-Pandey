import sys
sys.path.append("/content/kasparro-agentic-fb-analyst-Salwi-Pandey")

import pandas as pd
from src.agents.evaluator_agent import evaluator_agent

def test_evaluator_runs():
    """Basic test to ensure evaluator runs correctly."""
    
    hypotheses = {
        "hypotheses": [
            {
                "id": "H1",
                "reason": "Test ROAS drop",
                "evidence": {"roas_before": 2.0, "roas_after": 1.5, "delta": -0.5},
                "confidence": 0.90
            }
        ]
    }

    data_summary = {
        "daily_summary": [],
        "campaign_summary": [{"roas": 2.0, "ctr": 1.0}],
        "creative_summary": [{"creative_type": "Image", "ctr": 1.0, "roas": 1.2}],
        "audience_summary": [{"audience_type": "Women", "ctr": 1.0, "roas": 2.0}]
    }

    result = evaluator_agent(hypotheses, data_summary)

    assert "evaluated_hypotheses" in result
    assert isinstance(result["evaluated_hypotheses"], list)
    assert len(result["evaluated_hypotheses"]) == 1
