import click
import json
from utils.encryption import encrypt
from utils.store_file import ensure_store_file, STORE_PATH


@click.command()
@click.option('--site', '-s', prompt='Website name', required=True, help='Name of the website to be deleted.')
@click.option('--path', hidden=True, default=STORE_PATH, help='Path of the file that will store the info. FOR TESTING ONLY.')
def cli(site, path):
    """Delete website and password record from the file."""
    ensure_store_file(path)

    # Load current data from the store.json
    with open(path, 'r') as f:
        data = json.load(f)
    
    encrypted_site = encrypt(site)

    if encrypted_site in data:
        # Ask if they want to delete the record
        confirm_removal = click.confirm(f"[WARNING] '{site}' has been found in file. Are you sure you want to delete this record?")
        if not confirm_removal:
            click.echo(f"[ABORT] Stopping record deletion...")
            return
        # Otherwise, continue with the command function
        click.echo(f"[INFO] Deleting record for '{site}'...")
    else:
        click.echo(f"[WARNING] '{site}' not found in file. Stopping command...")
        return

    # Delete key:value pair from the data
    del data[encrypted_site]

    # Save data to json
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo(f"[SUCCESS] Removed \'{site}\' from the file.")
