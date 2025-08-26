Feature: Contact Form Submission

  Scenario: User submits a contact form successfully from contact page 
    Given the user is on the homepage
    When the user navigates to the contact page
    When the user provides valid contact details and a message about an order issue
    When the user submits the contact form
    Then the message should be displayed, that the form was sent successfully
