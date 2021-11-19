import os
from patterns import WEBDRIVER_PATH
from .driver_manager import DriverManager
from selenium import webdriver


class EdgeDriverManager(DriverManager):

    def __init__(self):
        super().__init__()

    def create_driver(self):
        self.driver = webdriver.Edge(executable_path="./webdrivers/msedgedriver.exe")
        # print(os.path.join(WEBDRIVER_PATH, "msedgedriver.exe"))
        # self.driver = webdriver.Edge(executable_path=os.path.join(WEBDRIVER_PATH, "msedgedriver.exe"))


