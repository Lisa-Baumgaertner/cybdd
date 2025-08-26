Feature: Scroll to Bottom and Return to Top of the page

  Scenario: User scrolls down and navigates back to the top of the page using the arrow
    Given the user visits the website "http://automationexercise.com"
    Then the home page should be visible with text "Full-Fledged practice website for Automation Engineers"
    When the user scrolls down to the footer of the page
    Then the "Subscription" section should be visible
    When the user clicks the arrow at the bottom-right corner of the page
    Then the text "Full-Fledged practice website for Automation Engineers" should be visible
