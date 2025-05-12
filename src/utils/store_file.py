import click
import os
import json
from pathlib import Path

# Windows: C:\Users\NAME\.config\jss\store.json
CONFIG_PATH = os.environ.get("XDG_CONFIG_HOME", os.path.join(Path.home(), ".config"))
STORE_PATH = os.path.join(CONFIG_PATH, "jss", "store.json")
TEMP_PATH = os.path.join(CONFIG_PATH, "jss", "temp.json")  # For test case


def ensure_store_file(path):
    """
    Helper function
    Checks to make sure the store.json file exists in the user directory. If none, then create a new one.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create a new file if config file does not exists
    if not os.path.exists(path):
        click.echo(f"[WARNING] Store file not found. Creating a new one at {path}.")
        with open(path, 'w') as f:
            json.dump({}, f)


def create_temp_file():
    os.makedirs(os.path.dirname(TEMP_PATH), exist_ok=True)
    with open(TEMP_PATH, 'w') as f:
        json.dump({}, f)


def remove_temp_file():
    os.makedirs(os.path.dirname(TEMP_PATH), exist_ok=True)
    if os.path.exists(TEMP_PATH):
        os.remove(TEMP_PATH)