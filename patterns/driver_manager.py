from abc import ABC, abstractmethod
from selenium import webdriver


class DriverManager(ABC):

    def __init__(self):
        self.driver: webdriver = None

    @abstractmethod
    def create_driver(self):
        """Create the driver, add desired capabilities, if necessary."""
        pass

    def get_driver(self) -> webdriver:
        """Initialize the driver and return it"""
        if self.driver is None:
            self.create_driver()
        return self.driver

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
