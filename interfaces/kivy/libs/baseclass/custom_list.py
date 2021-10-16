from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class CustomItem(RecycleDataViewBehavior, BoxLayout):
    pass


class CustomList(RecycleView):
    pass
