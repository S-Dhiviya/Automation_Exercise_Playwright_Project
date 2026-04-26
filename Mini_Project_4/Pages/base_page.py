# POM Framework using playwright for Automation Exercise website
# Page classes represents the webpage.
# BasePage contains init, searching selector, fill values,click and explicit wait
# Used to perform assertions on elements
from playwright.sync_api import expect

class BasePage:

    #Constructor to initialize the page object
    def __init__(self, page):
        self.page = page

    # Generic method to click on any element
    def click(self, locator):
        locator.click()

    # Generic method to fill input fields
    def fill(self, locator, value):
        locator.fill(value)

    # Explicit wait to ensure element is visible
    def wait_for_selector(self, locator):
        expect(locator).to_be_visible()

    # Method to get text from an element
    def get_text(self, locator):
        # Returns the text content of the element
        return locator.text_content()

    # Method to select value from dropdown
    def select_dropdown(self, locator, value):
        locator.select_option(value)