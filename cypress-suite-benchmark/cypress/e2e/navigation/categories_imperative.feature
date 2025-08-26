Feature: Category Navigation

  Scenario: User navigates to Regenjacken product list
    Given the user visits the website "https://www.bergfreunde.de/"
    When the user clicks the "Bekleidung" category in the top bar navigation
    When the user clicks on "Jacken" and makes sure to choose the first
    When then clicks on item with title "Regenjacken" and makes sure to choose the first 
    Then the product list page should be displayed with title "Regenjacken"
