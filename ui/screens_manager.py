from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from db import get_db
from ui.main import MainScreen
from ui.transaction_editor import TransactionEditorScreen


class ScreensManager(ScreenManager):

    main: MainScreen = ObjectProperty()
    transaction_editor: TransactionEditorScreen = ObjectProperty()
    db = get_db()
