import click
from utils.encryption import decrypt


@click.command()
@click.option('--text', '-t', help='Text to decrypt.')
def cli(text):
    """Decrypt a base64-encoded string.
    
    Tip: Be sure to wrap your password in single or double quotes when running this command.
    """
    if not text:
        click.echo("[INFO] Please provide text to decrypt using --text or -t.")
        return
    
    try:
        decoded = decrypt(text)
        click.echo(f"[SUCCESS] Decrypted: {decoded}")
    except Exception as e:
        click.echo(f"[ERROR] Unable to decode: {e}")


if __name__ == '__main__':
    cli()
