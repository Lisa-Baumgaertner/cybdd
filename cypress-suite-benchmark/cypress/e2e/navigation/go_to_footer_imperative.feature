Feature: Footer Social Media Icons

  Scenario: Footer includes social media icons
    Given the user visits the website "https://www.bergfreunde.de/"
    When the user scrolls down to the footer
    Then the icons for instagram, youtube and podcast should be visible
