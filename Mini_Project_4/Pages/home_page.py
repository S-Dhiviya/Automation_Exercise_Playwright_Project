#Home page for Automation Exercise
# Import BasePage to use its methods
from Pages.base_page import BasePage


# HomePage contains locators used in test cases
class HomePage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        # Locators are stored as key-value pairs in a dictionary
        self.elements={
            "HOME":self.page.get_by_text("Home"),
            "PRODUCTS_ICON":self.page.locator('//a[text()=" Products"]'),
            "CART_ICON":self.page.get_by_role("link", name="Cart"),
            "SIGNUP_ICON": self.page.get_by_role("link", name="Signup / Login"),
            "TESTCASES": self.page.locator('a[href="/test_cases"]').first,
            "API_TESTING": self.page.get_by_role("link", name="API Testing").first,
            "VIDEO": self.page.get_by_role("link", name="Video Tutorials"),
            "CONTACT_US":self.page.locator('a[href="/contact_us"]')
        }

        # These locators appear after logged in
        self.DELETE_ACCOUNT=self.page.get_by_role("link",name="Delete Account")
        self.DELETE_MESSAGE=self.page.locator('[data-qa="account-deleted"]')