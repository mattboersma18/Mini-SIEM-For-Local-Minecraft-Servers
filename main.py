import os
from dotenv import load_dotenv
from paramiko import SSHClient, AutoAddPolicy

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
    command = f"tail -F -n 0 {LOG_PATH}"

    stdin, stdout, stderr = client.exec_command(command)
    print(f"Connected to {HOST}:{PORT} as {USERNAME}. Streaming logs from {LOG_PATH}...\n")

    try:
        for line in stdout:
            print(line.strip())
    except KeyboardInterrupt:
            print("\nLog streaming interrupted by user.")

