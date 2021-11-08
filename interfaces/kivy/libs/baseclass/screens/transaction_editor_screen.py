from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from budget.models import Transaction


class TransactionEditorScreen(MDScreen):

    editor = ObjectProperty()

    def set_transaction(self, transaction: Transaction):
        print(f'editing {transaction.id}: {transaction.name}')
        self.editor.apply(transaction)

    def __draw_shadow__(self, origin, end, context=None):
        pass
