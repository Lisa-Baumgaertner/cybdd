Feature: Contact Form Submission

  Scenario: User submits a contact form successfully from contact page 
    Given the user visits "https://automationexercise.com/contact_us"
    Then the contact form should be visible
    When the user enters their name "Janet Doe", email address "janetdoe@test.com", subject "Problem with my order", and message "My order has not been shipped."
    When the user clicks the Submit button
    Then the message "Success! Your details have been submitted successfully." should be displayed
