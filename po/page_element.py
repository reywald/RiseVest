from unittest import TestCase
from abc import abstractmethod
from selenium.webdriver.common.by import By
from patterns.driver_manager import DriverManager


class PageElement:
    """ The base page element from which other page elements inherit """

    def __init__(self, driver_mgr: DriverManager, test_class: TestCase) -> None:
        """Assign elements to the page members"""
        self.driver_manager = driver_mgr
        self.test_class = test_class
        self.by = By

    @abstractmethod
    def validate_page(self):
        """ Check that all elements of the page are in place with
        the right text content
        """
        pass
