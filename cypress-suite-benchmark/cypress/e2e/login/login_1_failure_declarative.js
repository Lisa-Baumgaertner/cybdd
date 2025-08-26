import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://saucedemo.com');
});

When('the user fills out the login form and submits it', () => {
  cy.get('[data-test="username"]').type('locked_out_user');
  cy.get('[data-test="password"]').type('secret_sauce');
  cy.get('[data-test="login-button"]').click();
});

Then('the error message should be shown to the user', () => {
  cy.get('[data-test="error"]').should('be.visible');
});
