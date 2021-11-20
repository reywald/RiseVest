from selenium.webdriver.support.ui import Select
from .page_element import PageElement


class WealthForm(PageElement):
    """ The 'Start Building Your Future' form"""

    def __init__(self, driver_mgr, test_class):
        super().__init__(driver_mgr, test_class)

        self.age_input = self.driver_manager.find_element(self.by.NAME, "age")
        self.salary_input = self.driver_manager.find_element(
            self.by.NAME, "salary")
        self.invest_input = self.driver_manager.find_element(
            self.by.NAME, "investmentPercentage")
        self.retire_input = self.driver_manager.find_element(
            self.by.NAME, "retirementAge")
        self.invest_pref_input = Select(
            self.driver_manager.find_element(self.by.ID, "investmentPreference"))
        self.calculate = self.driver_manager.find_element(
            self.by.CSS_SELECTOR, "form button")

    def validate_page(self):
        self.test_class.assertEqual(
            "35", self.age_input.get_attribute("value"))
        self.test_class.assertEqual(
            "", self.salary_input.get_attribute("value"))
        self.test_class.assertEqual(
            "20", self.invest_input.get_attribute("value"))
        self.test_class.assertEqual(
            "65", self.retire_input.get_attribute("value"))
        invest_type = self.invest_pref_input.all_selected_options
        self.test_class.assertEqual("1", invest_type[0].get_attribute("value"))
        self.test_class.assertEqual("Calculate", self.calculate.text)

    def fill_form(self):
        # Clear all entries and input data
        self.age_input.clear()
        self.age_input.send_keys("25")
        self.salary_input.clear()
        self.salary_input.send_keys("350000")
        self.invest_input.clear()
        self.invest_input.send_keys("20")
        self.retire_input.clear()
        self.retire_input.send_keys("60")
        self.invest_pref_input.select_by_visible_text("Stability")
        self.calculate.submit()
