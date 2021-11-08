from kivy.properties import ObjectProperty

from budget.models import TransactionType, PlanType
from interfaces.kivy.libs.baseclass.custom_list import CustomList, CustomItem


class TransactionListItem(CustomItem):
    transaction = ObjectProperty()

    def __init__(self, transaction, **kwargs):
        super(TransactionListItem, self).__init__(**kwargs)
        self.transaction = transaction
        self.__apply()

    def __apply(self):
        self.text = self.transaction.name
        #self.secondary_theme_text_color = 'Custom'
        #self.secondary_text_color = (0, 100, 200, 100)
        self.secondary_text = str(self.transaction.value)
        self.tertiary_text = self.get_date()

    def get_value_color(self):
        color_map = {
            TransactionType.income: (0, 1, 0, 1),
            TransactionType.outcome: (1, 0, 0, 1),
            TransactionType.transfer: (0, 0, 0, 1),
        }
        return color_map.get(self.transaction.type, (0, 0, 0, 1))

    def get_date(self):
        prefix_map = {
            PlanType.year: 'Y',
            PlanType.month: 'M',
            PlanType.week: 'W',
            PlanType.day: 'D',
            PlanType.someday: 'N/A',
        }
        return (
            f'{prefix_map.get(self.transaction.plan_type, "?")}: '
            f'{str(self.transaction.plan_date)}'
        )

    def open_editor(self):
        print(f'taped on transaction with id: {self.transaction.id}')
        self.parent.open_editor(self.transaction)


class TransactionsList(CustomList):

    def clear(self):
        print(f'clearing {len(self.children)} list items...')
        print(f'children: {self.children}')
        while len(self.children) > 0:
            w = self.children.pop()
            self.remove_widget(w)
        print(f'cleared list items...')
        print(f'children [{len(self.children)}]: {self.children}')
        assert len(self.children) == 0

    def remove(self, item: TransactionListItem):
        self.remove_widget(item)

    def add(self, item: TransactionListItem):
        self.add_widget(item)
