Feature: User Account Registration

  Scenario: User creates a new account with valid information
    Given the user visits "https://opencart.abstracta.us/"
    When the user clicks on "My Account" in the top bar
    When selects "Register" from the dropdown
    When enters valid details including:
      | First Name   | John     |
      | Last Name    | Doe      |
      | Email        | john123@example.com |
      | Telephone    | 1234567890 |
      | Password     | Password123 |
    When confirms the password
    When agrees to the Privacy Policy
    When submits the form
    Then the user should see a message "Your Account Has Been Created!"
