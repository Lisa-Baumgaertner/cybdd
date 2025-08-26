Feature: User Logout

  Scenario: Successful logout from the user account
    Given the user visits "https://www.saucedemo.com/" 
    When the user enters "standard_user" in the username field "secret_sauce" in the password field
    When the user clicks the Login button
    When the user clicks the burger menu button
    When the user clicks the Logout link from the sidebar menu
    Then the user should be redirected to the login page with "https://www.saucedemo.com/" and the login button should be visible