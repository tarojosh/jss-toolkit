import click
import os
import json
from pathlib import Path


# Windows: C:\Users\NAME\.config
CONFIG_PATH = os.environ.get("XDG_CONFIG_HOME", os.path.join(Path.home(), ".config"))
STORE_PATH = os.path.join(CONFIG_PATH, "jss", "store.json")

def ensure_store_file():
    """
    Helper function
    Checks to make sure the store.json file exists in the user directory. If none, then create a new one.
    """
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    # Create a new file if config file does not exists
    if not os.path.exists(STORE_PATH):
        click.echo(f"[WARNING] Store file not found. Creating a new one at {CONFIG_PATH}.")
        with open(STORE_PATH, 'w') as f:
            json.dump({}, f)