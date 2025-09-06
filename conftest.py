import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')
    
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    
    yield driver
    driver.quit()