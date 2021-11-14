import os
import random
import string
import sys
from pathlib import Path

app_root = 'APP_ROOT'
if getattr(sys, 'frozen', False):  # bundle mode with PyInstaller
    os.environ['APP_ROOT'] = sys._MEIPASS  # ???
else:
    # sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ['APP_ROOT'] = str(Path(__file__).parent)
    # os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ['APP_ASSETS'] = os.path.join(os.environ['APP_ROOT'], f'assets{os.sep}')


class path_to:
    @staticmethod
    def kv(file_name: str):
        path = os.path.join(os.environ['APP_ROOT'], '..', '..', 'libs', 'kv', file_name)
        print(f'getting {path}')
        return path

    @staticmethod
    def asset(asset_name: str):
        return os.path.join(os.environ['APP_ASSETS'], asset_name)



def gen_id(length: int = 6) -> str:
    '''
    Generate id

    :param int length: length of the id
    :return: id - random string of length ``length`` with symbols within [a-zA-Z0-9]
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
