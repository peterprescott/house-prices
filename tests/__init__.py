"""Run tests and document results."""

from datetime import datetime
from selenium import webdriver  # for testing web app

def test_flask_app(page_location, page_title):
    """Tests that Flask App is running as expected.

    Uses Selenium Webdriver to check Flask App is running as expected.

    Args:
        URL (string): the address where the Flask App is running.
        page_title (string): the title of the webpage,
            as it should be defined by <title> tags.
    """
    driver = webdriver.Chrome()
    driver.get(page_location)
    if driver.title == page_title:
        result = "\nTest Successful: Flask App running as expected."
    else:
        result = "\nError: Flask App not running as expected."
    print(result)
    return result

if __name__ == '__main__':
    with open('logs.txt', 'a') as f:
        NOW = datetime.now()
        f.write("\n"+NOW.strftime("%d/%m/%Y %H:%M:%S"))
        f.write(test_flask_app("localhost:5000", "House Prices"))
        f.write("\n")
