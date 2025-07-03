import hashlib
import os
import random

def my_hash(m):
    #Generate random nonce
    nonce = str(random.randint(0, 100000000))
    #Generate hex digest
    combined = nonce + m
    hash_object = hashlib.sha256(combined.encode())
    h_hex = hash_object.hexdigest() 
    assert len(h_hex) == 64
    return nonce, h_hex
