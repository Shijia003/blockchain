import hashlib
import os
import random

def my_hash(m):
    #Generate random nonce
    if not isinstance(m, str):
        raise TypeError("Input must be a string")
    nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    #Generate hex digest
    combined = nonce + m
    hash_object = hashlib.sha256(combined.encode())
    h_hex = hash_object.hexdigest() 
    assert len(hash_hex) == 64
    return nonce, h_hex
