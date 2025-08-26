Feature: Full Cart Flow

  Scenario: User logs in, adds a product to the cart, removes it, and logs out
    Given the user visits the website "https://www.saucedemo.com/"
    When the user enters the username "standard_user" and password "secret_sauce"
    When the user clicks the Login button
    Then the inventory page should be displayed as "/inventory"
    When the user adds the first product to the cart
    When the user clicks the cart icon in the header
    Then the cart page should show the added product "Sauce Labs Backpack"
    When the user removes the product from the cart using the remove button
    Then the user clicks button Continue Shopping
    When the user opens the side menu to prepare logout
    When the user clicks the Logout button
    Then the user should be redirected to the login page containing "https://www.saucedemo.com/"
