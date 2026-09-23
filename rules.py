import time
import severity
import re

RECENT_LOGINS = {}
IP_USERNAMES = {}

THRESHOLD = 3
WINDOW_SECONDS = 30
POINTS_PER_HIT = 3

USERNAME_THRESHOLD = 3
USERNAME_WINDOW_SECONDS = 300
POINTS_PER_HIT_USER = 6

SUSPICIOUS_USERNAME_PATTERN = re.compile(r"^[a-f0-9]{8,}$|_?\d{5,}$")
MALFORMED_POINTS = 4

SUSPICIOUS_REASON_KEYWORDS = ["timed out", "internal exception", "decoderexception", "invalid"]
DISCONNECT_REASON_POINTS = 3

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
        return severity.report(ip, POINTS_PER_HIT)

    return None

def check_multiple_usernames(event):
    if event["event_type"] != "login":
        return None

    ip = event["ip"]
    username = event["username"]
    now = time.time()

    history = IP_USERNAMES.get(ip, [])
    history = [(u, t) for (u, t) in history if now - t < USERNAME_WINDOW_SECONDS]
    history.append((username, now))
    IP_USERNAMES[ip] = history

    distinct_usernames = {u for (u,t) in history}

    if len(distinct_usernames) >= USERNAME_THRESHOLD:
        return severity.report(ip, POINTS_PER_HIT_USER)

    return None

def check_malformed_username(event):
    if event["event_type"] != "login":
            return None

    ip = event["ip"]
    username = event["username"]

    if SUSPICIOUS_USERNAME_PATTERN.match(username):
        return severity.report(ip, MALFORMED_POINTS, username = username)

    return None

def check_disconnect_reason(event):
    if event["event_type"] != "disconnect":
        return None

    ip = event.get("ip")
    reason = event["reason"].lower()

    if any(keyword in reason for keyword in SUSPICIOUS_REASON_KEYWORDS):
        return severity.report(ip, DISCONNECT_REASON_POINTS)

    return None