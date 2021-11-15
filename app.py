import os
import sys
from pathlib import Path

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp

from db import DbClient
from ui.main import MainScreen  # noqa
from ui import ScreensManager
from ui.transaction_editor import TransactionEditorScreen  # noqa

kivy.require('2.0.0')

app_root = 'APP_ROOT'
if getattr(sys, 'frozen', False):  # bundle mode with PyInstaller
    os.environ['APP_ROOT'] = sys._MEIPASS  # ???
else:
    # sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ['APP_ROOT'] = str(Path(__file__).parent)
    # os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ['APP_ASSETS'] = os.path.join(os.environ['APP_ROOT'], f'assets{os.sep}')


class PathTo:
    @staticmethod
    def kv(file_name: str):
        path = os.path.join(os.environ['APP_ROOT'], 'ui', 'kv', file_name)
        print(f'loading {path} ...')
        return path

    @staticmethod
    def asset(asset_name: str):
        return os.path.join(os.environ['APP_ASSETS'], asset_name)


class MainApp(MDApp):
    def __init__(self, db_client: DbClient, **kwargs):
        super().__init__(**kwargs)
        self.db = db_client
        self.sm: ScreensManager = None

    def open_editor(self, transaction):
        print('opening editor...')
        self.sm.transition.direction = 'left'
        self.sm.current = 'transaction editor'
        self.sm.current_screen.set_transaction(transaction)

    def close_editor(self, save=False):
        print('closing editor...')

        if save:
            print('saving...')
            transaction = self.sm.current_screen.editor.get_transaction()
            self.sm.current_screen.editor.reset()
            self.db.update(transaction)

        self.sm.transition.direction = 'right'
        self.sm.current = 'main'

    def pick_from(self):
        self.sm.transaction_editor.editor.pick_from()

    def delete_transaction(self, transaction):
        self.db.delete(transaction.transaction)
        self.sm.main.root.history_screen.transactions_list.remove(transaction)

    def build(self):
        self._load_kvs()
        self.sm = ScreensManager()
        return self.sm

    def _load_kvs(self):
        Builder.load_file(PathTo.kv('accounts_list.kv'))
        Builder.load_file(PathTo.kv('main_screen.kv'))
        Builder.load_file(PathTo.kv('screens_manager.kv'))
        Builder.load_file(PathTo.kv('tabs.kv'))
        Builder.load_file(PathTo.kv('transaction_editor_screen.kv'))
        Builder.load_file(PathTo.kv('transaction_editor.kv'))
        Builder.load_file(PathTo.kv('transactions_list.kv'))
