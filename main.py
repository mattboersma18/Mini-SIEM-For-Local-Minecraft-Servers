import os
from dotenv import load_dotenv
from paramiko import SSHClient, AutoAddPolicy
from parser import parse_line
from rules import check_rapid_reconnection, check_multiple_usernames, check_malformed_username
import severity
from rcon_client import ban_ip, kick_player
from response import decide

load_dotenv()

HOST = os.getenv("MC_HOST")
PORT = int(os.getenv("MC_SSH_PORT", 22))
USERNAME = os.getenv("MC_SSH_USER")
PASSWORD = os.getenv("MC_SSH_PASSWORD")
LOG_PATH = os.getenv("MC_LOG_PATH")

def process_event(event):
    print(event)
    for check in (check_rapid_reconnection, check_multiple_usernames, check_malformed_username):
        result = check(event)
        if not result:
            continue

        level = severity.get_severity(result["score"])
        print(f"IP {result['ip']} — score: {result['score']:.1f} — severity: {level}")

        action = decide(result["ip"], result["score"], level)
        handle(action, result, event)


def handle(action, result, event):
    if action == "ban":
        print(f"Banned {result['ip']}")
    elif action == "kick":
        kick_player(event.get("username", ""))
        print(f"Kicked {event.get('username')}")

with SSHClient() as client:
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(hostname=HOST, port=PORT, username=USERNAME, password=PASSWORD, timeout=10)
    command = "journalctl -u minecraft.service -f -n 0"

    stdin, stdout, stderr = client.exec_command(command)
    print(f"Connected to {HOST}:{PORT} as {USERNAME}. Streaming logs from {LOG_PATH}...\n")

    try:
        for line in stdout:
            event = parse_line(line.strip())
            if event:
                process_event(event)
    except KeyboardInterrupt:
        print("\nLog streaming interrupted by user.")
