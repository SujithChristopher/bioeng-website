import ftplib
import os

from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]
LOCAL_DIST_DIR = "dist"

def fix_deployment():
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        print("Logged in")
        
        # 1. Create public_html if it doesn't exist at root
        ftp.cwd("/")
        items = []
        ftp.dir(items.append)
        if not any("public_html" in line for line in items):
            print("Creating /public_html")
            ftp.mkd("public_html")
        
        # 2. Move new site files into public_html
        new_site_files = [
            "index.html", "cmc_logo.png", "favicon.svg", "group_pic.jpeg",
            "_astro", "education", "join-us", "news", "open-science",
            "publications", "research", "team", "team-photos"
        ]
        
        for item in new_site_files:
            print(f"Moving {item} to public_html/...")
            try:
                ftp.rename(item, f"public_html/{item}")
            except Exception as e:
                print(f"Failed to move {item}: {e}")
                
        ftp.quit()
        print("Fixed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_deployment()
