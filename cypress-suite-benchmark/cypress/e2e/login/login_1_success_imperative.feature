Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user visits "https://saucedemo.com"
    When the user enters "standard_user" into the username field
    When the user enters "secret_sauce" into the password field
    When the user clicks the login button
    Then the user should be redirected to the page "/inventory"