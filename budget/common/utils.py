import random
import string


def gen_id(length: int = 6) -> str:
    '''
    Generate id

    :param int length: length of the id
    :return: id - random string of length ``length`` with symbols within [a-zA-Z0-9]
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
