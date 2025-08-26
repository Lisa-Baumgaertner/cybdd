Feature: Navigation to Video Tutorials on Youtube 

 Scenario: User verifies the Video Tutorials link points to YouTube
    Given the user is on the website "https://automationexercise.com"
    Then the link should be visible in the top navigation and have text "Video Tutorials", verify this by using the href attribute 
    Then the link should point to a valid YouTube URL that should include "youtube.com/c/AutomationExercise"
    
