import pytest
from click.testing import CliRunner
from utils.store_file import ensure_store_file, TEMP_PATH, create_temp_file, remove_temp_file

# COMMAND BEHAVIOR:
#   util/encryption.py
# ------------------ #
# C1: Checks if the store file exists on the user directory. 
# C2: If the file doesn't exist on the user directory, create a new empty file.

def delete_mock_file():
    """Helper function to delete the mock file for testing purposes."""
    pass


def test_file_exists_true():
    pass


def test_file_exists_false():
    pass