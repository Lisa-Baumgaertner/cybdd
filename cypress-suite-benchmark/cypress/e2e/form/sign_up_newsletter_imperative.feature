Feature: Newsletter Signup 

  Scenario: User subscribes to newsletter in footer
    Given the user visits "https://automationexercise.com"
    When the user scrolls down to footer 
    When the user types "testuser@example.com" into the subscription input
    When the user clicks the subscribe button
    Then the success message "You have been successfully subscribed!" should be visible
