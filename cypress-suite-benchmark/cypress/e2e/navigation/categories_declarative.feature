Feature: Category Navigation

  Scenario: Navigating to the Regenjacken product list
    Given the user is on the Bergfreunde website
    When the user navigates through categories to "Regenjacken"
    Then the product listing page titled "Regenjacken" should be displayed
