Feature: Search for non-existent item

  Scenario: Searching for a non-existent topic
    Given the user is on the Wikipedia homepage
    When a search is performed for the search term 
    Then the system should inform the user that no results were found