from kivy.properties import ObjectProperty

from db.models import Transaction
from ui.common import BaseTab
from .transactions_list import TransactionListItem, TransactionsList


class HistoryTab(BaseTab):

    transactions_list: TransactionsList = ObjectProperty()

    def on_enter(self):
        self.reload()

    def reload(self):
        print('reload history screen')
        self.transactions_list.clear()
        db_list = self.db.get(Transaction)
        for t in db_list:
            self.transactions_list.add(TransactionListItem(t))
