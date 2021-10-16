from kivy.properties import ObjectProperty

from budget.models import TransactionType, PlanType
from interfaces.kivy.libs.baseclass.custom_list import CustomList, CustomItem


class TransactionListItem(CustomItem):
    name = ObjectProperty()
    comment = ObjectProperty()
    planned = ObjectProperty()
    from_ = ObjectProperty()
    value = ObjectProperty()
    planned_value = ObjectProperty()
    to = ObjectProperty()
    plan_date = ObjectProperty()
    pay_date = ObjectProperty()
    tag = ObjectProperty()

    transaction = ObjectProperty()

    def refresh_view_attrs(self, rv, i, d):
        self.__apply(d['transaction'])

    def __apply(self, transaction):
        self.name.text = self.__get_text(transaction.name)
        self.from_.text = self.__get_text(transaction.from_)
        self.to.text = self.__get_text(transaction.to)
        self.value.text = self.__get_text(transaction.value)
        self.__set_value_color(transaction)
        self.pay_date.text = self.__get_text(transaction.pay_date)
        self.__set_plan_date(transaction)
        self.planned_value.text = self.__get_text(transaction.planned_value)
        self.planned.text = self.__get_text(transaction.planned)
        self.comment.text = self.__get_text(transaction.comment)
        self.tag.text = self.__get_text(transaction.tag)

    def __get_text(self, source):
        txt = str(source)
        return txt if source is not None else '-'

    def __set_value_color(self, transaction):
        color_map = {
            TransactionType.income: (0, 1, 0, 1),
            TransactionType.outcome: (1, 0, 0, 1),
            TransactionType.transfer: (0, 0, 0, 1),
        }
        self.value.text_color = color_map.get(transaction.type, (0, 0, 0, 1))

    def __set_plan_date(self, transaction):
        prefix_map = {
            PlanType.year: 'Y',
            PlanType.month: 'M',
            PlanType.week: 'W',
            PlanType.day: 'D',
            PlanType.someday: 'N/A',
        }
        self.plan_date.text = (
            f'{prefix_map.get(transaction.plan_type, "?")}: '
            f'{self.__get_text(transaction.plan_date)}'
        )

    def on_swipe_left(self):
        print('Swipe left!')


class TransactionsList(CustomList):
    pass
