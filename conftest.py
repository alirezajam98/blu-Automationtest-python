import pytest
from utils.driver import create_driver


@pytest.fixture(scope='function')
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def base_url():
    return 'http://127.0.0.1:4723/wd/hub'
