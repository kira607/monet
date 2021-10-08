import kivy
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.list import BaseListItem

from budget import Budget
from budget.models import Tables, Transaction

kivy.require('2.0.0')


class TransactionListItem(MDCard):
    def __init__(self, transaction: Transaction = None, **kwargs):
        self.transaction = transaction
        # print(self.name, '========================================================================================')
        # self.name.text = transaction.name
        super(TransactionListItem, self).__init__(**kwargs)
        print(self)


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
        self.root = Root(budget_ref)
        super().__init__(**kwargs)

    def on_start(self):
        self.budget.get(Transaction)
        return super().on_start()

    def build(self):
        return Root(self.budget)