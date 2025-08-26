import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://www.saucedemo.com/');
});

When('the user logs in with valid credentials', () => {
  cy.get('[data-test="username"]').clear().type('standard_user');
  cy.get('[data-test="password"]').clear().type('secret_sauce');
  cy.get('[data-test="login-button"]').click();
});

When('the user adds a product to the shopping cart', () => {
  cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
});

When('the user navigates to cart', () => {
  cy.get('[data-test="shopping-cart-link"]').click();
});

Then('the cart should display the selected product', () => {
  cy.get('[data-test="inventory-item-name"]').should('contain.text', 'Sauce Labs Backpack');
 
});

When('the user removes the product from the cart', () => {
  cy.get('[data-test="remove-sauce-labs-backpack"]').click();
});

When('the user chooses to continue shopping', () => {
  cy.get('[data-test="continue-shopping"]').click(); 
});

When('the user logs out', () => {
  cy.get('#react-burger-menu-btn').click();
  cy.get('[data-test="logout-sidebar-link"]').should('be.visible').click();
});

Then('the user should be returned to the login page', () => {
  cy.url().should('contain', 'https://www.saucedemo.com/')
});

