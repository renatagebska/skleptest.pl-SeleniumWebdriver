# skleptest.pl-SeleniumWebdriver
## Automation of Test Cases using Selenium Webdriver

## Test Cases


### ID: 001
### Title: Registering a new user using new registration data.

##### Environment: Chrome version 124.0.6367.60, Windows 11

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Go to the website: https://skleptest.pl/.
* Click the "Account" link.
* Enter the registration email.
* Enter the password.
* Click the registration button.
* Check if the registration was successful.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ opens in the Chrome browser window.
* After step 4: The "Account" link is clicked, leading the user to the account registration section.
* After steps 5-7: The correct registration email and password are entered, and then the registration button is clicked. If there are no conflicts, such as an existing account with this email address, the registration should be successful.
* After step 8: The user receives confirmation that the registration was successful.
* After step 9: The browser is closed.
---


### ID: 002
### Title: Logging in and logging out a registered user using correct data.

##### Environment: Chrome version 124.0.6367.60, Windows 11

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Go to the website: https://skleptest.pl/.
* Click the "Account" link.
* Enter login credentials: user email and password.
* Click the login button.
* Check if the user is successfully logged in.
* Click the logout button.
* Check if the user has been successfully logged out.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ opens in the Chrome browser window.
* After step 4: The user is redirected to the login section by clicking the "Account" link.
* After steps 5-6: The correct email address and password are entered, and then the login button is clicked. If the login data is correct, the user will be logged into their account.
* After step 7: The user can verify if they are successfully logged in by displaying information about the logged-in user on the page.
* After step 8: The logout button is clicked, resulting in the user being logged out of the account.
* After step 9: The user can verify if they have been successfully logged out, for example, by the absence of information about the logged-in user on the page.
* After step 10: The browser is closed.
---


### ID: 003
### Title: Navigating through different product categories and checking if clicking each subcategory displays the correct products.

##### Environment: Chrome version 124.0.6367.60, Windows 11

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Go to the website: https://skleptest.pl/.
* Locate and go to the "Categories" link.
* Click on each subcategory: "All", "Shirts", "Featured", "Trends", "Scarfs", "Shoes", "Tops", "Blouses", "Jeans", "Dresses", and check if they lead the user to the correct product page.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl/ opens in the Chrome browser window.
* After step 4: The user locates and clicks the "Categories" link to go to the product categories.
* After step 5: The user clicks on each subcategory and verifies if they are redirected to the correct product pages.
* After step 6: The browser is closed.
---


### ID: 004
### Title: Checking the correctness of the "Shirts" product sorting options.

##### Environment: Chrome version 124.0.6367.60, Windows 11

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Go to the website: https://skleptest.pl/.
* Locate and go to the "Categories" link.
* Click on the "Shirts" subcategory.
* Check the default sorting:
* Click on the sorting element.
* Make sure "Default sorting" is selected.
* Compare the order of results with the expected order.
* Sort by popularity:
* Click on the sorting element.
* Select the "Sort by popularity" option.
* Make sure the results are sorted by popularity.
* Sort by rating:
* Click on the sorting element.
* Select the "Sort by average rating" option.
* Make sure the results are sorted by product rating.
* Sort by newest:
* Click on the sorting element.
* Select the "Sort by newness" option.
* Make sure the results are sorted by product addition date, with the newest products at the beginning.
* Sort by price (lowest to highest):
* Click on the sorting element.
* Select the "Sort by price: low to high" option.
* Make sure the results are sorted by price, with the lowest prices at the beginning.
* Sort by price (highest to lowest):
* Click on the sorting element.
* Select the "Sort by price: high to low" option.
* Make sure the results are sorted by price, with the highest prices at the beginning.
* Close the browser.

#### Expected Result:
* After steps 1-3: The website https://skleptest.pl opens in the Chrome browser window.
* After step 4: The user locates and goes to the "Categories" link.
* After step 5: The user clicks on the "Shirts" subcategory.
* After steps 6-11: In case of successful test execution, the results should be displayed according to the selected sorting criterion. In case of errors, error messages or incorrectly sorted results are expected, indicating a problem with the sorting functionality on the website.
* After step 12: The browser is closed.
---


### ID: 005
### Title: Checking if users can successfully add products to the cart.

##### Environment: Chrome version 124.0.6367.60, Windows 11

#### Steps:
* Open the Chrome browser.
* Maximize the window.
* Go to the website: https://skleptest.pl/.
* Locate and go to the "Categories" link.
* Select the "Shirts" subcategory.
* Sort the products by popularity.
* Click on the first displayed product.
* Locate and click on the product quantity input field.
* Clear the product quantity input field.
* Enter a quantity of 1.
* Click on the "Add to cart" button.
* Return to the subcategory selection options by clicking on the "Categories" link.
* Click on the "Scarfs" subcategory.
* Sort the products by newest.
* Click on the second displayed product.
* Locate and click on the product quantity input field.
* Clear the product quantity input field.
* Enter a quantity of 2.
* Locate and click the "My Cart" buttons.
* Close the browser.

#### Expected Result: 
* Users can add products to the cart from different subcategories. It is possible to add different quantities of products to the cart for each category. After adding products to the cart, users can check its contents by clicking on the "My Cart" button. Ultimately, the expected result is the full functionality of the process of adding products to the cart.
---
