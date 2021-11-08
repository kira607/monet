import os
import sys
from pathlib import Path

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp

from budget import Budget
from budget.models import Transaction
from .libs.baseclass.root import Root  # noqa
from .libs.baseclass.screens.app_manager import AppManager
from .libs.baseclass.screens.main_screen import MainScreen  # noqa
from .libs.baseclass.screens.transaction_editor_screen import TransactionEditorScreen  # noqa
from .libs.baseclass.transaction_editor import TransactionEditor  # noqa

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
        print(f'loading {path} ...')
        return path

    @staticmethod
    def asset(asset_name: str):
        return os.path.join(os.environ['APP_ASSETS'], asset_name)


class MainApp(MDApp):
    def __init__(self, budget_ref: Budget, **kwargs):
        super().__init__(**kwargs)
        self.budget = budget_ref
        self.sm: AppManager = None

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
            self.budget.update(Transaction, transaction)

        self.sm.transition.direction = 'right'
        self.sm.current = 'main'
        # self.sm.current_screen.root.bottom_nav.children[1].current_screen.refresh()

    def delete_transaction(self, transaction):
        self.budget.delete(Transaction, transaction.transaction)
        self.sm.main.root.history_screen.transactions_list.remove(transaction)

    def build(self):
        self._load_kvs()
        self.sm = AppManager(self.budget)
        return self.sm

    def _load_kvs(self):
        Builder.load_file(path_to.kv('root.kv'))
        Builder.load_file(path_to.kv('accounts_list.kv'))
        Builder.load_file(path_to.kv('transactions_list.kv'))
        Builder.load_file(path_to.kv('transaction_editor_screen.kv'))
        Builder.load_file(path_to.kv('transaction_editor.kv'))
        Builder.load_file(path_to.kv('main_screen.kv'))
        Builder.load_file(path_to.kv('app_manager.kv'))
