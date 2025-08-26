import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user enters {string} into the username field', (string) => {
   cy.get('[data-test="username"]').type(string);
});

When('the user enters {string} into the password field', (string) => {
  cy.get('[data-test="password"]').type(string);
 
});

When('the user clicks the login button', () => {
  cy.get('[data-test="login-button"]').click();
});

Then('the user should be redirected to the page {string}', (url) => {
  cy.url().should('include', url);
}); 