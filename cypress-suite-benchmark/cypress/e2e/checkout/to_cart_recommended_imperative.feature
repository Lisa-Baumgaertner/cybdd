Feature: Add Product to Cart From Recommended Slider

  Scenario: User adds a recommended item to the cart and verifies correctness
    Given the user visits the website "http://automationexercise.com"
    When the user scrolls down to "recommended items" slider
    Then the "recommended items" section should be visible
    When the user clicks "Add To Cart" button on the first visible recommended product
    Then the user clicks the "View Cart" button
    Then the product with name "Stylish Dress" should be visible on the cart page in the cart description
