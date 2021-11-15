from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from ui.main.accounts import AccountsTab
from ui.main.analysis import AnalysisTab
from ui.main.history import HistoryTab
from ui.main.home import HomeTab
from ui.main.plans import PlansTab


class MainScreen(MDScreen):
    plans_screen: PlansTab = ObjectProperty()
    history_screen: HistoryTab = ObjectProperty()
    home_screen: HomeTab = ObjectProperty()
    analysis_screen: AnalysisTab = ObjectProperty()
    accounts_screen: AccountsTab = ObjectProperty()
