import tempfile
import os
import json
import click
from click.testing import CliRunner
from utils.encryption import encrypt
from utils.store_file import ensure_store_file, CONFIG_PATH
from cli.cli_store import cli

# COMMAND BEHAVIOR:
#   cli_store.py
# ------------------ #
# C1: 
# command with both options
# command without options; should fill in prompts
# command when file already has a website in it; prompt the user to change password and say yes
# command when file already has a website in it; prompt the user to change password and say no

TEMP_PATH = os.path.join(CONFIG_PATH, "jss", "temp.json")  # For test case


def test_store_both_options():
    runner = CliRunner()
    input_website = "TestingWebsite"
    input_password = "12345"

    result = runner.invoke(cli, ['--site', input_website, '--password', input_password, '--path', TEMP_PATH])
    assert result.exit_code == 0