import time

RECENT_LOGINS = {}

THRESHOLD = 3
WINDOW_SECONDS = 30

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
        return f"ALERT: Potential rapid reconnection detected from IP {ip}. {len(history)} login attempts in the last {WINDOW_SECONDS} seconds."

    return None



        
