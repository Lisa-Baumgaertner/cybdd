Feature: Add Product to Cart From Recommended Slider

  Scenario: User adds a recommended item to the cart and verifies correctness
    Given the user is on the Automation Exercise home page
    When the user goes to the recommended products section
    Then adds the first visible recommended product to the shopping cart
    Then the user should be able to view the shopping cart
    Then the cart should display the correct product details 
