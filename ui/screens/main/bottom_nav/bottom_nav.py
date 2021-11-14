from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout

from ui.screens.main.bottom_nav.accounts import ScreenAccounts
from ui.screens.main.bottom_nav.analysis import ScreenAnalysis
from ui.screens.main.bottom_nav.history import ScreenHistory
from ui.screens.main.bottom_nav.home import ScreenHome
from ui.screens.main.bottom_nav.plans import ScreenPlans


class BottomNav(MDBoxLayout):
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
