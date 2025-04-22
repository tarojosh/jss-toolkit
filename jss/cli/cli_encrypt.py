import click
import base64

@click.command()
@click.option('--text', '-t', help='Text to encrypt.')
def cli(text):
    """Encrypt a string using base64 encoding.
    
    Tip: Be sure to wrap your password in single or double quotes when running this command.
    """
    if not text:
        click.echo("[!] Please provide text to encrypt using --text or -t.")
        return

    encoded = base64.b64encode(text.encode()).decode()
    click.echo(f"[-] Encrypted: {encoded}")

if __name__ == '__main__':
    cli()
