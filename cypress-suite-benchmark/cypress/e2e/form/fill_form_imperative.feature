Feature: Student Registration Form

  Scenario: Filling out and submitting the student form
    Given the user visits the website "https://testpages.eviltester.com/styled/basic-html-form-test.html"
    When the user enters "JaneDoe" into the username field
    When the user enters "password123" into the password field
    When the user enters "Hello world!" into the textarea comment field
    When the user clicks all three checkbox items with the values cb1, cb2 and cb3
    When the user clicks radio item 3
    When the user selects Drop Down Item 2 
    When the user submits the form using ths submit button 
    Then the text "You submitted a form. The details below show the values you entered for processing." should be contained
