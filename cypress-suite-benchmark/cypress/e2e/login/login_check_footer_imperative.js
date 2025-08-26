import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user enters the valid login credentials username {string} and password {string}', (username, password) => {
  cy.get('[data-test="username"]').clear().type(username);
  cy.get('[data-test="password"]').clear().type(password);
});

When('the user clicks the Login button', () => {
  cy.get('[data-test="login-button"]').click();
});

Then('the inventory page should be displayed under {string}', (page) => {
  cy.url().should('contain', page);
});

When('the user scrolls to the footer on the bottom of the page', () => {
  cy.get('[data-test="footer"]').scrollIntoView();
});

Then('the social media icons for Twitter, Facebook, and LinkedIn should be visible in the footer with text {string}, {string} and {string}', (twitter, facebook, linkedin) => {
  cy.get('[data-test="social-twitter"]').should('be.visible').and('contain.text', twitter);
  cy.get('[data-test="social-facebook"]').should('be.visible').and('contain.text', facebook);
  cy.get('[data-test="social-linkedin"]').should('be.visible').and('contain.text', linkedin);
});

When('the user scrolls up to the menu and clicks on it', () => {
  cy.get('#react-burger-menu-btn').scrollIntoView();
  cy.get('#react-burger-menu-btn').click();
});

When('the user chooses to log out using the logout button in the sidebar', () => {
  cy.get('[data-test="logout-sidebar-link"]').click();
});

Then('the site should be {string} again', (page) => {
  cy.url().should('contain', page);
});