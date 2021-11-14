from kivy.properties import ObjectProperty

from db.models import Transaction
from ui.common import BaseScreen
from .transactions_list import TransactionListItem, TransactionsList


class ScreenHistory(BaseScreen):

    count = 0

    transactions_list: TransactionsList = ObjectProperty()

    def on_enter(self):
        self.reload()

    def reload(self):
        print('reload history screen')
        self.transactions_list.clear()
        db_list = self.budget.get(Transaction)
        if self.count < 3 or self.count > 5:
            for t in db_list:
                self.transactions_list.add(TransactionListItem(t))
        self.count += 1
