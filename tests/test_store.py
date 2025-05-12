from click.testing import CliRunner
from utils.store_file import TEMP_PATH, create_temp_file, remove_temp_file
from cli.cli_store import cli

# COMMAND BEHAVIOR:
#   cli_store.py
# ------------------ #
# C1: Given a website and password, command should store the information in encrypted format in the storage file.
# C2: Command should prompt the user for website and password information if none are provided.
# C3: Command should prompt the user to update the password if the website already exists.


def test_store_both_options():
    """
    Command should store the website and password in the store file when given the options.
    Tests C1
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    result = runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH])

    assert f"[INFO] '{input_website}' not found in file. Creating new key..." in result.output
    assert f"[SUCCESS] Stored password for {input_website}." in result.output
    remove_temp_file()


def test_store_with_prompts():
    """
    Command should prompt the user for the website and password when no options are filled in.
    Tests C2
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"
    input_whole = f"{input_website}\n{input_password}\n"

    result = runner.invoke(cli, ['--path', TEMP_PATH], input=input_whole)

    assert f"[INFO] '{input_website}' not found in file. Creating new key..." in result.output
    assert f"[SUCCESS] Stored password for {input_website}." in result.output
    remove_temp_file()


def test_store_existing_website_continue():
    """
    User confirms the prompt to update the password of an existing website in the store file.
    Tests C3
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH])
    result = runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH], input="y\n")

    assert f"[WARNING] '{input_website}' is already stored in file. Do you want to update the password?" in result.output
    assert "[WARNING] Updating password for" in result.output
    assert f"[SUCCESS] Stored password for {input_website}." in result.output
    remove_temp_file()


def test_store_existing_website_cancel():
    """
    User denies the prompt to update the password of an existing website in the store file.
    Tests C3
    """
    create_temp_file()
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH])
    result = runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH], input="n\n")

    assert f"[WARNING] '{input_website}' is already stored in file. Do you want to update the password?" in result.output
    assert "[ABORT] Canceling password update..." in result.output
    remove_temp_file()