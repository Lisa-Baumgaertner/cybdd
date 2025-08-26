import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Automation Exercise home page', () => {
  cy.visit('https://automationexercise.com/');

});

Then('a clearly labeled link to the official YouTube video tutorials should be visible', () => {
  cy.get('a[href="https://www.youtube.com/c/AutomationExercise"]').should('contain.text', 'Video Tutorials').and('be.visible');
 
});

Then('the link should direct users to the official YouTube channel', () => {
  cy.contains('Video Tutorials')
    .should('have.attr', 'href')
    .and('include', 'https://www.youtube.com/c/AutomationExercise');
 
});
