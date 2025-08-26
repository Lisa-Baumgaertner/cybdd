Feature: Search for tv show

  Scenario: User searches for a tv show
    Given the user visits the website "https://www.imdb.com/"
    When the user clicks on the search input field
    When the user types "<media>" into the search input
    When the user clicks the search button
    Then a results page should appear showing the tv show or media related to "<media>"

    Examples:
      | media                |
      | the office           |
      | arrested development |
      | seinfeld             |
