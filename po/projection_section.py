from .page_element import PageElement


class ProjectionSection(PageElement):

    def __init__(self, driver, test_case):
        super().__init__(driver, test_case)

        self.heading = self.driver.find_element(self.by.CSS_SELECTOR, "h2.border-inputBorder")
        self.wealth_goal = self.driver.find_element(self.by.CSS_SELECTOR, "p.text-2xl")
        self.duration = self.driver.find_element(self.by.CSS_SELECTOR, "p.text-2xl + p")

    def validate_page(self):
        self.test_class.assertEqual("Projection", self.heading.text)
        self.test_class.assertEqual("$0.00", self.wealth_goal.get_attribute("value"))
        self.test_class.assertEqual("In 30 Years", self.duration)

    def verify_wealth_value(self, goal, duration):
        self.test_class.assertEqual(goal, self.wealth_goal.text)
        self.test_class.assertEqual(f"In {duration} Years", self.duration.text)
        print(goal)