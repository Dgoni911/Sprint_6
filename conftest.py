<<<<<<< HEAD
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
=======
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
>>>>>>> 5e94532fc497709f8b899320f9d7b50e5d8148b5
    driver.quit()