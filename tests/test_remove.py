import json
from click.testing import CliRunner
from utils.store_file import TEMP_PATH, create_temp_file, remove_temp_file
from utils.encryption import encrypt
from cli.cli_remove import cli

# COMMAND BEHAVIOR:
#   cli_remove.py
# ------------------ #
# C1: Command makes sure that the store file exists on the user directory.
# C2: Command will prompt the user for confirmation on removing an existing website if it exists.
# C3: Command will remove the website and password record from the store file.
# C4: Command will prompt the user for the name of the website if none was given.


def test_remove_existing_website_confirm_prompt():
    """
    Command is given the option of the website name when invoked to remove a website from the store file.
    Tests: C1, C2, C3
    """
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    # Test setup
    create_temp_file()
    with open(TEMP_PATH, 'r') as f:
        data = json.load(f)

    encrypted_password = encrypt(input_password)
    encrypted_site = encrypt(input_website)
    data[encrypted_site] = encrypted_password

    # Save data to json
    with open(TEMP_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    result = runner.invoke(cli, ['--site', input_website, '--path', TEMP_PATH], input="y\n")

    assert f"[INFO] Deleting record for '{input_website}'..." in result.output
    assert f"[SUCCESS] Removed '{input_website}' from the file." in result.output
    remove_temp_file()


def test_remove_existing_website_cancel_prompt():
    """
    Command prompts the user for the website name that is to be removed.
    Tests: C1, C2
    """
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    # Test setup
    create_temp_file()
    with open(TEMP_PATH, 'r') as f:
        data = json.load(f)

    encrypted_password = encrypt(input_password)
    encrypted_site = encrypt(input_website)
    data[encrypted_site] = encrypted_password

    # Save data to json
    with open(TEMP_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    result = runner.invoke(cli, ['--site', input_website, '--path', TEMP_PATH], input="n\n")

    assert f"[WARNING] '{input_website}' has been found in file. Are you sure you want to delete this record?" in result.output
    assert f"[ABORT] Stopping record deletion..." in result.output
    remove_temp_file()


def test_remove_nonexisting_website_given_option():
    """
    Command is given a website that is not found in the store file.
    Tests: C1
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "NonexistingWebsite"
    
    result = runner.invoke(cli, ['--site', input_website, '--path', TEMP_PATH])

    assert f"[WARNING] '{input_website}' not found in file. Stopping command..." in result.output
    remove_temp_file()


def test_remove_nonexisting_website_promopted():
    """
    Command prompts the user for a website, and the input is not found in the store file.
    Tests: C1, C4
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "NonexistingWebsite"
    
    result = runner.invoke(cli, ['--path', TEMP_PATH], input=f"{input_website}\n")

    assert f"[WARNING] '{input_website}' not found in file. Stopping command..." in result.output
    remove_temp_file()