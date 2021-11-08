from threading import Thread

from kivy.properties import ObjectProperty

from budget.models import Tables
from interfaces.kivy.libs.baseclass.base_screen import BaseScreen
from interfaces.kivy.libs.baseclass.transactions_list import TransactionListItem, TransactionsList


class ScreenHistory(BaseScreen):

    count = 0

    transactions_list: TransactionsList = ObjectProperty()

    def on_enter(self):
        self.reload()

    def reload(self):
        print('reload history screen')
        self.transactions_list.clear()
        db_list = self.budget.get(Tables.transactions)
        if self.count < 3 or self.count > 5:
            for t in db_list:
                self.transactions_list.add(TransactionListItem(t))
        self.count += 1
