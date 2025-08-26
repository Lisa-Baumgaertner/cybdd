import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user navigates to {string} page', (text) => {
  cy.get('[href="/products"]').click();
  cy.url().should('contain', text);
});

When('the user clicks the "View Product" button for the first product on the home page', () => {
  cy.get('[href="/product_details/1"]').click();
});

Then('the product detail page should be displayed on page {string}', (text) => {
  cy.url().should('contain', text);

});

When('the user sets the product quantity to 5', () => {
  cy.get('[id="quantity"]').clear().type('5');
});

When('the user clicks on the {string} button', (text) => {
  cy.get('[class="btn btn-default cart"]').should('contain.text', text).click();
});

Then('a confirmation modal should appear', () => {
  cy.get('[id="cartModal"]').should('be.visible');

});

When('the user clicks the {string} button', (text) => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('the product should be displayed in the cart page with quantity 5', () => {
  cy.get('[class="cart_quantity"]').should('contain.text', '5');

});