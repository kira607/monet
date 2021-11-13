from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from libs.baseclass.screens.main_screen import MainScreen
from libs.baseclass.screens.transaction_editor_screen import TransactionEditorScreen


class AppManager(ScreenManager):

    main: MainScreen = ObjectProperty()
    transaction_editor: TransactionEditorScreen = ObjectProperty()

    def __init__(self, budget, **kwargs):
        super().__init__(**kwargs)
        self.budget = budget
        self.main.root.set_budget(self.budget)
