#Contact Us page for Automation Exercise
# Import BasePage to use its methods
from Pages.base_page import BasePage


# ContactPage contains locators and methods used in test cases
class ContactPage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        # Contact Us locators
        self.CONTACT_US=self.page.locator('a[href="/contact_us"]')
        self.CONTACT_TEXT=self.page.get_by_text("Get In Touch")
        self.NAME=self.page.locator('[data-qa="name"]')
        self.EMAIL=self.page.locator('[data-qa="email"]')
        self.SUBJECT=self.page.locator('[data-qa="subject"]')
        self.MESSAGE=self.page.locator('[data-qa="message"]')
        self.UPLOAD_FILE=self.page.locator('[name="upload_file"]')
        self.SUBMIT=self.page.locator('[data-qa="submit-button"]')



    # METHODS TO INTERACT WITH THE ELEMENTS
    # contactus() helps to send feedbacks or queries to the page
    def contactus(self,name,email,subject,message):
        self.click(self.CONTACT_US)
        self.fill(self.NAME,name)
        self.fill(self.EMAIL,email)
        self.fill(self.SUBJECT,subject)
        self.fill(self.MESSAGE,message)

        # Uploading file uses set_input_files('file_path')
        self.UPLOAD_FILE.set_input_files('/Users/dhiviya/Desktop/exchange.py')
        self.click(self.SUBMIT)