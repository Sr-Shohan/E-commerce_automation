from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="session", autouse=True)
def driver():
    # Set up the ChromeOptions object for headless browsing
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    # Initialize the WebDriver instance with the ChromeOptions object
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # Return the WebDriver instance for use in the tests
    yield driver
    # Tear down the WebDriver instance
    driver.quit()
