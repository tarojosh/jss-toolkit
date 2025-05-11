import click
import json
from utils.encryption import encrypt
from utils.store_file import ensure_store_file, STORE_PATH


@click.command()
@click.option('--site', '-s', prompt='Website name', required=True, help='Name of the website for the password.')
@click.option('--password', '-p', prompt='Password', required=True, help='Password being used for the website.')
@click.option('--path', hidden=True, default=STORE_PATH, help='Path of the file that will store the info. FOR TESTING ONLY.')
def cli(site, password, path):
    """Store and update website and password stored in the user directory."""
    ensure_store_file(path)

    # Load current data from the store.json
    with open(path, 'r') as f:
        data = json.load(f)
    
    encrypted_site = encrypt(site)

    if encrypted_site in data:
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
    data[encrypted_site] = encrypted_password

    # Save data to json
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo(f"[SUCCESS] Stored password for {site}.")
