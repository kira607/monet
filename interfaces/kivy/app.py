import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.0.0')


class MyApp(App):
    def __init__(self, t, **kwargs):
        self.t = t
        super().__init__(**kwargs)

    def build(self):
        return Label(text=self.t)
