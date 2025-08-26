Feature: Search for non-existent item

  Scenario: Searching for a non-existent topic
    Given the user visits the page "https://en.wikipedia.org/"
    When the user clicks on the search button and chooses the first one
    When the user clicks on the search bar and chooses the first one
    When the user enters the search term "nonexistent12345678"
    When the user clicks the search button and chooses the first one
    Then the system informs the user with "There were no results matching the query"