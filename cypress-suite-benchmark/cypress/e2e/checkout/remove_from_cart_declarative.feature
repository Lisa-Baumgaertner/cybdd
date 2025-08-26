Feature: Remove a Product from Cart

  Scenario: User removes a product from the cart
    Given the user is on the website
    When the user navigates to product page
    When the user selects the first available product to add to the cart
    Then the system should confirm that the product has been added
    When the user proceeds to view the shopping cart
    Then the cart should display the correct selected product 
    When the user removes the product from cart
    Then the cart should be empty
