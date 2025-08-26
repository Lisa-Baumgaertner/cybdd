Feature: Submit Product Review

  Scenario: Submit a product review successfully
    Given the user visits the site "http://automationexercise.com"
    When the user clicks on the "Products" button in top navigation bar
    Then the user should be navigated to the "/products" page
    When the user clicks on the "View Product" button for the first product
    Then the "Write Your Review" section should be visible
    When the user enters the name "Tester", the email address "test@test.com", and the review text "Good product"
    When the user clicks the "Submit" button
    Then the success message "Thank you for your review." should be displayed
