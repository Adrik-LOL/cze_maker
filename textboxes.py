import tkinter as tk
from tkinter import messagebox
import random
import json

# Parse conf.ini file
with open('conf.ini', 'r') as conf_file:
    lines = conf_file.readlines()
    for line in lines:
        if line.startswith("errors ="):
            errors_json_path = line.split("=")[1].strip().strip('"')

# Load error messages from errors.json
with open(errors_json_path, 'r') as errors_file:
    errors_data = json.load(errors_file)
    errors = errors_data["ERROR_CODES"]

def generate_error():
    # Select a random error message
    error = random.choice(errors)

    # Display the error message in a message box
    messagebox.showerror(error["TITLE"], error["TEXT"] )

if __name__ == "__main__":
    generate_error()
