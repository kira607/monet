import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

from budget import Budget
from budget.models import Tables, Transaction

kivy.require('2.0.0')


class TransactionListItem(BoxLayout):
    def __init__(self, transaction: Transaction = None, **kwargs):
        self.transaction = transaction
        super(TransactionListItem, self).__init__(**kwargs)


class Root(BoxLayout):
    def __init__(self, budget, **kwargs):
        self.budget = budget
        super(Root, self).__init__(**kwargs)

    def show(self):
        data = self.budget.get(Tables.transactions)
        for d in data:
            self.transactions_list.add_widget(TransactionListItem(transaction=d))


class MainApp(MDApp):
    def __init__(self, budget_ref: Budget, **kwargs):
        self.budget = budget_ref
        super().__init__(**kwargs)

    def build(self):
        screen = Screen()
        return Root(self.budget)
