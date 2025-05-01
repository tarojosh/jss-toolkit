import pytest
from click.testing import CliRunner
from cli.cli_encrypt import cli
from utils import encryption

# COMMAND BEHAVIOR:
#   cli_encrypt.py
# ------------------ #
# C1: Function should return encrypted text based on the input
# C2: Function does not continue if the user does not enter any input
# C3: If no text is provided on command call, prompt the user for one
# C4: Function can handle special character cases without throwing error


def test_encrypt_encrypted_plain_text():
    """
    Normal ASCII text (characters and numbers) as input should result in encryption as intended.
    Tests C1
    """
    runner = CliRunner()
    input = 'password123'

    result = runner.invoke(cli, ['--text', input])
    expected = encryption.encrypt(input)
    
    assert result.exit_code == 0
    assert "[SUCCESS] Encrypted: " in result.output
    assert expected in result.output


def test_encrypt_encrypted_special_chars():
    """
    It should be possible for special characters to also be encrypted without any errors. 
    Tests C1, C4
    IMPORTANT NOTE: 
        While this test does pass, the user themselves won't be able 
        to input certain special characters like the & symbol
        as that symbol is reserved and throws an error.
    """
    runner = CliRunner()
    input = '!@#$%^*()-=[]{};:",.<>/?~`'

    result = runner.invoke(cli, ['--text', input])
    expected = encryption.encrypt(input)
    
    assert result.exit_code == 0
    assert "[SUCCESS] Encrypted: " in result.output
    assert expected in result.output


def test_encrypt_no_input():
    """
    If the command is entered without any inputs, the command stops and informs the user that text is a needed input in order to function.
    Tests C2
    """
    runner = CliRunner()
    input = ''

    result = runner.invoke(cli, ['--text', input])
    expected = "[!] Please provide text to encrypt using --text or -t."
    
    assert result.exit_code == 0
    assert expected in result.output


def test_encrypt_prompt_user():
    """
    If the user types the command but doesn't enter the text they want encrypted, the command should prompt the user to give one.
    In this case, to avoid softlocking the test, `input=` is used to simulate a user typing in the command after having entered the command.
    Tests C3
    """
    runner = CliRunner()
    input = ''

    result = runner.invoke(cli, [], input="mypassword\n")
    expected = "[SUCCESS] Encrypted: "
    expected_password = encryption.encrypt(input)
    
    assert result.exit_code == 0
    assert expected in result.output
    assert expected_password in result.output