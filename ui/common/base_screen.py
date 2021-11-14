from kivymd.uix.bottomnavigation import MDBottomNavigationItem


class BaseScreen(MDBottomNavigationItem):
    def init(self, budget):
        self.budget = budget
