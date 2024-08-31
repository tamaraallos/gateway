import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Directory paths
EMAILS_DIR = 'emails'
APPROVED_DIR = 'approved'
DECLINED_DIR = 'declined'

class EmailMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"New email detected: {event.src_path}")
            # Add code to notify the admin of a new email

def monitor_directory(directory):
    print(f"Starting email monitoring on {directory}")
    event_handler = EmailMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_directory(EMAILS_DIR)
