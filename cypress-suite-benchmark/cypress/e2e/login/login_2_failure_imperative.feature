Feature: User Login

  Scenario: Login with invalid credentials
    Given the user visits "https://saucedemo.com"
    When the user enters "locked_out_user" into the username field
    When the user enters "secret_sauce" into the password field
    When the user clicks the login button
    Then the error message should be visible
