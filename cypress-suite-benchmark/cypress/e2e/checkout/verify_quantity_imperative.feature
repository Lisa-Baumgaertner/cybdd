Feature: Add Product with Specific Quantity to Cart

  Scenario: User adds a product with quantity 5 to the cart and verifies it
    Given the user visits the website "http://automationexercise.com"
    When the user navigates to "/product" page
    When the user clicks the "View Product" button for the first product on the home page
    Then the product detail page should be displayed on page "/product_details/1"
    When the user sets the product quantity to 5
    When the user clicks on the "Add to cart" button
    Then a confirmation modal should appear
    When the user clicks the "View Cart" button
    Then the product should be displayed in the cart page with quantity 5
