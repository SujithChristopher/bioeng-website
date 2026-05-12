import ftplib
import os
import time
from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]
LOCAL_BACKUP_DIR = "backup_site"

def get_ftp_connection():
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

def download_recursive(ftp, remote_path, local_path):
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    
    try:
        ftp.cwd(remote_path)
    except Exception as e:
        print(f"Could not enter {remote_path}: {e}")
        return

    items = []
    try:
        ftp.dir(items.append)
    except Exception as e:
        print(f"Failed to list directory {remote_path}: {e}. Reconnecting...")
        return

    for line in items:
        parts = line.split()
        if len(parts) < 9:
            continue
        
        name = " ".join(parts[8:])
        if name in [".", "..", "_backup_old_site"]:
            continue
            
        is_dir = parts[0].startswith('d')
        local_item_path = os.path.join(local_path, name)
        
        if is_dir:
            download_recursive(ftp, name, local_item_path)
            try:
                ftp.cwd("..")
            except:
                pass
        else:
            if os.path.exists(local_item_path):
                continue
                
            print(f"Downloading file {name}...")
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    with open(local_item_path, "wb") as f:
                        ftp.retrbinary(f"RETR {name}", f.write)
                    break
                except Exception as e:
                    print(f"Failed to download {name} (attempt {attempt+1}): {e}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                        try:
                            ftp = get_ftp_connection()
                            ftp.cwd(remote_path)
                        except:
                            pass

def backup_main():
    while True:
        try:
            ftp = get_ftp_connection()
            print("Logged in successfully")
            
            if not os.path.exists(LOCAL_BACKUP_DIR):
                os.makedirs(LOCAL_BACKUP_DIR)
                
            print("Starting local download (with resume support)...")
            download_recursive(ftp, ".", LOCAL_BACKUP_DIR)
            print("Local download check complete.")
            
            print("Moving files to _backup_old_site on server...")
            ftp.cwd("/")
            root_items = []
            ftp.dir(root_items.append)
            
            if not any("_backup_old_site" in line for line in root_items):
                ftp.mkd("_backup_old_site")
            
            for line in root_items:
                parts = line.split()
                if len(parts) < 9: continue
                name = " ".join(parts[8:])
                if name in [".", "..", "_backup_old_site"]:
                    continue
                
                print(f"Moving {name} to _backup_old_site/")
                try:
                    ftp.rename(name, f"_backup_old_site/{name}")
                except Exception as e:
                    print(f"Failed to move {name}: {e}")
            
            ftp.quit()
            print("Backup and cleanup complete.")
            break
        except Exception as e:
            print(f"Top-level error: {e}. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    backup_main()
