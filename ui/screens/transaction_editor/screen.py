from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from .editor import TransactionEditor

from db.models import Transaction


class TransactionEditorScreen(MDScreen):

    editor: TransactionEditor = ObjectProperty()

    def set_transaction(self, transaction: Transaction):
        print(f'editing {transaction.id}: {transaction.name}')
        self.editor.apply(transaction)
