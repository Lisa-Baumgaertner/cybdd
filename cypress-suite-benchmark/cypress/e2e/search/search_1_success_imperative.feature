Feature: Keyword Search

  Scenario: User searches for a valid keyword
    Given the user visits the site "https://opencart.abstracta.us"
    When the user types "MacBook" into the search bar
    When the user clicks the search button
    Then the text "Search - MacBook" should be displayed
