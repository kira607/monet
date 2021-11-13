from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout

from libs.baseclass.screens.screen_accounts import ScreenAccounts
from libs.baseclass.screens.screen_analysis import ScreenAnalysis
from libs.baseclass.screens.screen_history import ScreenHistory
from libs.baseclass.screens.screen_home import ScreenHome
from libs.baseclass.screens.screen_plans import ScreenPlans


class Root(MDBoxLayout):
    '''The main layout. Contains all app widgets'''

    # screens
    plans_screen: ScreenPlans = ObjectProperty()
    history_screen: ScreenHistory = ObjectProperty()
    home_screen: ScreenHome = ObjectProperty()
    analysis_screen: ScreenAnalysis = ObjectProperty()
    accounts_screen: ScreenAccounts = ObjectProperty()

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.budget = None

    def set_budget(self, budget):
        self.budget = budget
        self.plans_screen.init(self.budget)
        self.history_screen.init(self.budget)
        self.home_screen.init(self.budget)
        self.analysis_screen.init(self.budget)
        self.accounts_screen.init(self.budget)
