import time
import severity

RECENT_LOGINS = {}

THRESHOLD = 3
WINDOW_SECONDS = 30
POINTS_PER_HIT = 3

def check_rapid_reconnection(event):
    if event["event_type"] != "login":
        return None

    ip = event["ip"]
    now = time.time()

    history = RECENT_LOGINS.get(ip, [])
    history = [t for t in history if now - t < WINDOW_SECONDS]
    history.append(now)
    RECENT_LOGINS[ip] = history

    if len(history) >= THRESHOLD:
        score = severity.add_score(ip, POINTS_PER_HIT)
        return {"ip": ip, "score": score}

    return None



        
