import os

for dirpath, dirnames, filenames in os.walk(r'C:\Python\pythonProject'):
    print(f'Found directory: {dirpath}')
    for dirname in dirnames:
        print(f'\tSub-directory: {dirname}')
    for filename in filenames:
        print(f'\tFile: {filename}')


# Write a Python script using the os module that searches for all .log files in a given directory and its subdirectories,
# moves them to a backup directory named backup_logs, and logs each move operation with a timestamp to a file named move_log.txt.

import os
import shutil
from datetime import datetime


def move_log_files(source_dir, backup_dir, log_file):
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)

    # Open the log file in append mode
    with open(log_file, 'a') as log:
        # Traverse the directory tree
        for dirpath, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                if filename.endswith('.log'):
                    source_file = os.path.join(dirpath, filename)
                    destination_file = os.path.join(backup_dir, filename)

                    try:
                        shutil.move(source_file, destination_file)
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = f"{timestamp} - Moved: {source_file} -> {destination_file}\n"
                        log.write(log_entry)
                        print(log_entry.strip())
                    except Exception as e:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        error_entry = f"{timestamp} - Failed to move {source_file}: {e}\n"
                        log.write(error_entry)
                        print(error_entry.strip())


if __name__ == "__main__":
    source_directory = '/path/to/source_directory'
    backup_directory = '/path/to/backup_logs'
    log_filename = 'move_log.txt'

    move_log_files(source_directory, backup_directory, log_filename)
    print("Log file updated.")
