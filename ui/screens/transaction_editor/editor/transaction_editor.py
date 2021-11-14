from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem

from db.models import Transaction, Account
from db import get_db



class AccountPickerItem(OneLineAvatarListItem):
    divider=None
    account=None


class AccountPicker:
    def __init__(self):
        self.db = get_db()
        self.dialog = None

    def pick_from(self):
        if self.dialog is None: 
            self.create_dialog()
        self.dialog.open()

    def create_dialog(self):
        items = []
        accs = self.db.get(Account)
        for acc in accs:
            new_item = AccountPickerItem(text=acc.name)
            new_item.account = acc
            items.append(new_item)
        self.dialog = MDDialog(
            title='Pick Account',
            type='simple',
            items=items,
        )


class TransactionEditor(MDBoxLayout):

    name_input = ObjectProperty()
    from_button = ObjectProperty()

    transaction = None
    account_picker = AccountPicker()

    def pick_from(self):
        self.account_picker.pick_from()

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
