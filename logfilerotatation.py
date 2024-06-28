import os
import shutil
import logging

def rotate_logs(log_file, backup_dir, max_backups=5):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Rotate the existing logs
    for i in range(max_backups - 1, 0, -1):
        src = f"{log_file}.{i}"
        dst = f"{log_file}.{i + 1}"
        if os.path.exists(src):
            shutil.move(src, dst)

    # Backup the current log file
    if os.path.exists(log_file):
        shutil.move(log_file, f"{log_file}.1")

    # Truncate the original log file
    with open(log_file, 'w') as f:
        f.truncate(0)

    print(f"Rotated logs for {log_file}")

if __name__ == "__main__":
    log_file_path = "/path/to/logfile.log"
    backup_directory = "/path/to/log_backups"
    rotate_logs(log_file_path, backup_directory)
