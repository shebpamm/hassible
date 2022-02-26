import secrets
import sys
from hashlib import scrypt


def hash_pw(password, hex_salt=secrets.token_hex(8)):

    hashed_pw = scrypt(password, n=16384, r=8, p=1, salt=hex_salt.encode())
    hex_hash = "".join("{:02x}".format(x) for x in hashed_pw)

    return f"{hex_salt}:{hex_hash}"


if __name__ == "__main__":
    hash = hash_pw(sys.argv[1].encode())
    print(hash, end="")
