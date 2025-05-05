import click
import os
import json
from pathlib import Path
from utils.encryption import encrypt


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
@click.option('--site', '-s', prompt='Website name', required=True, help='Name of the website for the password.')
@click.option('--password', '-p', prompt='Password', required=True, help='Password being used for the website.')
def cli(site, password):
    """Store the website and password in user directory."""
    ensure_store_file()

    # Load current data from the store.json
    with open(STORE_PATH, 'r') as f:
        data = json.load(f)
    
    encypted_site = encrypt(site)

    if encypted_site in data:
        # Tell the user that website has already been stored with a password
        # Ask if they want to update existing password.
        replace_password = click.confirm(f"[WARNING] '{site}' is already stored in file. Do you want to update the password?")
        if not replace_password:
            click.echo(f"[ABORT] Canceling password update...")
            return
        click.echo(f"[WARNING] Updating password for '{site}'...")
    else:
        click.echo(f"[INFO] '{site}' not found in file. Creating new key...")

    encrypted_password = encrypt(password)
    data[encypted_site] = encrypted_password

    # Save data to json
    with open(STORE_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo(f"[SUCCESS] Stored password for {site}.")


if __name__ == '__main__':
    cli()
