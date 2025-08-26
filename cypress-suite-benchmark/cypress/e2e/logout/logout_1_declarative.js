import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is logged in on the site', () => {
  cy.visit('https://www.saucedemo.com/');
  cy.get('[data-test="username"]').type('standard_user');
  cy.get('[data-test="password"]').type('secret_sauce');
  cy.get('[data-test="login-button"]').click();
});

When('the user logs out', () => {
  cy.get('[id="react-burger-menu-btn"]').click();
  cy.get('[data-test="logout-sidebar-link"]').click();
});

Then('the login page is displayed again', () => {
  cy.url().should("include", "saucedemo.com");
  cy.get("#login-button").should("be.visible");
});
