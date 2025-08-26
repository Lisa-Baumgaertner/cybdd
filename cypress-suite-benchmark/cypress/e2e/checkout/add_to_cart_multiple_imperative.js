import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on the {string} button in the top navigation bar', () => {
  cy.get('[href="/products"]').click();
});

Then('the {string} page should be visible', (text) => {
  cy.url().should('contain', text);
});

When('the user clicks {string} button for the first product', () => {
  cy.get('[class="single-products"]').eq(0).find('[data-product-id="1"]:visible').click();
});

Then('a cart modal should appear with confirmation', () => {
  cy.get('[id="cartModal"]').should('be.visible');

});

When('the user clicks the {string} button on the modal', (text) => {
  cy.get('[id="cartModal"]').find('[class="btn btn-success close-modal btn-block"]').click();
});

Then('the user adds the second product by clicking the {string} button', (text) => {
  cy.get('[class="single-products"]').eq(1).find('[data-product-id="2"]:visible').click();
});

Then('the cart modal should appear again with confirmation', () => {
  cy.get('[id="cartModal"]').should('be.visible');
});

When('the user clicks the {string} button', (text) => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('both products should be visible in the cart with names {string} and {string}', (name_product_one, name_product_two) => {
  cy.get('[id="product-1"]').should('contain.text', name_product_one);
  cy.get('[id="product-2"]').should('contain.text', name_product_two);
});

