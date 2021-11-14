from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from .bottom_nav import BottomNav


class MainScreen(MDScreen):
    root: BottomNav = ObjectProperty()

    def __draw_shadow__(self, origin, end, context=None):
        pass
