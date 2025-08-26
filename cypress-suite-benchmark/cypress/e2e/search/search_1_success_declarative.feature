Feature: Keyword Search

  Scenario: User searches for a valid keyword
    Given the user is on the homepage
    When a search is performed for the given search term
    Then the results page should show the heading including the search term
