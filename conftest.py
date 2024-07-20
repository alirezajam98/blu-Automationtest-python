import pytest
import yaml
import logging
import os

from utils.driver import create_driver

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("test_log.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default=None, help="Device to run tests on")

@pytest.fixture(scope='session')
def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

@pytest.fixture(scope='session')
def setup_environment(load_config):
    logger.info("Setting up environment")
    yield
    logger.info("Tearing down environment")

@pytest.fixture(scope='function')
def create_driver_fixture(request, load_config):
    device_name = request.config.getoption("--device")
    if not device_name:
        pytest.fail("Device name must be specified using --device option")
    desired_caps = load_config['desired_caps'][device_name]
    driver = create_driver(desired_caps)
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    screenshot_path = os.path.join('screenshots', f"{name}.png")
    driver.save_screenshot(screenshot_path)
    logger.info(f"Screenshot saved to {screenshot_path}")
