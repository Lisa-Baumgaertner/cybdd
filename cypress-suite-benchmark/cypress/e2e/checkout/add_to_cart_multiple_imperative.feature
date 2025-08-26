Feature: Add Multiple (Two) Products to Cart and Verify

  Scenario: User adds two products to the cart and verifies the details
    Given the user visits the website "http://automationexercise.com"
    When the user clicks on the "Products" button in the top navigation bar
    Then the "/products" page should be visible
    When the user clicks "Add to cart" button for the first product
    Then a cart modal should appear with confirmation
    When the user clicks the "Continue Shopping" button on the modal
    Then the user adds the second product by clicking the "Add to cart" button
    Then the cart modal should appear again with confirmation
    When the user clicks the "View Cart" button
    Then both products should be visible in the cart with names "Blue Top" and "Men Tshirt"
    
