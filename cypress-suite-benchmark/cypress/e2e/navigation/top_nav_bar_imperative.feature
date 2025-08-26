Feature: Top Navigation Bar

  Scenario: User verifies that all key navigation links are visible in the top bar in correct order
    Given the user visits the website "https://automationexercise.com/"
    When the user checks the number of items in the top navigation bar and makes sure it is "8"
    Then the navigation bar should include texts for "Home", "Products", "Cart", "Signup / Login", "Test Cases", "API Testing", "Video Tutorials", and "Contact us"
