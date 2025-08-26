import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user enters the username {string} and password {string}', (username, password) => {
  cy.get('[data-test="username"]').clear().type(username);
  cy.get('[data-test="password"]').clear().type(password);
});

When('the user clicks the Login button', () => {
  cy.get('[data-test="login-button"]').click();
});

Then('the inventory page should be displayed as {string}', (page) => {
  cy.url().should('contain', page);
});

When('the user adds the first product to the cart', () => {
  cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
});

When('the user clicks the cart icon in the header', () => {
  cy.get('[data-test="shopping-cart-link"]').click();
 
});

Then('the cart page should show the added product {string}', (product) => {
  cy.get('[data-test="inventory-item-name"]').should('contain.text', product);
});

When('the user removes the product from the cart using the remove button', () => {
  cy.get('[data-test="remove-sauce-labs-backpack"]').click();
});

Then('the user clicks button Continue Shopping', () => {
  cy.get('[data-test="continue-shopping"]').click(); 
});

When('the user opens the side menu to prepare logout', () => {
  cy.get('#react-burger-menu-btn').click();
});

When('the user clicks the Logout button', () => {
  cy.get('[data-test="logout-sidebar-link"]').should('be.visible').click();
});

Then('the user should be redirected to the login page containing {string}', (url) => {
  cy.url().should('contain', url)
  
});