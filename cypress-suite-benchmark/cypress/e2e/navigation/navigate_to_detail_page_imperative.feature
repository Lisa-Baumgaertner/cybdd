Feature: Navigating to detail page from search

  Scenario: User searches for a movie and goes to its detail page
    Given the user visits the website "https://www.imdb.com/"
    When the user clicks on the search bar 
    When the user types "Inception" into the search input and presses Enter to submit
    When the user clicks on the first result
    Then the Inception movie detail page should be displayed with title "Inception" 
