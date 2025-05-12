import pytest
from click.testing import CliRunner
from cli.cli_decrypt import cli
from utils.encryption import encrypt

# COMMAND BEHAVIOR:
#   cli_decrypt.py
# ------------------ #
# C1: Command returns the decrypted text of an encrypted string input
# C2: If no text is provided, command informs the user to use the `-t` or `--text` option.
# C3: Function can handle special character cases without throwing error
# C4: Command displays any errors in decoding the text to the user.

def test_decrypt_text_input():
    """
    Command is given the encrypted text to be decrypted using `-t` or `--text` options.
    Tests: C1
    """
    runner = CliRunner()
    input = "HelloWorld"
    encrypted_input = encrypt(input)

    result = runner.invoke(cli, ['--text', encrypted_input])

    assert f"[SUCCESS] Decrypted: {input}" in result.output


def test_decrypt_no_input():
    """
    Command is given any option for encrypted text.
    Tests: C2
    """
    runner = CliRunner()

    result = runner.invoke(cli)

    assert f"[INFO] Please provide text to decrypt using --text or -t." in result.output


def test_decrypt_invalid_input():
    """
    Command is given an invalid input.
    Tests: C4
    """
    runner = CliRunner()
    input = "HelloWorld"

    result = runner.invoke(cli, ['--text', input])

    assert f"[ERROR] Unable to decode:" in result.output


def test_decrypt_special_characters():
    """
    Command is given encrypted text of special characters to be decrypted.
    Tests: C1, C3
    """
    runner = CliRunner()
    input = '!@#$%^*()-=[]{};:",.<>/?~`'
    encrypted_input = encrypt(input)

    result = runner.invoke(cli, ['--text', encrypted_input])

    assert f"[SUCCESS] Decrypted: {input}" in result.output