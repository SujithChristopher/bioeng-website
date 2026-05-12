import ftplib
import os
from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]
LOCAL_DIST_DIR = "dist"

def get_ftp():
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

def move_to_backup(ftp):
    print("Moving files to _backup_old_site on server...")
    ftp.cwd("/")
    items = []
    ftp.dir(items.append)
    
    if not any("_backup_old_site" in line for line in items):
        try:
            ftp.mkd("_backup_old_site")
            print("Created _backup_old_site")
        except:
            pass
            
    for line in items:
        parts = line.split()
        if len(parts) < 9: continue
        name = " ".join(parts[8:])
        if name in [".", "..", "_backup_old_site"]: continue
        
        print(f"Moving {name}...")
        try:
            ftp.rename(name, f"_backup_old_site/{name}")
        except Exception as e:
            print(f"Failed to move {name}: {e}")

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
                pass
            ftp.cwd(item)
            upload_recursive(ftp, local_path)
            ftp.cwd("..")

def main():
    try:
        ftp = get_ftp()
        move_to_backup(ftp)
        
        print("Starting deployment of new site...")
        ftp.cwd("/")
        # Some servers need public_html
        items = []
        ftp.dir(items.append)
        if any("public_html" in line for line in items):
            print("Targeting public_html directory...")
            ftp.cwd("public_html")
            
        upload_recursive(ftp, LOCAL_DIST_DIR)
        
        ftp.quit()
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
