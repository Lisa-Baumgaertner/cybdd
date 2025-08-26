Feature: User Login

  Scenario: Login with invalid credentials
    Given the user visits the website
    When the user fills out the login form and submits it
    Then the error message should be shown to the user
