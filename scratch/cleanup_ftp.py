import ftplib
from utils import get_ftp_config

config = get_ftp_config()
FTP_HOST = config["host"]
FTP_USER = config["user"]
FTP_PASS = config["pass"]

def cleanup_ftp():
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        print("Logged in")
        
        ftp.cwd("/")
        lines = []
        ftp.dir(lines.append)
        
        team_found = False
        for line in lines:
            parts = line.split()
            if len(parts) >= 9:
                name = " ".join(parts[8:])
                if name == "team":
                    team_found = True
                    break
        
        if team_found:
            print("Removing old 'team' directory...")
            # Recursive delete
            def delete_recursive(path):
                ftp.cwd(path)
                items = []
                ftp.dir(items.append)
                for item in items:
                    p = item.split()
                    if len(p) < 9: continue
                    n = " ".join(p[8:])
                    if n in [".", ".."]: continue
                    if p[0].startswith('d'):
                        delete_recursive(n)
                    else:
                        ftp.delete(n)
                ftp.cwd("..")
                ftp.rmd(path)
            
            delete_recursive("team")
            print("Done.")
        else:
            print("Team directory not found.")
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cleanup_ftp()
