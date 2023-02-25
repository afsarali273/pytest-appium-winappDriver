
from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import scenario, given, when, then

feature_path = '../features/test_scenario_creation.feature'


@scenario(feature_path, 'Create simple scenario on AE')
def test_scenario_creation():
    pass


@given('I open AE as admin user')
def i_open_ae_as_admin_user(app):
    app.find_element(AppiumBy.NAME, "Clear").click()
    app.find_element(AppiumBy.NAME, "Seven").click()
    app.find_element(AppiumBy.NAME, "Clear").click()


@when('I create scenario on AE')
def i_create_scenario(app):
    app.find_element(AppiumBy.NAME, "One").click()
    app.find_element(AppiumBy.NAME, "Plus").click()
    app.find_element(AppiumBy.NAME, "Seven").click()
    app.find_element(AppiumBy.NAME, "Equals").click()


@then('I should see created scenario in scenario list')
def i_verify_created_scenario(app):
    #     Addition
    app.find_element(AppiumBy.NAME, "One").click()
    app.find_element(AppiumBy.NAME, "Plus").click()
    app.find_element(AppiumBy.NAME, "Seven").click()
    app.find_element(AppiumBy.NAME, "Equals").click()
