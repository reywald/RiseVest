# Project Deployment Instructions
## Prerequisites
1. **Git preinstalled and configured**
2. **Python 3.7+ must be installed on the target machine**

## Steps
1. Navigate to a directory to hold the project.
2. Open a browser and navigate to https://github.com/reywald/RiseVest
3. Download the repository and copy it to the directory in step (1).
4. Extract the contents to the directory.
5. Navigate into the newly extracted repository.
6. Open a command-line interface (CLI) and navigate to the repository's directory.
7. Create a directory called **.venv** to contain the virtual environment for python.
    * ***mkdir .venv***
9. Install **pipenv**: 
    * ***python -m pip install pipenv*** or ***pip install pipenv***.
11. Once completed, create the virtual environment and install all dependencies in one go:
    * ***pipenv install***
12. Start up the virtual environment:
    * ___pipenv shell___ 👍
14. Run the tests:
    * ___python -m unittest___.
16. To run on different browsers, open ___rise_vest_tester.py___, scroll to line 19-22 and (un)comment the desired line.
```python
[13] class RiseVestTester(TestCase):
[14]
[15]    def setUp(self):
[16]        self.home_url = "https://rise.capital"
[17]
[18]        # Choices of drivers: FIREFOX, CHROME, EDGE
[19]        self.driver_manager: DriverManager = DriverManagerFactory.get_manager(
[20]            DriverTypes.CHROME)
[21]        # self.driver_manager: DriverManager = DriverManagerFactory.get_manager(DriverTypes.EDGE)
[22]        # self.driver_manager: DriverManager = DriverManagerFactory.get_manager(DriverTypes.FIREFOX)
[23]        self.driver = self.driver_manager.get_driver()
[24]        self.driver.implicitly_wait(10)
```
