Feature: Newsletter Subscription from Cart Page

  Scenario: User subscribes to the newsletter from the cart page
    Given the user is on the website 
    When the user navigates to cart page 
    When the user navigates to subscription 
    When the user provides a valid email address for newsletter subscription
    When the user submits the subscription form
    Then the system should confirm successful subscription with a message
