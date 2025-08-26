import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on the {string} button in the top navigation', (text) => {
  cy.get('[href="/products"]').click();
});

Then('the {string} page should be visible', (text) => {
  cy.url().should('contain', text);
});

When('the user adds the first product to cart using button {string}', (text) => {
  cy.get('[class="single-products"]').eq(0).find('[data-product-id="1"]:visible').click();
});

Then('a confirmation modal should appear', () => {
  cy.get('[id="cartModal"]').should('be.visible');

});

When('the user clicks the href in the modal', (text) => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('the cart page should display the first product wih name {string}', (text) => {
  cy.get('[class="cart_description"]').find('h4').should('contain.text', text);
});

