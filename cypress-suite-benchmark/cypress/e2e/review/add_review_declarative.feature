Feature: Submit Product Review

  Scenario: Submit a product review successfully
    Given the user is on the website
    When the user navigates to the products page
    When the user views the details of a product
    When the user submits a review with name, email, and message
    Then a confirmation message should be displayed confirming the review
