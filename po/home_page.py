from .base_page import BasePage
from .menu_section import MenuSection


class HomePage(BasePage):
    """ The home page"""

    def __init__(self, driver, test_class):
        """Assign elements to the page members"""
        super().__init__(driver, test_class)

        self.page_url = self.driver.current_url
        self.page_title = "Rise - Dollar investments that help you grow."
        self.menu = MenuSection(driver, test_class)

    def validate_page(self):
        self.test_class.assertEqual("https://risevest.com/", self.page_url)
        self.test_class.assertEqual(self.page_title, self.driver.title)

    def perform_action(self):
        self.menu.validate_page()
        self.menu.click_submenu("Build Wealth")
