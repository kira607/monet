from kivy.properties import ObjectProperty

from budget.models import Tables
from interfaces.kivy.libs.baseclass.accounts_list import AccountListItem, AccountsList
from interfaces.kivy.libs.baseclass.base_screen import BaseScreen


class ScreenAccounts(BaseScreen):

    accounts_list: AccountsList = ObjectProperty()

    def reload(self):
        print('reload accounts screen')
        self.accounts_list.clear()
        db_list = self.budget.get(Tables.accounts)
        for a in db_list:
            self.accounts_list.add(AccountListItem(a))
