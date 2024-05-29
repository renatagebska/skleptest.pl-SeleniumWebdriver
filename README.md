# skleptest.pl-SeleniumWebdriver
## Automation of Test Cases using Selenium Webdriver

## Test Cases:
### ID: 001 Functional Tests for User Registration
### Test 1
### Title: Registration of a new user using new registration details.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/.
* Click the "Account" link.
* Enter the registration email.
* Enter the password.
* Click the registration button.
* Check if the registration was successful.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ will open in the Chrome browser window.
* After step 4: The "Account" link will be clicked, leading the user to the account registration section.
* After steps 5-7: The correct registration email and password will be entered, and the registration button will be clicked. If there are no conflicts, such as an existing account with this email address, the registration should be successful.
* After step 8: The user will receive confirmation that the registration was successful.
* After step 9: The browser will be closed.

### Test 2
### Title: Checking if an error message appears when attempting to register without providing an email address.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/.
* Click the "Account" link.
* Enter the password.
* Click the registration button.
* Check if the registration was successful.
* Close the browser.

#### Expected Result:
After clicking the "Register" button, an error message should appear asking for an email address.

### Test 3
### Title: Checking if an error message appears when attempting to register without providing a password.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/.
* Click the "Account" link.
* Enter the registration email.
* Click the registration button.
* Check if the registration was successful.
* Close the browser.

#### Expected Result:
After clicking the "Register" button, an error message should appear asking for a password.

---

### ID: 002 Functional Tests for Login
### Test 1
### Title: Logging in and logging out a registered user using correct credentials.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Click the "Account" link.
* Enter the login credentials: user's email and password.
* Click the login button.
* Check if the user is successfully logged in.
* Click the logout button.
* Check if the user is successfully logged out.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ will open in the Chrome browser window.
* After step 4: The user will be redirected to the login section by clicking the "Account" link.
* After steps 5-6: The correct email and password will be entered, and the login button will be clicked. If the login credentials are correct, the user will be logged into their account.
* After step 7: The user will be able to verify successful login by displaying logged-in user information on the page.
* After step 8: The logout button will be clicked, causing the user to be logged out.
* After step 9: The user will be able to verify successful logout by the absence of logged-in user information on the page.
* After step 10: The browser window will be closed.

### Test 2
### Title: Checking if an error message appears when attempting to log in without providing an email/username.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Click the "Account" link.
* Enter the login credentials: password. Leave the email field empty.
* Click the login button.
* Check if the user is successfully logged in.
* Close the browser.

#### Expected Result:
After clicking the "Login" button, an error message should appear asking for an email/username.

### Test 3
### Title: Checking if an error message appears when attempting to log in with an incorrect email/username.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Click the "Account" link.
* Enter the login credentials: incorrect user email and correct password.
* Click the login button.
* Check if the user is successfully logged in.
* Close the browser.

#### Expected Result:
After clicking the "Login" button, an error message should appear asking for a correct username or email address.

### Test 4
### Title: Checking if an error message appears when attempting to log in without providing a password.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Click the "Account" link.
* Enter the login credentials: user's email. Leave the password field empty.
* Click the login button.
* Check if the user is successfully logged in.
* Close the browser.

#### Expected Result:
After clicking the "Login" button, an error message should appear asking for a password.

### Test 5
### Title: Checking if an error message appears when attempting to log in with an incorrect password.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Click the "Account" link.
* Enter the login credentials: correct user email and incorrect password.
* Click the login button.
* Check if the user is successfully logged in.
* Close the browser.

#### Expected Result:
After clicking the "Login" button, an error message should appear asking for the correct password.

---

### ID: 003 Functional Tests for Navigation
### Title: Navigation through different product categories and checking if clicking each subcategory displays the correct products.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/
* Locate and click the "Categories" link.
* Click on the individual subcategories: "All", "Shirts", "Featured", "Trends", "Scarfs", "Shoes", "Tops", "Blouses", "Jeans", "Dresses" and check if they direct the user to the appropriate page.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ will open in the Chrome browser window.
* After step 4: The user will locate and click the "Categories" link to navigate to the product categories.
* After step 5: The user will click on each subcategory and verify if they direct the user to the appropriate product pages.
* After step 6: The browser will be closed.

---

### ID: 004 Functional Tests for Product Sorting
### Title: Verify the functionality of the "Shirts" product sorting options.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/.
* Locate and click the "Categories" link.
* Click on the "Shirts" subcategory.
* Check default sorting:
  * Click the sorting element.
  * Ensure "Default sorting" is selected.
  * Compare the order of results with the expected order.
* Sort by popularity:
  * Click the sorting element.
  * Select "Sort by popularity".
  * Ensure the results are sorted by popularity.
* Sort by rating:
  * Click the sorting element.
  * Select "Sort by average rating".
  * Ensure the results are sorted by rating.
* Sort by newness:
  * Click the sorting element.
  * Select "Sort by newness".
  * Ensure the results are sorted by the date of addition, with the newest products at the top.
* Sort by price (low to high):
  * Click the sorting element.
  * Select "Sort by price: low to high".
  * Ensure the results are sorted by price, with the lowest prices at the top.
* Sort by price (high to low):
  * Click the sorting element.
  * Select "Sort by price: high to low".
  * Ensure the results are sorted by price, with the highest prices at the top.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl will open in the Chrome browser window.
* After step 4: The user will locate and click the "Categories" link.
* After step 5: The user will click the "Shirts" subcategory.
* After steps 6-11: If the test works correctly, the results should be displayed according to the selected sorting criteria. In the case of errors, error messages or incorrectly sorted results are expected, indicating an issue with the sorting functionality on the website.
* After step 12: The browser will be closed.

---

### ID: 005 Functional Tests for Adding Products to Cart
### Title: Verify if users can successfully add products to the cart.

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Navigate to the website: https://skleptest.pl/.
* Locate and click the "Categories" link.
* Select the "Shirts" subcategory.
* Sort products by popularity.
* Click the first displayed product.
* Locate and click the product quantity input field.
* Clear the quantity input field.
* Enter quantity 1.
* Click the "Add to cart" button.
* Return to the subcategory search options by clicking the "Categories" link.
* Click the "Scarfs" subcategory.
* Sort products by newness.
* Click the second displayed product.
* Locate and click the product quantity input field.
* Clear the quantity input field.
* Enter quantity 2.
* Locate and click the "My Cart" button.
* Close the browser.

#### Expected Result:
Users can add products to the cart from different subcategories. It is possible to add different quantities of products to the cart for each category. After adding products to the cart, users can check its contents by clicking the "My Cart" button. Ultimately, the expected result is full functionality of the product addition process to the cart.

---
