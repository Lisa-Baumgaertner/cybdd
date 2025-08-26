import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user enters {string} into the username field', (username) => {
  cy.get('[data-test="username"]').type(username);
});

When('the user enters {string} into the password field', (password) => {
  cy.get('[data-test="password"]').type(password);
});

When('the user clicks the login button', () => {
  cy.get('[data-test="login-button"]').click();
});

Then('the error message should be visible', () => {
  cy.get('[data-test="error"]').should('be.visible');
});
