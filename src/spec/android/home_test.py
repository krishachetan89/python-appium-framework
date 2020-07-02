from src.helpers.appiumdriver import Driver
from src.screens.android.home_screen import HomeLocators
from src.helpers.app import App


class TestHome(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def test_home_1(self):
        App.element(self, HomeLocators.homeMenu)
        App.element(self, HomeLocators.loginMenu)
        App.element(self, HomeLocators.formsMenu)
        App.element(self, HomeLocators.swipeMenu)
        # App.assert_text(self, HomeLocators.loginMenu, 'Leads')

    def test_home_2(self):
        App.element(self, HomeLocators.homeMenu)
        App.element(self, HomeLocators.loginMenu)