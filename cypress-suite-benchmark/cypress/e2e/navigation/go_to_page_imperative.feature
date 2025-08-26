Feature: Navigate to page

  Scenario: User navigates to the Test Cases page from the homepage
    Given visits the website "http://automationexercise.com"
    When the user chooses the li element with href "/test_cases" in top navigation 
    Then the user should be navigated to the Test Cases page successfully and see the text "Test Cases"
