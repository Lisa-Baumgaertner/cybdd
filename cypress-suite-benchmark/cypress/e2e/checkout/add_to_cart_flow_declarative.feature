Feature: Full Cart Flow

  Scenario: User logs in, adds a product to the cart, removes it, and logs out
    Given the user visits the website
    When the user logs in with valid credentials
    When the user adds a product to the shopping cart
    When the user navigates to cart
    Then the cart should display the selected product
    When the user removes the product from the cart
    When the user chooses to continue shopping
    When the user logs out
    Then the user should be returned to the login page



