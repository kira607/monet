from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout

from budget.models import Tables


class Root(MDBoxLayout):
    '''The main layout. Contains all app widgets'''

    transactions_list = ObjectProperty()
    accounts_list = ObjectProperty()

    def __init__(self, budget, **kwargs):
        self.budget = budget
        print(self.ids)
        super(Root, self).__init__(**kwargs)

    def update_list(self):
        transactions_list = self.budget.get(Tables.transactions)
        self.transactions_list.data = [{'transaction': t} for t in transactions_list]

    def update_accounts(self):
        accounts_list = self.budget.get(Tables.accounts)
        print(accounts_list)
        self.accounts_list.data = [{'account': a} for a in accounts_list]

    def __draw_shadow__(self, origin, end, context=None):
        pass