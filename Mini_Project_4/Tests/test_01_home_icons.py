# Importing HomePage to use its methods
from Pages.home_page import HomePage
# Used to perform assertions on elements
from playwright.sync_api import expect


# test_home_url() asserts the page url and title of automation exercise
def test_home_url(page):
    expect(page).to_have_url("https://www.automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")


# test_invalid_home_url() asserts the invalid page url and title of automation exercise
def test_invalid_home_url(page):
    expect(page).to_have_url("https://www.automation.com/")
    expect(page).to_have_title("Cart Page")


# test_home_icons() checks each menu stored in dictionary form is visible or not
def test_home_icons(page):
    home_icons=HomePage(page)
    for name, selector in home_icons.elements.items():
        expect(selector).to_be_visible()
        print(f"{name} is visible")


