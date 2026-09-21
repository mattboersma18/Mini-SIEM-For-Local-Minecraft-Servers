import time

IP_SCORES = {}

def add_score(ip, points):
    now = time.time()
    entry = IP_SCORES.get(ip, {"score": 0, "last_updated": now})

    elapsed_minutes = (now - entry["last_updated"]) / 60
    decayed_score = max(0, entry["score"] - elapsed_minutes)

    new_score = decayed_score + points
    IP_SCORES[ip] = {"score": new_score, "last_updated": now}

    return new_score

def get_severity(score):
    if score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    elif score > 0:
        return "Low"
    return None