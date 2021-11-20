#Project Deployment Instructions
_____________________________________
##Requirements
1. Git preinstalled and configured
2. Python 3.7+ must be installed on the target machine

##Steps
1. Navigate to a directory to hold the project.
2. Open a browser and navigate to https://github.com/reywald/qa-test
3. Download the repository and copy it to the directory in step (1).
4. Extract the contents to the directory.
5. Navigate into the newly extracted repository.
6. Open a command-line interface (CLI) and navigate to the repository's directory.
7. Type the command: pip install -r requirements.txt, or
8. Alternative, type: _python -m pip install pipenv_. Once that is done, type: _pipenv install_.
9. Once all dependencies are installed, if option 7 is followed, type: _activate.bat_, to start up the virtual environment.
10. If option 8 is followed, type: _pipenv shell_ to start up the virtual environment.
11. Run: _python -m unittest_.
12. To run on different browsers, open _rise_vest_tester.py_, scroll to line 19-22 and (un)comment the desired line.