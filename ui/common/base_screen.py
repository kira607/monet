from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from db import get_db


class BaseTab(MDBottomNavigationItem):
    db = get_db()

