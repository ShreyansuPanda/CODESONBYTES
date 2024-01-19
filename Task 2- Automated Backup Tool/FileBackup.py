#CodeOnBytes Task 2:Automated Backup Tool:- This is a project that automate backup of files in folder from one location to other
#Change the location of Source folder and Destination Folder according to your need
#Change the time as per need, use 24hr format
import os
import shutil
import schedule
import time

def backup(src, dst):
    try:
        if not os.path.exists(dst):
            os.makedirs(dst)

        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=True)
            else:
                shutil.copy2(s, d)

        print(f"Backup completed successfully from {src} to {dst}")
    except Exception as e:
        print(f"An error occurred during backup: {str(e)}")

def schedule_backup():
    backup_time = "10:00"  # schedule time in 24h format
    schedule.every().day.at(backup_time).do(backup, source, destination)
    print(f"Backup scheduled for {backup_time} every day")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    source = r"E:\programming\Python\CodesonBytes\File Backup\Source File"
    destination = r"E:\programming\Python\CodesonBytes\File Backup\Destination File"
    schedule_backup()
