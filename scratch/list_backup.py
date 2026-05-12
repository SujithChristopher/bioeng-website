import ftplib

from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]

def list_backup():
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("_backup_old_site")
        items = []
        ftp.dir(items.append)
        for item in items:
            print(item)
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_backup()
