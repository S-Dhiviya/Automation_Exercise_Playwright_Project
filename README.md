                  ** Automation Testing of Automation Exercise(https://automationexercise.com/) **  
			
The application under test is a demo e-commerce platform designed for practicing web automation and testing scenarios. It provides a wide range of features including user registration, login, product browsing, cart management, and checkout workflows, making it suitable for end-to-end testing.The platform includes various interactive UI components such as forms, dynamic elements, allowing comprehensive validation of real-world user interactions. It also supports multiple navigation flows and user states, which are essential for validating session handling and page transitions.

The test scripts are developed using Playwright with Python and Pytest, following the Page Object Model (POM) framework and adhering to Object-Oriented Programming (OOP) principles. Common configurations are handled in config.py.The suite includes 7 detailed test cases focused on verifying page behavior,login process,navigation flows, products selection, adding products to cart and logout process.


**Project Architecture :**

**MiniProject4/**
│
├── **Pages/**
│   ├── __init__.py
│   ├── base_page.py
│   ├── contactus_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│
├── **Tests/**
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_01_home_icons.py
│   ├── test_02_signup.py
│   ├── test_03_login.py
│   ├── test_04_products.py
│   ├── test_05_product_brands.py
│   ├── test_06_contactus.py
│   ├── test_07_logout.py
│
├── **Utils/**
│   ├── __init__.py
│   ├── config.py
│
├── requirements.txt
├── pytest.ini
├── README.md



**Tools & Technologies:**
*     Playwright
*     Python 
*     Pytest
*     OOPS
*     Page Object Model (POM)
*     Pytest HTML Reports


  **Test Suite :**

  Test Case 1: Verify that the home URL,title and icons of home page is visible or not

	* Validates proper navigation to (https://automationexercise.com/) and asserts current URL and title.
    * Validates invalid URL and title of (https://automationexercise.com/)
    * Checks all the home icons like(Home,Products,Cart,Test Cases,API testing,Video Tutorials, Contact Us) stored as dictionary is visible or not.

   Test Case 2: Creating a new user login using Sign up with user details

	* Validates whether the user has already signed up. This throws error message like "Email already exists".
	* Creates new user along with user details like Password,First_Name,Last_Name,Address,State,City,Zipcode,Mobile_no and displays account created.
  * Signup with empty fields and this throws a validation message like "Please fill in the field".

   Test Case 3: Validate login functionality using both valid and invalid credentials, and verify that the correct username is displayed on the home page.

	* Checks successful login with valid email and password of user.
	* Validates login functionality with invalid email and password and asserts the error message "Your email or password is incorrect!".
  * Checks logged username appears in home page "Logged in as {username}" after entering valid credentials.

   Test Case 4: Selection of products from the products list and adds it to cart

	* Selects 5 random products out of total products and adds it to cart. Displays the name and price of product
	* Searches for any specific product using product name and adds it to cart.
  * Searches for an invalid product which is not available and asserts the result.

   Test Case 5: Searches products through search icon and based on its brands
  
	* Checks whether product can be located through Search icon by entering Product name search.
  * Verifies products get listed based on their brands by clicking on Brands name.
	  
   Test Case 6: To check whether the ‘Contact Us’ icon is visible and to submit the feedback form

	* Verifies whether Contact Us icon is visible or not.
	* Enter valid data (Name, Email, Subject, and Message) and click Submit to provide feedback or for any other purpose.

   Test Case 7: Verify that the user can successfully log out of the application and deletion of account
  
	* If a user has properly logged in with valid details,user can successfully logout.
	* After proper login and purchase of products, user can also delete their account.

 
Instructions:

1.Ensure Playwright,Python and any Browser(Chrome,Firefox,Edge) installed in your system.

>pip install playwright

>playwright install

2.To create a virtual environment,

>python -m venv venv

>source venv/bin/activate(macOS)

>venv\scripts\activate(Windows)

3.To install the dependencies,

>pip install -r requirements.txt

4.To execute all the test files,

>pytest -v -s Tests/

>pytest -v -s Tests/test_01_home_icons.py(for any specific file)

>pytest -v -s Tests/test_01_home_icons.py::test_invalid_home_url(for specific method in a test file)


To Generate HTML Report:

To install pytest–html package

>pip install pytest–html

To execute all the test files and generate html report,

>pytest -v -s Tests/   --html=reports.html    --self-contained-html

To execute single file and generate html report,

>pytest -v -s Tests/test_01_home_icons.py --html=case01_report.html   --self-contained-html

