Feature: Scroll to Bottom and Return to Top of the page

  Scenario: User scrolls down and navigates back to the top of the page using the arrow
    Given the user visits the website
    When the user scrolls down to the bottom of the page
    Then the subscription section should be visible
    When the user chooses to return to the top
    Then the homepage headline should be visible
