import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user enters {string} into the username field', (string) => {
   cy.get('[id="user-name"]').type(string);
});

When('the user enters {string} into the password field', (string) => {
  cy.get('[id="password"]').type(string);
 
});

When('the user clicks the login button', () => {
  cy.get('[id="login-button"]').click();
});

Then('the user should be redirected to the page {string}', (url) => {
  cy.url().should('include', url);
}); 