import click
import os
import json
from pathlib import Path
from utils.encryption import decrypt

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
        click.echo(f"[!] Store file not found. Creating a new one at {CONFIG_PATH}.")
        with open(STORE_PATH, 'w') as f:
            json.dump({}, f)


@click.command()
@click.option('--site', '-s', prompt='Website name', required=True, help='The website you are trying to get the password of.')
def cli(site):
    """Retrieve password from user directory."""
    ensure_store_file()

    # Load current data from the store.json
    with open(STORE_PATH, 'r') as f:
        data = json.load(f)
    
    encrypted_password = data.get(site)

    if encrypted_password == None:
        click.echo(f"[FAILURE] No password was found for {site}.")
    else:
        decrypted_password = decrypt(encrypted_password)
        click.echo(f"[SUCCESS] The password for {site} is:\t{decrypted_password}")


if __name__ == '__main__':
    cli()
