import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def app():

    desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
                    "platformName": "Windows",
                    "deviceName": "WindowsPC"
                    }
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=desired_caps)

    yield driver

    driver.quit()
