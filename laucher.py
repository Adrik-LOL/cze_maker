import tkinter as tk
from tkinter import messagebox
import random
import json
import time
import os

file_path = None

# Parse conf.ini file
with open('conf.ini', 'r') as conf_file:
    lines = conf_file.readlines()
    start_delay = 0
    errors_delay = 500
    errors_json_path = None
    for line in lines:
        if line.startswith("start_delay.ms"):
            start_delay = int(line.split("=")[1].strip())
        elif line.startswith("errors_delay.ms"):
            errors_delay = int(line.split("=")[1].strip())

def launch():
    # Delay start if specified in conf.ini
    time.sleep(start_delay / 1000.0)

    # Generate errors with specified delay
    while True:
        file_path = "textboxes.exe"
        import subprocess
        subprocess.Popen(file_path)

        time.sleep(errors_delay / 1000.0)

if __name__ == "__main__":
    launch()
