from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .menu_section import MenuSection
from .wealth_form import WealthForm
from .projection_section import ProjectionSection


class WealthPage(BasePage):
    """ The Build Wealth Page """

    def __init__(self, driver, test_class):
        super().__init__(driver, test_class)

        self.page_url = self.driver.current_url
        self.page_title = "Build Wealth - Dollar investments that help you grow."
        self.menu = MenuSection(driver, test_class)
        self.heading1 = self.driver.find_element(self.by.CSS_SELECTOR, "div#__next div.container .w-full h1")
        self.wealth_form = WealthForm(driver, test_class)
        self.projection_section = ProjectionSection(driver, test_class)

    def validate_page(self):
        self.test_class.assertIn("build-wealth", self.page_url)
        self.test_class.assertEqual(self.page_title, self.driver.title)
        self.menu.validate_page()
        self.wealth_form.validate_page()
        self.test_class.assertEqual("Save for retirement in dollars", self.heading1.text)
        print(self.heading1.text)

    def perform_action(self):
        self.wealth_form.fill_form()
        # WebDriverWait(self.driver, 5)
        self.projection_section.verify_wealth_value("$1,309,578.71", "35")