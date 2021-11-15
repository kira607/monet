from kivy.properties import ObjectProperty

from ui.common import CustomList, CustomItem


class AccountListItem(CustomItem):

    account = ObjectProperty()

    def __init__(self, account, **kwargs):
        super(AccountListItem, self).__init__(**kwargs)
        self.account = account
        self.__apply()

    def __apply(self):
        self.text = self.account.name
        self.secondary_text = str(self.account.current_value)

    def on_release(self):
        print(f'taped on account with id: {self.account.id}')
        self.parent.open_editor(self.account)


class AccountsList(CustomList):

    def clear(self):
        for w in self.children:
            self.remove_widget(w)

    def add(self, item: AccountListItem):
        self.add_widget(item)

    def __draw_shadow__(self, origin, end, context=None):
        pass
