import pytest
from click.testing import CliRunner
from utils.encryption import encrypt, decrypt

import string
import random

# COMMAND BEHAVIOR:
#   util/encryption.py
# ------------------ #
# C1: `encrypt()` should return encrypted text of the input
# C2: `decrypt()` should return decrypted text of the input
# C3: If the text is empty, the function should return nothing
# C4: Text that has been encoded and decoded should be unchanged
# C5: Function should be able to handle special characters and unicode

# Test encryption C1
def test_encryption_encrypt():
    """
    The output of `encrypt()` should be encrypted text of the input
    Tests C1
    """
    input = 'password123'
    expected = 'cGFzc3dvcmQxMjM='
    result = encrypt(input)
    
    assert expected == result


# Test decryption C2
def test_encryption_decrypt():
    """
    The output of `decrypt()` should be normal text of the encrypted input
    Tests C2
    """
    input = 'cGFzc3dvcmQxMjM='
    expected = 'password123'
    result = decrypt(input)
    
    assert expected == result


# Test no input C3
def test_encryption_encrypt_no_input():
    """
    If no input is given to `encrypt()`, the output should be an empty string
    Tests C3
    """
    input = ''
    expected = ''
    result_encryption = encrypt(input)
    result_decryption = decrypt(input)
    
    assert expected == result_encryption
    assert expected == result_decryption

# Test encryption --> decryption C4, C1, C2
def test_encryption_roundtrip():
    """
    The original input should be unchanged after being put through encryption and decryption
    Tests C4, C1, C2
    """
    input = 'password123'
    expected = 'password123'
    result = decrypt(encrypt(input))
    
    assert expected == result


# Test special characters C5, C1, C2, C4
def test_encryption_special_chars_encrypt():
    """
    Given special characters, the `encrypt()` should return the encrypted text without any error
    Tests C5, C1, C2, C4
    """
    input = '!@#$%^&*()_+-={}[]:";<>?,./`~'
    expected = 'IUAjJCVeJiooKV8rLT17fVtdOiI7PD4/LC4vYH4='
    result = encrypt(input)
    
    assert expected == result


def test_encryption_special_chars_decrypt():
    """
    Given encrypted text, the `decrypt()` should return the decrypted text containing special characters without any error
    Tests C5, C1, C2, C4
    """
    input = 'IUAjJCVeJiooKV8rLT17fVtdOiI7PD4/LC4vYH4='
    expected = '!@#$%^&*()_+-={}[]:";<>?,./`~'
    result = decrypt(input)
    
    assert expected == result

# --------------------------------- #
# AUTOMATED TEST / FUZZER
# --------------------------------- #

def test_encryption_roundtrip_fuzzer():
    """
    Fuzzer test for roundtrip; the input should be unchanged after being encrypted and decrypted
    Tests C4, C1, C2
    """
    for i in range(0, 5000):
        rand_size = random.randint(1, 500)
        rand_password = _generate_password(rand_size)
        input = rand_password
        expected = rand_password

        result = decrypt(encrypt(input))
        assert expected == result


def _generate_password(max_length: int) -> str:
    all_characters: str = (string.ascii_letters + string.digits + string.punctuation)
    password = ''.join(random.choices(all_characters, k=max_length))
    return(password)