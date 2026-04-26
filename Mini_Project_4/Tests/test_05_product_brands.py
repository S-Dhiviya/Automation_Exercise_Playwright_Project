# Importing ProductsPage to use its methods
from Pages.products_page import ProductsPage
# Import test data for Product details
from Utils.config import Product_name,Brand_name


# test_search_icon() searches product through search icon in product page
# Any product name can be provided through utils file
def test_search_icon(page):
    search_products=ProductsPage(page)
    search_products.search_product(Product_name)


# test_products_brands() lists the products based on their brands
def test_products_brands(page):
    brands=ProductsPage(page)
    brands.product_brands(Brand_name)
