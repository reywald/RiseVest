from .driver_types import DriverTypes
from .driver_manager import DriverManager
from .chrome_driver_manager import ChromeDriverManager
from .firefox_driver_manager import FirefoxDriverManager
from .edge_driver_manager import EdgeDriverManager


class DriverManagerFactory:

    def __init__(self):
        self.manager = None

    @classmethod
    def get_manager(cls,  driver_type: DriverTypes) -> DriverManager:
        """ Simulate a switch case to create the proper webdriver
        to return, given a driver type.
        """
        return {
            DriverTypes.CHROME: ChromeDriverManager,
            DriverTypes.FIREFOX: FirefoxDriverManager,
            DriverTypes.EDGE: EdgeDriverManager,
        }[driver_type]()
