Feature: Navigating to detail page from search

  Scenario: User searches for a movie and goes to its detail page
    Given the user visits the website
    When the user performs a movie search
    When the user selects the first search result
    Then the correct movie detail page should be shown
