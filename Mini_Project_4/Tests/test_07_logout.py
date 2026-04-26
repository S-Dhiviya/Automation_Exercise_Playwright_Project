# Importing LoginPage,HomePage to use its methods
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
# Import test data for log out credentials
from Utils.config import Email,Password


# test_logout() works only if user is already logged in
#log out using valid credentials and asserts the home page url
def test_logout(page):
    logout=LoginPage(page)
    logout.logout(Email,Password)
    assert page.url=="https://www.automationexercise.com/login"


# test_delete_account() user can delete their account if it is not needed
# Valid login process is necessary before deletion
def test_delete_account(page):
    login_page=LoginPage(page)
    login_page.login(Email,Password)
    assert page.url == "https://www.automationexercise.com/"
    delete_icon=HomePage(page)
    delete_icon.click(delete_icon.DELETE_ACCOUNT)
    print(delete_icon.get_text(delete_icon.DELETE_MESSAGE))
