from .driver_manager import DriverManager
from selenium import webdriver


class ChromeDriverManager(DriverManager):

    def __init__(self):
        super().__init__()

    def create_driver(self):
        self.driver = webdriver.Chrome(executable_path="../webdrivers/chromedriver.exe")
