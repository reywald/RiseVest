from .page_element import PageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuSection(PageElement):
    """ The menu section of every page"""

    def __init__(self, driver, test_class) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, test_class)

        self.page_url = self.driver_manager.current_url
        self.home_link = self.driver_manager.find_element(self.by.XPATH, "//nav/a[1]")
        self.investment_link = self.driver_manager.find_element(self.by.XPATH, "//nav/a[2]")
        self.about_link = self.driver_manager.find_element(self.by.XPATH, "//nav/a[3]")
        self.faqs_link = self.driver_manager.find_element(self.by.XPATH, "//nav/a[4]")
        self.blog_link = self.driver_manager.find_element(self.by.XPATH, "//nav/a[5]")

        # Sub-menus
        # self.products_link = self.driver.find_element(self.by.CSS_SELECTOR, "nav div.z-50 span.main-nav-item > span")
        self.products_link = self.driver_manager.find_element(self.by.CSS_SELECTOR, "nav div.z-50 > div.cursor-pointer")
        self.stocks_link = self.driver_manager.find_element(self.by.CSS_SELECTOR, "nav a.dropdown-nav-item:nth-child(1)")
        self.real_estate_link = self.driver_manager.find_element(self.by.CSS_SELECTOR, "nav a.dropdown-nav-item:nth-child(2)")
        self.fixed_income_link = self.driver_manager.find_element(self.by.CSS_SELECTOR, "nav a.dropdown-nav-item:nth-child(3)")
        self.build_wealth_link = self.driver_manager.find_element(self.by.CSS_SELECTOR, "nav a.dropdown-nav-item:nth-child(4)")

    def validate_page(self):
        self.test_class.assertEqual("Home", self.home_link.text)
        self.test_class.assertEqual("Investment Club", self.investment_link.text)
        self.test_class.assertEqual("Products", self.products_link.text)
        self.test_class.assertEqual("Investment Club", self.investment_link.text)
        self.test_class.assertEqual("About Us", self.about_link.text)
        self.test_class.assertEqual("FAQs", self.faqs_link.text)
        self.test_class.assertEqual("Blog", self.blog_link.text)

        # Assert the submenu by waiting implicitly for the menu to drop down
        self.drop_menu()
        self.test_class.assertEqual("Stocks", self.stocks_link.text)
        self.test_class.assertEqual("Real Estate", self.real_estate_link.text)
        self.test_class.assertEqual("Fixed Income", self.fixed_income_link.text)
        self.test_class.assertEqual("Build Wealth", self.build_wealth_link.text)
        self.products_link.click()

    def click_menu(self, menu_type: str):
        """Use the passed menu_type string to determine which menu to click"""
        return {
            "Home": self.home_link.click,
            "Investment Club": self.investment_link.click,
            "About Us": self.about_link.click,
            "FAQs": self.faqs_link.click,
            "Blog": self.blog_link.click,
            "Products": self.drop_menu,
        }[menu_type]()

    def click_submenu(self, submenu_type: str):
        return {
            "Stocks": lambda: (self.drop_menu(1), self.stocks_link.click()),
            "Real Estate": lambda: (self.drop_menu(2), self.real_estate_link.click()),
            "Fixed Income": lambda: (self.drop_menu(3), self.fixed_income_link.click()),
            "Build Wealth": lambda: (self.drop_menu(4), self.build_wealth_link.click()),
        }[submenu_type]()

    def drop_menu(self, index: int = 1):
        self.products_link.click()
        WebDriverWait(self.driver_manager, 10).until(
            EC.element_to_be_clickable((self.by.CSS_SELECTOR, f"nav a.dropdown-nav-item:nth-child({index})"))
        )