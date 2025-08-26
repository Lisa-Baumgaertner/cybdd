import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
  
});

When('the user enters {string} in the username field {string} in the password field', (username, password) => {
  cy.get('[data-test="username"]').type(username);
  cy.get('[data-test="password"]').type(password);
})

When('the user clicks the Login button', () => {
  cy.get('[data-test="login-button"]').click();
})

When('the user clicks the burger menu button', () => {
  cy.get('[id="react-burger-menu-btn"]').click();
})

When('the user clicks the Logout link from the sidebar menu', () => {
  cy.get('[data-test="logout-sidebar-link"]').click();
});

Then('the user should be redirected to the login page with {string} and the login button should be visible', (url) => {
  cy.url().should("include", url);
  cy.get("#login-button").should("be.visible");
});
