import click
import random as rand
import string as characters


# Generate Password ----------------------------------------@
@click.command(name='create-password')
@click.option('-s', '--size', default=12, help='The size of the password within valid range of 1-90. (Default: 12)')
def cli(size):
    """Generates a random string of ASCII characters."""
    # if size < 1 or size > 90:
    #     click.echo("[INFO] Input size is not within valid range (1-90).")
    #     return

    password: str = _generate_password(size)
    click.echo(f"[RESULT] Your password of length {size} is:\t{password}\nBe sure to store this in a secure location.")


def _generate_password(max_length: int) -> str:
    """Helper function to create a random string of characters to be used as a password. Invoked by the generate_password command."""
    all_characters: str = (characters.ascii_letters + characters.digits + characters.punctuation)

    # Remove these characters as they can conflict with the encrypt/decrypt command
    all_characters = all_characters.replace('\'', '')
    all_characters = all_characters.replace('\"', '')
    all_characters = all_characters.replace('~', '')
    all_characters = all_characters.replace('&', '')
    
    max_length = max(0, min(max_length, 94))  # Clamp value
    password = ''.join(rand.choices(all_characters, k=max_length))
    return(password)
