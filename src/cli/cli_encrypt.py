import click
from utils.encryption import encrypt

@click.command()
@click.option('--text', '-t', required=True, prompt='Password', help='Text to encrypt.')
def cli(text):
    """Encrypt a string using base64 encoding.
    
    Tip: Be sure to wrap your password in single or double quotes when running this command.
    """
    if not text:
        click.echo("[INFO] Please provide text to encrypt using --text or -t.")
        return

    encoded = encrypt(text)
    click.echo(f"[SUCCESS] Encrypted: {encoded}")


if __name__ == '__main__':
    cli()
