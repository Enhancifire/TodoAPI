import os
import hashlib

def hash(password):
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
            )


    return (key, salt)

def dehash(key, salt, password):
    new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
            )

    new_key = str(new_key)
    if key == new_key:
        return True

    else:
        return False
