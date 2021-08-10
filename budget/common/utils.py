import string
import random


def gen_id(prefix='', postfix='', length: int = 6):
    nid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return prefix + nid + postfix
