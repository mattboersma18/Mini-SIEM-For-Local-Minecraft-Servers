import os
from dotenv import load_dotenv
from paramiko import SSHClient, AutoAddPolicy
from parser import parse_line
from rules import check_brute_force

load_dotenv()

HOST = os.getenv("MC_HOST")
PORT = int(os.getenv("MC_SSH_PORT", 22))
USERNAME = os.getenv("MC_SSH_USER")
PASSWORD = os.getenv("MC_SSH_PASSWORD")
LOG_PATH = os.getenv("MC_LOG_PATH")

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
                 print(event)
                 alert = check_brute_force(event)
                 if alert:
                        print(alert)
    except KeyboardInterrupt:
            print("\nLog streaming interrupted by user.")

