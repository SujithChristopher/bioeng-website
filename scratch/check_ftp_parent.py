import ftplib
from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]

def check_parent():
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        print(f"Current dir: {ftp.pwd()}")
        
        ftp.cwd("..")
        print(f"Parent dir: {ftp.pwd()}")
        items = []
        ftp.dir(items.append)
        for item in items:
            print(item)
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_parent()
