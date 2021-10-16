from kivy.properties import ObjectProperty

from interfaces.kivy.libs.baseclass.custom_list import CustomList, CustomItem


class AccountListItem(CustomItem):
    name = ObjectProperty()
    value = ObjectProperty()

    account = ObjectProperty()

    def refresh_view_attrs(self, rv, i, d):
        self.__apply(d['account'])

    def __apply(self, account):
        self.name.text = f'{account.name} ({account.currency})'
        self.value.text = f'{account.current_value}'


class AccountsList(CustomList):
    pass
