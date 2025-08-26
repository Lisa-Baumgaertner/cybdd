import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user navigates to product page', () => {
  cy.get('[href="/products"]').click();
  cy.url().should('contain', '/products');
});

When('the user selects the first available product to add to the cart', () => {
  cy.get('[class="single-products"]').eq(0).find('[data-product-id="1"]:visible').click();
});

Then('the system should confirm that the product has been added', () => {
  cy.get('[id="cartModal"]').should('be.visible');
});

When('the user continues shopping', () => {
  cy.get('[id="cartModal"]').find('[class="btn btn-success close-modal btn-block"]').click();
});

When('the user selects the second available product', () => {
  cy.get('[class="single-products"]').eq(1).find('[data-product-id="2"]:visible').click();
});

Then('the system should confirm that the product has also been added', () => {
  cy.get('[id="cartModal"]').should('be.visible');
});

When('the user proceeds to view the shopping cart', () => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('the cart should display the correct selected product', () => {
  cy.get('[id="product-1"]').should('contain.text', 'Blue Top');
  cy.get('[id="product-2"]').should('contain.text', 'Men Tshirt');
});



