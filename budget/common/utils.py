import random
import string


def gen_id(prefix: str = '', length: int = 6) -> str:
    '''
    Generate id

    :param str prefix: prefix of the id
    :param int length: length of the id
    :return: id in format prefix + random string of length length with symbols within [a-zA-Z0-9]
    '''
    nid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return f'{prefix}-{nid}' if prefix else nid
