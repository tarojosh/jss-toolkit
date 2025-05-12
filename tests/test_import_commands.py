from cli import cli_decrypt, cli_encrypt, cli_get, cli_password, cli_remove, cli_store
from utils import encryption, store_file

# The purpose of this test and script is so that running `pytest --cov=src. --cov-report=term-missing` 
# will accurately cover all code that is being tested to ensure an accurate report of code coverage.

def test_all_code():
    assert encryption
    # assert store_file
    assert cli_decrypt
    assert cli_encrypt
    assert cli_get
    assert cli_password
    assert cli_remove
    assert cli_store