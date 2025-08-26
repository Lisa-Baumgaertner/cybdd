import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user on the website', () => {
  cy.visit('https://www.saucedemo.com/');
});

When('the user enters valid credentials and logs in', () => {
  cy.get('[data-test="username"]').clear().type('standard_user');
  cy.get('[data-test="password"]').clear().type('secret_sauce');
  cy.get('[data-test="login-button"]').click();
});

Then('the inventory page should be visible', () => {
  cy.url().should('contain', '/inventory');
});

When('the user navigates to footer, the social icons should be present', () => {
  cy.get('[data-test="footer"]').scrollIntoView();
  cy.get('[data-test="social-twitter"]').should('be.visible').and('contain.text', 'Twitter');
  cy.get('[data-test="social-facebook"]').should('be.visible').and('contain.text', 'Facebook');
  cy.get('[data-test="social-linkedin"]').should('be.visible').and('contain.text', 'LinkedIn');
});

When('the user chooses to log out from the menu', () => {
  cy.get('#react-burger-menu-btn').scrollIntoView();
  cy.get('#react-burger-menu-btn').click();
  cy.get('[data-test="logout-sidebar-link"]').click();
});

Then('the user should be redirected back to the login page', () => {
  cy.url().should('contain', 'https://www.saucedemo.com/');
});

