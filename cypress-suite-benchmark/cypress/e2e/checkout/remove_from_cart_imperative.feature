Feature: Remove a Product from Cart

  Scenario: User removes a product from the cart
    Given the user visits the website "http://automationexercise.com"
    When the user clicks on the "Products" button in the top navigation
    Then the "/products" page should be visible
    When the user adds the first product to cart using button "Add to cart"
    Then a confirmation modal should appear
    When the user clicks the href in the modal
    Then the cart page should display the first product with name "Blue Top"
    When the user clicks the X button attached to the product in the cart
    Then the cart should be empty, indicated by text "Cart is empty!"
    




