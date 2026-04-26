#Signup/Login page for Automation Exercise
# Import BasePage to use its methods
from Pages.base_page import BasePage

# LoginPage contains locators and methods used in test cases
class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        # LOGIN locators
        self.LOGIN_EMAIL=self.page.locator('[data-qa="login-email"]')
        self.LOGIN_PASSWORD=self.page.locator('[data-qa="login-password"]')
        self.LOGIN_BUTTON=self.page.locator('button[data-qa="login-button"]')
        self.LOGGED_USER=self.page.locator('a >> b')
        self.ERROR_MESSAGE=self.page.get_by_text("Your email or password is incorrect!")
        self.LOGOUT=self.page.locator('a[href="/logout"]')

        # SIGNUP Locators
        self.SIGNUP_ICON=self.page.get_by_role("link", name="Signup / Login")
        self.NAME=self.page.get_by_placeholder("Name")
        self.SIGNUP_EMAIL=self.page.locator('[data-qa="signup-email"]')
        self.SUBMIT=self.page.get_by_role("button",name="Signup")
        self.ACCOUNT_EXIST=self.page.get_by_text("Email Address already exist!")

        # SIGNUP Account Information Locators
        self.TITLE=self.page.locator('#id_gender2')
        self.signup_NAME=self.page.locator('input[id="name"]')
        self.signup_EMAIL=self.page.locator('input[id="email"]')
        self.PASSWORD=self.page.locator('input[id="password"]')
        #Date of Birth
        self.DAY=self.page.locator('#days')
        self.MONTH=self.page.locator('#months')
        self.YEAR=self.page.locator('#years')

        # Address Information Locators in Signup
        self.FIRST_NAME=self.page.locator('#first_name')
        self.LAST_NAME=self.page.locator('#last_name')
        self.ADDRESS=self.page.locator('#address1')
        self.COUNTRY=self.page.locator('#country')
        self.STATE=self.page.locator('#state')
        self.CITY=self.page.locator('#city')
        self.ZIPCODE=self.page.locator('#zipcode')
        self.MOBILE_NUMBER=self.page.locator('#mobile_number')
        self.CREATE_ACCOUNT=self.page.get_by_role("button",name="Create Account")
        self.ACCOUNT_CREATED=self.page.locator('.col-sm-9.col-sm-offset-1 p')
        self.CONTINUE=self.page.locator('[data-qa="continue-button"]')



    # METHODS TO INTERACT WITH THE ELEMENTS
    # signup() is used to enter username and email for new user
    def signup(self,name,email):
        self.click(self.SIGNUP_ICON)
        self.fill(self.NAME,name)
        self.fill(self.SIGNUP_EMAIL,email)
        self.click(self.SUBMIT)


    # signup_account_info() is used to provide information of new user like first_name,last_name,address
    def signup_account_info(self,password,first_name,last_name,address,state,city,zipcode,mobile_num):
        self.wait_for_selector(self.TITLE)
        self.click(self.TITLE)
        self.fill(self.PASSWORD,password)
        self.select_dropdown(self.DAY,'28')
        self.select_dropdown(self.MONTH,'January')
        self.select_dropdown(self.YEAR,'1995')

        self.fill(self.FIRST_NAME,first_name)
        self.fill(self.LAST_NAME,last_name)
        self.fill(self.ADDRESS,address)
        self.select_dropdown(self.COUNTRY,'India')
        self.fill(self.STATE,state)
        self.fill(self.CITY,city)
        self.fill(self.ZIPCODE,zipcode)
        self.fill(self.MOBILE_NUMBER,mobile_num)
        self.click(self.CREATE_ACCOUNT)
        # self.get_text(self.ACCOUNT_CREATED)


    # login() after proper signup user can log in with valid credentials
    # If the user cannot log in, they must sign up first
    def login(self,email,password):
        self.click(self.SIGNUP_ICON)
        self.fill(self.LOGIN_EMAIL,email)
        self.fill(self.LOGIN_PASSWORD,password)
        self.click(self.LOGIN_BUTTON)


    # logout() is used to log out from the website
    def logout(self,email,password):
        self.login(email,password)
        self.click(self.LOGOUT)






