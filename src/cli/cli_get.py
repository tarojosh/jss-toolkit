import click
import json
from utils.encryption import decrypt, encrypt
from utils.store_file import ensure_store_file, STORE_PATH


@click.command()
@click.option('--all', '-a', 'show_all', is_flag=True, help='Display all stored websites.')
@click.option('--site', '-s', help='The website you are trying to get the password of.')
@click.option('--path', hidden=True, default=STORE_PATH, help='Path of the file that will store the info. FOR TESTING ONLY.')
def cli(site, show_all, path):
    """Retrieve password from user directory."""
    ensure_store_file(path)

    # Load current data from the store.json
    with open(path, 'r') as f:
        data = json.load(f)
    
    if show_all:
        _display_all_websites(data)
    else:
        # Make sure to get a website name from the user
        if not site:
            site = click.prompt("Website name")
        _get_website_record(data, site)


def _get_website_record(data, site):
    """Return the password of the given website name."""
    encrypted_site = encrypt(site)
    encrypted_password = data.get(encrypted_site)

    if encrypted_password is None:
        click.echo(f"[WARNING] No password was found for {site}.")
    else:
        decrypted_password = decrypt(encrypted_password)
        click.echo(f"[RESULT] The password for {site} is:\t{decrypted_password}")
    return


def _display_all_websites(data):
    """Display all website names found on the file."""
    websites = data.keys()
    if len(websites) == 0:
        click.echo(f"[WARNING] No website passwords are stored in file.")
        return

    click.echo(f"[RESULT] {len(websites)} stored password(s) were found:")
    for _s in websites:
        click.echo(f"\t{decrypt(_s)}")
    return
