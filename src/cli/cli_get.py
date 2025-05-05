import click
import os
import json
from pathlib import Path
from utils.encryption import decrypt, encrypt

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


@click.command()
@click.option('--all', '-a', 'show_all', is_flag=True, help='Display all stored websites.')
@click.option('--site', '-s', help='The website you are trying to get the password of.')
def cli(site, show_all):
    """Retrieve password from user directory."""
    ensure_store_file()

    # Load current data from the store.json
    with open(STORE_PATH, 'r') as f:
        data = json.load(f)
    
    if show_all:
        _display_all_websites(data)
    else:
        # Make sure to get a website name from the user
        if not site:
            site = click.prompt("Website name")
        _get_website_record(data, site)


def _get_website_record(data, site):
    encrypted_site = encrypt(site)
    encrypted_password = data.get(encrypted_site)

    if encrypted_password is None:
        click.echo(f"[WARNING] No password was found for {site}.")
    else:
        decrypted_password = decrypt(encrypted_password)
        click.echo(f"[RESULT] The password for {site} is:\t{decrypted_password}")
    return


def _display_all_websites(data):
    websites = data.keys()
    if len(websites) == 0:
        click.echo(f"[WARNING] No website passwords are stored in file.")
        return

    click.echo(f"[RESULT] {len(websites)} stored password(s) were found:")
    for _s in websites:
        click.echo(decrypt(_s))
    return


if __name__ == '__main__':
    cli()
