# Importing LoginPage to use its methods
from Pages.login_page import LoginPage
# Import test data for Sign up
from Utils.config import Name,Email,Password,First_Name,Last_Name,Address,State,City,Zipcode,Mobile_no


# test_existing_signup_user() checks if the user has already signed up
# Asserts Email Address already exist
def test_existing_signup_user(page):
    signup_page=LoginPage(page)
    signup_page.signup('diya','diya123@gmail.com')
    assert signup_page.ACCOUNT_EXIST.inner_text() =="Email Address already exist!"


# test_signup_account_info() creates new user sign up and prints error message if user exists
# Displays account created information and user can log in with the details
def test_signup_account_info(page):
    signup=LoginPage(page)
    signup.signup(Name,Email)

    if signup.ACCOUNT_EXIST.is_visible():
        print(signup.ACCOUNT_EXIST.inner_text())

    else:
        page.wait_for_url('https://www.automationexercise.com/signup')
        signup.signup_account_info(Password,First_Name,Last_Name,Address,State,City,Zipcode,Mobile_no)

        # all_inner_texts() displays all the text context in the page
        text=signup.ACCOUNT_CREATED.all_inner_texts()
        for t in text:
            print(t)


# test_empty_field_signup() signup with just "".
# This throws a validation message to fill the field
def test_empty_field_signup(page):
    signup = LoginPage(page)
    signup.signup("","")
    message = signup.SIGNUP_EMAIL.evaluate("el => el.validationMessage")
    print("Validation message:", message)




