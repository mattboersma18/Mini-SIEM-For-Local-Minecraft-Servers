import re

LOGIN_PATTERN = re.compile(
    r"\[(?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+)\]: "
    r"(?P<username>\w+)\[/(?P<ip>[\d.]+):(?P<port>\d+)\] logged in"
)

DISCONNECT_PATTERN = re.compile(
    r"\[(?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+)\]: "
    r"(?P<username>\w+) lost connection: (?P<reason>.+)"
)

def parse_line(line: str):
    login_match = LOGIN_PATTERN.search(line)
    if login_match:
        return {
            "event_type": "login",
            "username": login_match.group("username"),
            "ip": login_match.group("ip"),
            "time": login_match.group("time"),
        }

    disconnect_match = DISCONNECT_PATTERN.search(line)
    if disconnect_match:
        return {
            "event_type": "disconnect",
            "username": disconnect_match.group("username"),
            "reason": disconnect_match.group("reason"),
            "time": disconnect_match.group("time"),
        }

    return None
