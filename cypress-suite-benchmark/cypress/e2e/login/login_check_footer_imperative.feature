Feature: Footer Social Media Icons

  Scenario: User logs in and verifies the social media icons in footer
    Given the user visits the website "https://www.saucedemo.com/"
    When the user enters the valid login credentials username "standard_user" and password "secret_sauce"
    When the user clicks the Login button
    Then the inventory page should be displayed under "/inventory"
    When the user scrolls to the footer on the bottom of the page
    Then the social media icons for Twitter, Facebook, and LinkedIn should be visible in the footer with text "Twitter", "Facebook" and "LinkedIn"
    When the user scrolls up to the menu and clicks on it 
    When the user chooses to log out using the logout button in the sidebar 
    Then the site should be "https://www.saucedemo.com/" again