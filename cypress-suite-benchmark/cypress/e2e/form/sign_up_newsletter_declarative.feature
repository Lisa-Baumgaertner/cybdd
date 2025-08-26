Feature: Newsletter Signup

  Scenario: User subscribes to newsletter in footer
    Given the user is on the Automation Exercise website
    When the user subscribes to the newsletter with a valid email address
    Then a success message confirming the subscription should be visible
