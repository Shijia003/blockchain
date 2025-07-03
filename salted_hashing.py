import hashlib
import os

def myhash(m):
    #Generate random nonce
    nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    #Generate hex digest
    combined = s + nonce
    hash_object = hashlib.sha256(combined.encode())
    h_hex = hash_object.hexdigest() 
    return nonce, h_hex