import os
import sys
from pathlib import Path

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp

from db import DbClient
from ui.screens.main.bottom_nav import BottomNav  # noqa
from ui.screens.app_manager import AppManager
from ui.screens import MainScreen  # noqa
from ui.screens import TransactionEditorScreen  # noqa
from ui.screens.transaction_editor.editor.transaction_editor import TransactionEditor  # noqa

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
        self.am: AppManager = None

    def open_editor(self, transaction):
        print('opening editor...')
        self.am.transition.direction = 'left'
        self.am.current = 'transaction editor'
        self.am.current_screen.set_transaction(transaction)

    def close_editor(self, save=False):
        print('closing editor...')

        if save:
            print('saving...')
            transaction = self.am.current_screen.editor.get_transaction()
            self.am.current_screen.editor.reset()
            self.db.update(transaction)

        self.am.transition.direction = 'right'
        self.am.current = 'main'

    def pick_from(self):
        self.am.transaction_editor.editor.pick_from()

    def delete_transaction(self, transaction):
        self.db.delete(transaction.transaction)
        self.am.main.root.history_screen.transactions_list.remove(transaction)

    def build(self):
        self._load_kvs()
        self.am = AppManager(self.db)
        return self.am

    def _load_kvs(self):
        Builder.load_file(PathTo.kv('main_screen.kv'))
        Builder.load_file(PathTo.kv('accounts_list.kv'))
        Builder.load_file(PathTo.kv('transactions_list.kv'))
        Builder.load_file(PathTo.kv('transaction_editor_screen.kv'))
        Builder.load_file(PathTo.kv('transaction_editor.kv'))
        Builder.load_file(PathTo.kv('main_screen.kv'))
        Builder.load_file(PathTo.kv('app_manager.kv'))
