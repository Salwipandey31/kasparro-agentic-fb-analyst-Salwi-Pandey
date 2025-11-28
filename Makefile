install:
	pip install -r requirements.txt

run:
	python -c "from src.orchestrator.pipeline import run_pipeline; run_pipeline('Explain ROAS change and suggest creatives', 'config/config.yaml')"

test:
	pytest -q
