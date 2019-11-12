"""Run tests and document results."""

import os.path
import sys
from datetime import datetime
from selenium import webdriver  # for testing web app

def test_flask_app(URL, page_title):
    """Tests that Flask App is running as expected.
    
    Uses Selenium Webdriver to check Flask app is running as expected.
    
    Args:
        URL (string): the address where the flask app is running.
        page_title (string): the title of the webpage, 
            as it should be defined by <title> tags.
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    if driver.title==page_title:
        result = "\nTest Successful: Flask App running as expected."
    else:
        result = "\nError: Flask App not running as expected."
    print(result)
    return result

with open(os.path.join(sys.path[0], 'test_output', 'logs.txt'), 'a') as f:
    now = datetime.now()
    f.write("\n"+now.strftime("%d/%m/%Y %H:%M:%S"))
    f.write(test_flask_app("localhost:5000","House Prices"))
    f.write("\n")


