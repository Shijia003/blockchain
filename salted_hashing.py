import hashlib
import os

def my_hash(m):
    #Generate random nonce
    nonce = str(random.randint(0, 1_000_000_000))
    #Generate hex digest
    combined = nonce + m
    hash_object = hashlib.sha256(combined.encode())
    h_hex = hash_object.hexdigest() 
    return nonce, h_hex
