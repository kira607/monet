import string
import random


def gen_id(prefix='', postfix=''):
    nid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return prefix + nid + postfix
