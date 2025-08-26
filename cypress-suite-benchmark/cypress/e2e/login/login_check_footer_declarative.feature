Feature: Footer Social Media Icons

  Scenario: User logs in and verifies the social media icons in footer
    Given the user on the website
    When the user enters valid credentials and logs in
    Then the inventory page should be visible
    When the user navigates to footer, the social icons should be present
    When the user chooses to log out from the menu
    Then the user should be redirected back to the login page




