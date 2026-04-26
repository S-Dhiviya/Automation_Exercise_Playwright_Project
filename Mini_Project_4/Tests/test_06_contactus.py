# Importing ContactusPage to use its methods
from Pages.contactus_page import ContactPage
# Used to perform assertions on elements
from playwright.sync_api import expect
# Import test data for user details
from Utils.config import Name,Email,Subject,Message


# test_contactus_icon() clicks on Contact_Us icon and enters the contact page
# Asserts "Get In Touch" content in the page
def test_contactus_icon(page):
    contact_us=ContactPage(page)
    contact_us.CONTACT_US.click()
    page.wait_for_url('https://www.automationexercise.com/contact_us')
    expect(contact_us.CONTACT_TEXT).to_be_visible()


# test_contactus_form() enters valid data and submits the form
def test_contactus_form(page):
    contact_form=ContactPage(page)
    contact_form.contactus(Name,Email,Subject,Message)
