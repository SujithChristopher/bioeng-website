import ftplib
import os
import concurrent.futures
import time

from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]
LOCAL_BACKUP_DIR = "backup_site"

def get_ftp():
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

def download_file(remote_path, local_path):
    if os.path.exists(local_path):
        return
    
    dir_name = os.path.dirname(local_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
        
    try:
        ftp = get_ftp()
        print(f"Downloading {remote_path}...")
        with open(local_path, "wb") as f:
            ftp.retrbinary(f"RETR {remote_path}", f.write)
        ftp.quit()
    except Exception as e:
        print(f"Failed {remote_path}: {e}")

def get_all_files(ftp, current_dir="."):
    files = []
    items = []
    ftp.dir(items.append)
    
    for line in items:
        parts = line.split()
        if len(parts) < 9: continue
        name = " ".join(parts[8:])
        if name in [".", "..", "_backup_old_site"]: continue
        
        is_dir = parts[0].startswith('d')
        remote_path = os.path.join(current_dir, name).replace("\\", "/")
        
        if is_dir:
            try:
                ftp.cwd(name)
                files.extend(get_all_files(ftp, remote_path))
                ftp.cwd("..")
            except:
                pass
        else:
            files.append(remote_path)
    return files

def main():
    ftp = get_ftp()
    print("Collecting file list...")
    all_files = get_all_files(ftp)
    ftp.quit()
    
    print(f"Total files to download: {len(all_files)}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for rf in all_files:
            lf = os.path.join(LOCAL_BACKUP_DIR, rf.replace("/", os.sep))
            futures.append(executor.submit(download_file, rf, lf))
        
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
