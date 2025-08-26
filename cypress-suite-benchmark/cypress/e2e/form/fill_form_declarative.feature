Feature: Student Registration Form

  Scenario: Completing and submitting the registration form
    Given the user is on the website
    When the user fills out all required form fields
    When the user selects all checkbox and radio options as instructed
    When the user selects the appropriate dropdown option
    When the user submits the form
    Then the confirmation message should be displayed correctly
