from kivy.properties import ObjectProperty

from db.models import Account
from libs.baseclass.accounts_list import AccountListItem, AccountsList
from libs.baseclass.base_screen import BaseScreen


class ScreenAccounts(BaseScreen):

    accounts_list: AccountsList = ObjectProperty()

    def reload(self):
        print('reload accounts screen')
        self.accounts_list.clear()
        db_list = self.budget.get(Account)
        for a in db_list:
            self.accounts_list.add(AccountListItem(a))
