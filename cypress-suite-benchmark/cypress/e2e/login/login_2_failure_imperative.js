import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user enters {string} into the username field', (username) => {
  cy.get('[id="user-name"]').type(username);
});

When('the user enters {string} into the password field', (password) => {
  cy.get('[id="password"]').type(password);
});

When('the user clicks the login button', () => {
  cy.get('[id="login-button"]').click();
});

Then('the error message should be visible', () => {
  cy.get('[class="error-message-container error"]').should('be.visible');

});
