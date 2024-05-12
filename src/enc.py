from typing import Dict, Union, List
from .aes import encrypt, decrypt
import hashlib, hmac
import random

hash_function = hash_function = hashlib.sha256


def encode_msg(msg: str, key: int) -> Dict[str, Union[str, List[int]]]:
    return {
        "hash": hmac.new(str(key).encode(), msg.encode(), hash_function).hexdigest(),
        "message": list(encrypt(str(key).encode(), msg))
    }


def decode_msg(enc: Dict[str, Union[str, List[int]]], key: int) -> str:
    return decrypt(str(key).encode(), bytearray(enc["message"])).decode()


MY_KEY=None
G=9
P=2*255-19


def encode_key() -> Dict[str, int]:
    MY_KEY = random.randint(2, P - 1)
    encoded = pow(9, MY_KEY, P)
    return {
        "key": encoded,
    }


def decode_key(enc: Dict[str, int]) -> int:
    return pow(enc["key"], MY_KEY, P)