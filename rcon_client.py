import os
from mcrcon import MCRcon
from dotenv import load_dotenv

RCON_HOST = os.getenv("MC_HOST")
RCON_PORT = int(os.getenv("MC_RCON_PORT", 25575))
RCON_PASSWORD = os.getenv("MC_RCON_PASSWORD")

def send_command(command):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port = RCON_PORT) as mcr:
            response = mcr.command(command)
            return response
    except Exception as e:
        print(f"RCON error: {e}")
        return None

def ban_ip(ip, reason = "Flagged"):
    return send_command(f"ban-ip {ip} {reason}")

def kick_player(username, reason = "Flagged"):
    return send_command(f"kick {username} {reason}")

