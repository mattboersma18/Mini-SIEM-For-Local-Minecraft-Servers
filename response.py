WHITELIST_IPS = {"100.70.225.26"}
ALREADY_ACTIONED = set()

def decide(ip, score, level):
    if ip in WHITELIST_IPS:
        return None
    if ip in ALREADY_ACTIONED:
        return None

    if level == "High":
        ALREADY_ACTIONED.add(ip)
        return "ban"
    elif level == "Medium":
        ALREADY_ACTIONED.add(ip)
        return "kick"
    return None