# Kasparro — Agentic Facebook Performance Analyst  
By: Salwi Pandey

This repository implements a complete **Agentic Multi-Agent System** designed for the **Kasparro Applied AI Engineer Assignment**.  
The system autonomously analyzes Facebook Ads performance, explains ROAS/CTR changes, validates hypotheses, and proposes data-driven creative improvements.

---

# 🚀 Quick Start

## 1️⃣ Python Environment
```bash
python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  
# Windows: .venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Run the Full Multi-Agent Pipeline
make run

📂 Data Configuration
Using full dataset

Place CSV in any folder and set:
export DATA_CSV="/path/to/synthetic_fb_ads_undergarments.csv"
Using sample dataset (default)

The repo includes:
data/sample_ads.csv

Additional documentation:
data/README.md

⚙️ Config (config/config.yaml)

Edit thresholds, seeds, paths, runtime mode:

python: "3.10"
seed: 42

paths:
  data_path: "data/sample_ads.csv"
  output_dir: "reports"
  logs_dir: "logs"

thresholds:
  confidence_min: 0.6
  roas_drop_pct: 0.05
  ctr_drop_pct: 0.03
  creative_roas_delta_pct: 0.20
  audience_roas_diff_pct: 0.25

runtime:
  use_sample_data: true

🧠 Agentic Architecture
User Query
   │
   ▼
Planner Agent
   │ breaks tasks
   ▼
Data Agent
   │ loads + summarizes
   ▼
Insight Agent
   │ generates hypotheses
   ▼
Evaluator Agent
   │ validates hypotheses
   ▼
Creative Generator Agent
   │ generates new creatives
   ▼
Final Report

📁 Repository Map
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
│   ├── insights.json
│   ├── creatives.json
│   └── final_report.json
│
└── tests/
    └── test_evaluator.py

🧪 Testing

Run evaluator tests:
make test
Ensures:
evaluator runs
threshold logic works
output schema matches expected format

📊 Outputs

Generated after running pipeline:
reports/final_report.json     – Full multi-agent output
reports/insights.json         – Hypotheses + reasoning
reports/creatives.json        – Creative recommendations
logs/run_log.json             – Execution evidence

📦 Release
Version tag used for submission:
v1.0

🧵 Self-Review PR

A Pull Request titled:
self-review

Includes:
design choices
reasoning architecture
rubric mapping
tradeoffs

🙌 Author
Salwi Pandey Kasparro Applied AI Engineer Assignment ```
