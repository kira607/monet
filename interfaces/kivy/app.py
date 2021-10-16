import os
import sys
from pathlib import Path

import kivy
from kivymd.app import MDApp
from kivy.lang import Builder

from budget import Budget

from .libs.baseclass.root import Root


kivy.require('2.0.0')


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
        path = os.path.join(os.environ['APP_ROOT'], 'libs', 'kv', file_name)
        print(f'getting {path}')
        return path

    @staticmethod
    def asset(asset_name: str):
        return os.path.join(os.environ['APP_ASSETS'], asset_name)


class MainApp(MDApp):
    def __init__(self, budget_ref: Budget, **kwargs):
        self.budget = budget_ref
        super().__init__(**kwargs)

    def on_start(self):
        self.root.update_list()
        self.root.update_accounts()

    def build(self):
        Builder.load_file(path_to.kv('root.kv'))
        Builder.load_file(path_to.kv('accounts_list.kv'))
        Builder.load_file(path_to.kv('transactions_list.kv'))
        Builder.load_file(path_to.kv('custom_list.kv'))
        return Root(self.budget)
