import click
import base64

@click.command()
@click.option('--text', '-t', help='Text to decrypt.')
def cli(text):
    """Decrypt a base64-encoded string.
    
    Tip: Be sure to wrap your password in single or double quotes when running this command.
    """
    if not text:
        click.echo("[!] Please provide text to decrypt using --text or -t.")
        return
    
    try:
        decoded = base64.b64decode(text.encode()).decode()
        click.echo(f"Decrypted: {decoded}")
    except Exception as e:
        click.echo(f"Error decoding: {e}")


if __name__ == '__main__':
    cli()
