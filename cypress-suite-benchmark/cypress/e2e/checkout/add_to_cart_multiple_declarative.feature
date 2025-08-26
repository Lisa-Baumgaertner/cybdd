Feature: Add Multiple (Two) Products to Cart and Verify

  Scenario: User adds two products to the cart and verifies the details
    Given the user is on the website
    When the user navigates to product page
    When the user selects the first available product to add to the cart
    Then the system should confirm that the product has been added
    When the user continues shopping
    When the user selects the second available product
    Then the system should confirm that the product has also been added
    When the user proceeds to view the shopping cart
    Then the cart should display the correct selected product 

    
