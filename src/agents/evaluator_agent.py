import pandas as pd
import numpy as np

def evaluator_agent(hypotheses, data_summary):
    """
    Evaluator Agent:
    Validates hypotheses quantitatively and assigns support/confidence.
    """

    daily = pd.DataFrame(data_summary["daily_summary"])
    campaign = pd.DataFrame(data_summary["campaign_summary"])
    creative = pd.DataFrame(data_summary["creative_summary"])
    audience = pd.DataFrame(data_summary["audience_summary"])

    results = []

    # Baselines
    avg_roas = float(campaign["roas"].mean()) if len(campaign) else 0
    avg_ctr = float(campaign["ctr"].mean()) if len(campaign) else 0

    def evaluate_threshold(delta, threshold):
        """Return (is_supported, confidence)."""
        if abs(delta) >= threshold:
            return True, min(1.0, abs(delta) / (threshold * 2))
        else:
            return False, abs(delta) / threshold

    for h in hypotheses["hypotheses"]:
        h_id = h["id"]
        h_reason = h["reason"]
        evidence = h["evidence"]

        # --- H1: ROAS drop ---
        if h_id == "H1":
            delta = evidence["delta"]
            supported, conf = evaluate_threshold(delta, threshold=0.05 * evidence["roas_before"])
            results.append({
                "id": h_id,
                "reason": h_reason,
                "is_supported": supported,
                "confidence": float(conf),
                "evidence": evidence
            })
            continue

        # --- H2: CTR drop ---
        if h_id == "H2":
            delta = evidence["delta"]
            supported, conf = evaluate_threshold(delta, threshold=0.03 * evidence["ctr_before"])
            results.append({
                "id": h_id,
                "reason": h_reason,
                "is_supported": supported,
                "confidence": float(conf),
                "evidence": evidence
            })
            continue

        # --- Creative performance hypothesis ---
        if h_id.startswith("H_creative_"):
            roas_val = evidence["roas"]
            delta = roas_val - avg_roas
            supported, conf = evaluate_threshold(delta, threshold=0.20 * avg_roas)
            results.append({
                "id": h_id,
                "reason": h_reason,
                "is_supported": supported,
                "confidence": float(conf),
                "evidence": {
                    "creative_roas": float(roas_val),
                    "avg_roas": avg_roas,
                    "delta": float(delta)
                }
            })
            continue

        # --- Audience-based hypothesis ---
        if h_id == "H_audience":
            delta = evidence["worst_roas"] - evidence["best_roas"]
            supported, conf = evaluate_threshold(delta, threshold=0.25 * evidence["best_roas"])
            results.append({
                "id": h_id,
                "reason": h_reason,
                "is_supported": supported,
                "confidence": float(conf),
                "evidence": evidence
            })
            continue

        # default fallback
        results.append({
            "id": h_id,
            "reason": h_reason,
            "is_supported": False,
            "confidence": 0.1,
            "evidence": evidence
        })

    return {"evaluated_hypotheses": results}
