from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from interfaces.kivy.libs.baseclass.root import Root


class MainScreen(MDScreen):
    root: Root = ObjectProperty()

    def __draw_shadow__(self, origin, end, context=None):
        pass
