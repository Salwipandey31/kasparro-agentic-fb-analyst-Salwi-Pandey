# Kasparro Agentic Facebook Performance Analyst  
### By: Salwi Pandey

This repository implements a full **Agentic Multi-Agent System** designed for the **Kasparro Applied AI Engineer Assignment**.  
The system diagnoses **Facebook Ads performance**, analyzes trends, validates hypotheses, and generates **creative recommendations**.

---

# 🚀 Quick Start

## 1️⃣ Install all dependencies
```bash
pip install -r requirements.txt

2️⃣ Run the full agentic pipeline
This command runs:
Planner Agent
Data Agent
Insight Agent
Evaluator Agent
Creative Generator
Final Report Builder
make run

Generated outputs:
reports/final_report.json
reports/insights.json
reports/creatives.json
logs/run_log.json
make test

User Query
     │
     ▼
Planner Agent
     │  Decomposes tasks
     ▼
Data Agent
     │  Loads + validates + summarizes data
     ▼
Insight Agent
     │  Generates hypotheses with evidence
     ▼
Evaluator Agent
     │  Validates hypotheses (threshold-based)
     ▼
Creative Generator Agent
     │  Generates new creative directions
     ▼
Final Report Builder


📁 Repository Structure
kasparro-agentic-fb-analyst-yourname/
│
├── README.md
├── Makefile
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   ├── creative_agent.py
│   │   └── __init__.py
│   │
│   ├── orchestrator/
│   │   ├── pipeline.py
│   │   └── __init__.py
│   │
│   └── utils/
│       ├── jsonsafe.py
│       ├── io.py
│       └── __init__.py
│
├── prompts/
│   ├── PLANNER.md
│   ├── DATA_AGENT.md
│   ├── INSIGHT_AGENT.md
│   ├── EVALUATOR_AGENT.md
│   └── CREATIVE_AGENT.md
│
├── data/
│   ├── sample_ads.csv
│   └── README.md
│
├── logs/
│   └── run_log.json
│
├── reports/
│   ├── final_report.json
│   ├── insights.json
│   └── creatives.json
│
└── tests/
    └── test_evaluator.py

⚙️ Configuration (config.yaml)
config/config.yaml
Includes:
seed value
data paths
report/log paths
thresholds for performance drops
sample mode switch

🧩 Agent Details
🟦 Planner Agent
Decomposes user query into tasks
Defines input/output schemas
Provides retry logic and confidence levels

🟩 Data Agent
Loads dataset
Validates columns
Summaries by day, campaign, creative type, audience
Identifies low-CTR and low-ROAS segments

🟨 Insight Agent
Detects performance patterns
Generates hypotheses: CTR drop, ROAS drop, audience differences, creative fatigue
Provides evidence + confidence

🟧 Evaluator Agent
Applies threshold-based quantitative validation
Marks hypotheses as Supported or Rejected
Generates confidence scores

🟪 Creative Generator Agent
Analyzes low-CTR campaigns
Extracts themes from creative_message
Detects issues

Generates:
Headlines
Primary text
CTAs

📊 Example Output Snippet (final_report.json)
{
  "insights": {
    "hypotheses": [
      {
        "id": "H1",
        "reason": "Recent ROAS decline detected.",
        "confidence": 0.85
      }
    ]
  },
  "creative_recommendations": [
    {
      "campaign_name": "Campaign A",
      "new_headlines": [
        "Feel Comfort All Day — Designed for Daily Wear"
      ]
    }
  ]
}


🙌 Author

Salwi Pandey
Kasparro Applied AI Engineer Assignment
