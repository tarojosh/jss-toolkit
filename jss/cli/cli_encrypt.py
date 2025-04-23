import click
import base64

banned_characters = ['\'', '\"', '~', '&']

@click.command()
@click.option('--text', '-t', help='Text to encrypt.')
def cli(text):
    """Encrypt a string using base64 encoding.
    
    Tip: Be sure to wrap your password in single or double quotes when running this command.
    """
    if not text:
        click.echo("[!] Please provide text to encrypt using --text or -t.")
        return
    
    # # TODO: Add checks to the text to see if it contains invalid special characters (' " ~ &), and warn the user
    # for illegal_char in banned_characters:
    #     if illegal_char in text:
    #         click.echo(f"[!] WARNING: An illegal character {illegal_char} was found in {text} that won't work.")
    #         return

    encoded = base64.b64encode(text.encode()).decode()
    click.echo(f"[-] Encrypted: {encoded}")

if __name__ == '__main__':
    cli()
