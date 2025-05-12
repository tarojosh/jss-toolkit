import json
from click.testing import CliRunner
from utils.store_file import TEMP_PATH, create_temp_file, remove_temp_file
from utils.encryption import encrypt
from cli.cli_get import cli

# COMMAND BEHAVIOR:
#   cli_get.py
# ------------------ #
# C1: Command makes sure that the store file exists on the user directory.
# C2: Command will return the password on the input of the associated website name.
# C3: Command will prompt the user for the name of the website if no optional input is given.
# C4: Command will display a list of all website names if the --all flag is given.


def test_get_website_provided():
    """
    Command returns the decrypted password when given the associated website name.
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
    
    result = runner.invoke(cli, ['--site', input_website, '--path', TEMP_PATH])

    assert f"[RESULT] The password for {input_website} is:\t{input_password}" in result.output
    remove_temp_file()


def test_get_website_prompted():
    """
    Command returns the decrypted password when the user is prompted for website name.
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
    
    result = runner.invoke(cli, ['--path', TEMP_PATH], input=f"{input_website}\n")

    assert f"[RESULT] The password for {input_website} is:\t{input_password}" in result.output
    remove_temp_file()


def test_get_website_none_found():
    """
    Command informs the user that no password was found for a website not stored within the store file.
    Tests: C1
    """
    runner = CliRunner()
    create_temp_file()
    input_website = "ERR_404_NOT_FOUND"
    
    result = runner.invoke(cli, ['--path', TEMP_PATH], input=f"{input_website}\n")

    assert f"[WARNING] No password was found for {input_website}." in result.output
    remove_temp_file()


def test_get_website_listings():
    """
    Command prints a list of website names that are stored on the file.
    Tests: C1, C4
    """
    runner = CliRunner()
    _websites = ["HelloWorld", "HiThere", "Howdy"]
    _passwords = ["Goodbye", "See ya", "So long, pardner"]

    # Test setup
    create_temp_file()
    with open(TEMP_PATH, 'r') as f:
        data = json.load(f)

    for i in range(len(_websites)):
        encrypted_password = encrypt(_passwords[i])
        encrypted_site = encrypt(_websites[i])
        data[encrypted_site] = encrypted_password

    # Save data to json
    with open(TEMP_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    result = runner.invoke(cli, ['--all', '--path', TEMP_PATH])

    assert "[RESULT] 3 stored password(s) were found:" in result.output
    remove_temp_file()


def test_get_website_no_listings():
    """
    Command will inform the user that the store file is empty and there are no websites available.
    Tests: C1
    """
    runner = CliRunner()

    # Test setup
    create_temp_file()
    with open(TEMP_PATH, 'r') as f:
        data = json.load(f)

    # Save data to json
    with open(TEMP_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    result = runner.invoke(cli, ['--all', '--path', TEMP_PATH])

    assert "[WARNING] No website passwords are stored in file." in result.output
    remove_temp_file()