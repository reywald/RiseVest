import os
from patterns import WEBDRIVER_PATH
from .driver_manager import DriverManager
from selenium import webdriver


class FirefoxDriverManager(DriverManager):

    def __init__(self):
        super().__init__()

    def create_driver(self):
        self.driver = webdriver.Firefox(executable_path="D:\Programming\Projects\Testing\part_two\webdrivers\chromedriver.exe")


