import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import os

# 绝对路径，指向 VultrApi 根目录
WATCH_DIR = "/home/ubuntu/codersun/VultrApi"

class RestartHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command)
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"{event.src_path} changed, restarting...")
            self.process.terminate()
            self.process.wait()
            self.process = subprocess.Popen(self.command)

if __name__ == "__main__":
    event_handler = RestartHandler([sys.executable, "app.py"])
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=True)
    observer.start()
    print(f"Watching {WATCH_DIR} for .py changes ...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()