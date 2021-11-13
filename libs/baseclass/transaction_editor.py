from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout

from db.models import Transaction


class TransactionEditor(MDBoxLayout):

    name_input = ObjectProperty()
    transaction = None

    def reset(self):
        self.transaction = None
        self.name_input.text = ''

    def apply(self, transaction: Transaction):
        self.transaction = transaction
        self.name_input.text = transaction.name

    def get_transaction(self):
        if self.transaction:
            self.transaction.name = self.name_input.text
            return self.transaction

        return Transaction(
            name=self.name_input.text,
        )
