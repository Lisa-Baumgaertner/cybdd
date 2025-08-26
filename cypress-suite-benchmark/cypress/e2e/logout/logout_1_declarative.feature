Feature: User Logout

  Scenario: Successful logout from the user account
    Given the user is logged in on the site
    When the user logs out
    Then the login page is displayed again
