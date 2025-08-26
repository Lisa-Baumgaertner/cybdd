Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user is on the website
    When the user submits valid login information
    Then the user should be redirected to the inventory page
