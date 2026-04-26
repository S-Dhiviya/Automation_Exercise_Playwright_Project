# Importing ProductsPage to use its methods
from Pages.products_page import ProductsPage
# Import test data for Product details
from Utils.config import Product_name,Invalid_Product_name


# test_random_products() adds 5 random products and adds to cart
# Displays name and price of the product
def test_random_products(page):
    random_products=ProductsPage(page)
    random_products.add_products()
    page.goto('https://www.automationexercise.com/view_cart')


# test_specific_products() searches for a specific product through product name
# Adds it to the cart
def test_specific_products(page):
    specific_product=ProductsPage(page)
    specific_product.add_specific_products(Product_name)


# test_invalid_product() searches for an invalid product through product name
#Asserts result is False so this negative test case Passes
def test_invalid_product(page):
    invalid_product=ProductsPage(page)
    result=invalid_product.invalid_product_search(Invalid_Product_name)
    assert result is False

