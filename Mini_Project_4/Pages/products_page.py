# Products page for Automation Exercise
# Importing random to choose the random products from the page
import random
# Import BasePage to use its methods
from Pages.base_page import BasePage


# ProductsPage contains locators and methods used in test cases
class ProductsPage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        # PRODUCTS Locators
        self.PRODUCTS_ICON=self.page.locator('//a[text()=" Products"]')
        self.PRODUCTS=self.page.locator('.features_items .product-image-wrapper')
        self.SEARCH_PRODUCT=self.page.locator('input#search_product')
        self.SEARCH_ICON=self.page.locator('button#submit_search')
        self.CONTINUE_SHOPPING = self.page.get_by_role("button", name="Continue Shopping")

        # Product Brands Locators
        self.VIEW_PRODUCT =self.page.get_by_text("View Product")
        self.BRANDS = self.page.locator('div.brands-name')
        self.ALL_BRANDS=self.page.locator('ul.nav.nav-pills.nav-stacked li')

        # CART PAGE LOCATORS
        self.CART_ICON=self.page.get_by_role("a",name="Cart")
        self.CART_TABLE=self.page.locator('table#cart_info_table')



    # METHODS TO INTERACT WITH THE ELEMENTS
    # add_products() randomly selects the 5 products out of total products
    # Selected product are added to cart
    def add_products(self):
        self.click(self.PRODUCTS_ICON)
        total_products=self.PRODUCTS.count()
        print(total_products)

        # randomly selects the product
        selected=random.sample(range(total_products),5)

        # Using index to select products
        for i in selected:
            product = self.PRODUCTS.nth(i)
            # Hover over product
            product.hover()

            # .first ensures you interact with the correct visible one
            name = product.locator('.productinfo p').first.text_content().strip()
            price = product.locator('.productinfo h2').first.text_content().strip()
            print(f"{name} - {price}")

            # Selected products gets added to cart
            ADD_TO_CART= product.locator('.product-overlay a.add-to-cart')
            self.click(ADD_TO_CART)

            # Clicks on Continue shopping after each product is added to the cart
            self.wait_for_selector(self.CONTINUE_SHOPPING)
            self.click(self.CONTINUE_SHOPPING)


    # add_specific_products() clicks on specific product based on its name
    # Uses filter to match the product name
    def add_specific_products(self,product_name):
        self.click(self.PRODUCTS_ICON)
        self.specific_products = self.page.locator(".productinfo").filter(has_text=product_name)

        name = self.specific_products.locator('p').inner_text()
        price = self.specific_products.locator('h2').inner_text()

        print(f"{name} - {price}")
        self.specific_products.hover()

        # Add specific product to cart
        ADD_TO_CART = self.specific_products.locator('a.add-to-cart')
        self.click(ADD_TO_CART)


    # invalid_product_search() searches for invalid product and if product doesn't exist returns Fasle
    def invalid_product_search(self, product_name):
        product = self.page.locator(".productinfo").filter(has_text=product_name)

        if product.count() == 0:
            return False

        # If product exists it adds it to cart by clicking it
        product.locator("a").click()
        return True


    # search_product() enters the product name in the search field and views the product
    def search_product(self,product_name):
        self.click(self.PRODUCTS_ICON)
        self.fill(self.SEARCH_PRODUCT,product_name)
        self.click(self.SEARCH_ICON)
        self.click(self.VIEW_PRODUCT)


    # In Playwright, you can filter an existing locator instead of redefining it.
    # BRANDS_NAME() is used to select a specific brand name
    def BRANDS_NAME(self, brand_name):
        return self.ALL_BRANDS.filter(has_text=brand_name)


    # product_brands() selects the brands and list the products of that brands
    def product_brands(self,brand_name):
        self.click(self.PRODUCTS_ICON)
        # expect(self.BRANDS).to_be_visible()
        self.wait_for_selector(self.BRANDS)
        self.BRANDS_NAME(brand_name).click()
