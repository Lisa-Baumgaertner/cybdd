Feature: Newsletter Subscription from Cart Page

  Scenario: User subscribes to the newsletter from the cart page
    Given the user visits the website "http://automationexercise.com"
    When the user clicks the "Cart" button
    Then the cart page should be displayed on "/view_cart"
    When the user scrolls down to the footer section
    Then the text "Subscription" should be visible
    When the user enters the valid email address "test@tes.com" into the subscription input field
    When the user clicks the subscription arrow button
    Then a success message "You have been successfully subscribed!" should be visible
