import yaml

def load_config(path="config.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def score_metric(value, th):
    if value <= th["bad"]:
        return 0
    if value >= th["good"]:
        return 100
    if value <= th["ok"]:
        return 50 * (value - th["bad"]) / (th["ok"] - th["bad"])
    return 50 + 50 * (value - th["ok"]) / (th["good"] - th["ok"])

def overall_score(values, cfg):
    total = 0
    breakdown = {}
    for metric, value in values.items():
        s = score_metric(value, cfg["thresholds"][metric])
        breakdown[metric] = round(s, 1)
        total += s * cfg["weights"][metric]
    return round(total, 1), breakdown
