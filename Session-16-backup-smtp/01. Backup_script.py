import os
import shutil
from datetime import datetime
# for windows
# source_dir= './'
# backup_dir= 'D://backups/'
#declare Source and Dest Directory inside linux
source_dir= '/home/sonam/developers'
backup_dir= '/home/sonam/backups'
#Create backup Directory if not exist
os.makedirs(backup_dir,exist_ok=True)
#Generate Timestamp
timestamp=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
#Create backup filename 
backup_file_name=f"backup-{timestamp}"

back_path=os.path.join(backup_dir,backup_file_name)
shutil.make_archive(back_path,'zip',source_dir)
