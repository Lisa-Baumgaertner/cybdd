import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('https://saucedemo.com');
});

When('the user submits valid login information', () => {
   cy.get('[data-test="username"]').type('standard_user');
   cy.get('[data-test="password"]').type('secret_sauce');
   cy.get('[data-test="login-button"]').click();
});

Then('the user should be redirected to the inventory page', () => {
  cy.url().should('include', '/inventory');
}); 