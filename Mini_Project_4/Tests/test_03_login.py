# Importing LoginPage to use its methods
from Pages.login_page import LoginPage
# Used to perform assertions on elements
from playwright.sync_api import expect
# Import test data for login credentials
from Utils.config import Name,Email,Password,Invalid_Email,Invalid_Password


# test_valid_login() tests with valid login email and password
# Asserts the page url
def test_valid_login(page):
    login_page=LoginPage(page)
    login_page.login(Email,Password)
    assert page.url=="https://www.automationexercise.com/"


# test_invalid_login() tests the log in with invalid email and password
# Asserts the error message
def test_invalid_login(page):
    invalid_login = LoginPage(page)
    invalid_login.login(Invalid_Email, Invalid_Password)
    expect(invalid_login.ERROR_MESSAGE).to_have_text("Your email or password is incorrect!")
    print(invalid_login.get_text(invalid_login.ERROR_MESSAGE))


#  test_logged_user() tests the logged username appears as "Logged in as {username}"
def test_logged_user(page):
    login_user=LoginPage(page)
    login_user.login(Email,Password)
    expect(login_user.LOGGED_USER).to_have_text(Name)
