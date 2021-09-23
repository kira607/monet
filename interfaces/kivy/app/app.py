import kivy
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton

from budget import Budget
from budget.models import Operation

kivy.require('2.0.0')

class MainApp(MDApp):
    def __init__(self, budget_ref: Budget, **kwargs):
        self.budget = budget_ref
        super().__init__(**kwargs)

    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen
