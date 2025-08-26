Feature: Add Product with Specific Quantity to Cart

  Scenario: User adds a product with quantity 5 to the cart and verifies it
    Given the user visits the website
    When the user navigates to the product page
    When the user views the details of the first product
    When the user selects a quantity of 5 for the product
    When the user adds the product to the shopping cart
    Then the system should confirm that the product was added successfully
    When the user opens the shopping cart
    Then the cart should display the product with the correct quantity
