import os

def load_env(path=".env"):
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    env[key] = value
    return env

def get_ftp_config():
    config = load_env()
    return {
        "host": config.get("FTP_HOST"),
        "user": config.get("FTP_USER"),
        "pass": config.get("FTP_PASS")
    }
