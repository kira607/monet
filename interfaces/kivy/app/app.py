import kivy
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from budget import Budget
from budget.models import Tables, TransactionType, PlanType

kivy.require('2.0.0')


class TransactionListItem(RecycleDataViewBehavior, BoxLayout):
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


class Root(MDBoxLayout):
    '''The main layout. Contains all app widgets'''
    transactions_list = ObjectProperty()

    def __init__(self, budget, **kwargs):
        self.budget = budget
        print(self.ids)
        super(Root, self).__init__(**kwargs)

    def update_list(self):
        transactions_list = self.budget.get(Tables.transactions)
        self.transactions_list.data = [{'transaction': t} for t in transactions_list]


class MainApp(MDApp):
    def __init__(self, budget_ref: Budget, **kwargs):
        self.budget = budget_ref
        super().__init__(**kwargs)

    def on_start(self):
        self.root.update_list()

    def build(self):
        return Root(self.budget)
