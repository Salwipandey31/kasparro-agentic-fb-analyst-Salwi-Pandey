import json
from pathlib import Path
from .jsonsafe import make_json_safe
import yaml

def save_json(obj, path):
    """Save Python object as JSON with JSON-safe formatting."""
    safe_obj = make_json_safe(obj)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(safe_obj, f, indent=2)

def load_yaml(path):
    """Load YAML config file."""
    with open(path) as f:
        return yaml.safe_load(f)
