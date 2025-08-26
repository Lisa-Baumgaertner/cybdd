import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website {string}', (url) => {
  cy.visit(url);

});

Then('the link should be visible in the top navigation and have text {string}, verify this by using the href attribute', (text) => {
  cy.get('a[href="https://www.youtube.com/c/AutomationExercise"]').should('contain.text', text).and('be.visible');
 
});

Then('the link should point to a valid YouTube URL that should include {string}', (text) => {
  cy.contains('Video Tutorials')
    .should('have.attr', 'href')
    .and('include', text);
 
});
