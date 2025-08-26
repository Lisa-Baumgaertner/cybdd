Feature: Product Detail Page Check 

  Scenario: Verify details are displayed correctly on the detail page
    Given the user visits "https://automationexercise.com/product_details/1"
    When the product detail page is displayed on page "/product_details/1"
    Then the product image should be visible
    Then the product name "Blue Top" should be visible
    Then the product category "Women > Tops" should be visible
    Then the product price "Rs. 500" should be visible
    Then the product availability "In Stock" should be visible
    Then the product condition "New" should be visible
    Then the product brand "Polo" should be visible
