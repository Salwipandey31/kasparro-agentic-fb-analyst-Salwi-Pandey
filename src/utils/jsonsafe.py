import numpy as np
import pandas as pd

def make_json_safe(obj):
    """Recursively convert pandas/numpy objects into JSON-safe types."""

    # Basic Python types are fine
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj

    # numpy types
    if isinstance(obj, (np.integer, np.int64, np.int32, np.int16)):
        return int(obj)
    if isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)

    # Timestamps → string
    if isinstance(obj, pd.Timestamp):
        return obj.isoformat()

    # pandas Series → dict
    if isinstance(obj, pd.Series):
        return make_json_safe(obj.to_dict())

    # pandas DataFrame → record list
    if isinstance(obj, pd.DataFrame):
        return make_json_safe(obj.to_dict(orient="records"))

    # dict → recursively clean values
    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    # list → clean each item
    if isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    # fallback
    return str(obj)
