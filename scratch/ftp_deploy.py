import ftplib
import os
from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]
LOCAL_DIST_DIR = "dist"

def upload_recursive(ftp, local_dir):
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        if os.path.isfile(local_path):
            print(f"Uploading {item}...")
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {item}", f)
        elif os.path.isdir(local_path):
            print(f"Creating directory {item}...")
            try:
                ftp.mkd(item)
            except:
                pass # Already exists
            ftp.cwd(item)
            upload_recursive(ftp, local_path)
            ftp.cwd("..")

def deploy_main():
    if not os.path.exists(LOCAL_DIST_DIR):
        print(f"Error: {LOCAL_DIST_DIR} directory not found. Please run 'npm run build' first.")
        return

    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        print("Logged in successfully")
        
        ftp.cwd("/")
        # Check for public_html
        items = []
        ftp.dir(items.append)
        if any("public_html" in line for line in items):
            print("Targeting public_html directory...")
            ftp.cwd("public_html")
            
        print("Starting upload...")
        upload_recursive(ftp, LOCAL_DIST_DIR)
        
        ftp.quit()
        print("Deployment complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    deploy_main()
