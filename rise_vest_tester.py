from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from po.home_page import HomePage
from po.build_wealth_page import WealthPage

from patterns.driver_manager import DriverManager
from patterns.driver_types import DriverTypes
from patterns.driver_manager_factory import DriverManagerFactory


class RiseVestTester(TestCase):

    def setUp(self):
        self.home_url = "https://rise.capital"

        # Choices of drivers: FIREFOX, CHROME, EDGE
        # self.driver_manager: DriverManager = DriverManagerFactory.get_manager(DriverTypes.CHROME)
        # self.driver_manager: DriverManager = DriverManagerFactory.get_manager(DriverTypes.EDGE)
        self.driver_manager: DriverManager = DriverManagerFactory.get_manager(DriverTypes.FIREFOX)
        self.driver = self.driver_manager.get_driver()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver = None
        self.driver_manager.quit_driver()

    def test_build_wealth_page(self):
        self.driver.maximize_window()
        self.driver.get(self.home_url)

        home_page = HomePage(self.driver, self)
        home_page.validate_page()
        home_page.perform_action()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("wealth")
        )
        wealth_page = WealthPage(self.driver, self)
        wealth_page.validate_page()

    def test_fill_wealth_form(self):
        self.driver.maximize_window()
        self.driver.get(self.home_url)

        home_page = HomePage(self.driver, self)
        home_page.perform_action()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("wealth")
        )

        wealth_page = WealthPage(self.driver, self)
        wealth_page.perform_action()
