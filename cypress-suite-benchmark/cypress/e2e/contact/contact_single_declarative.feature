Feature: Contact Form Submission

  Scenario: User submits a contact form successfully from contact page 
    Given the user is on the contact page 
    When the user provides valid contact information and a message
    When the user submits the contact form
    Then the system should confirm that the contact message was sent successfully