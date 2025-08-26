import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user navigates to the product page', () => {
  cy.get('[href="/products"]').click();
  cy.url().should('contain', '/products');
});

When('the user views the details of the first product', () => {
  cy.get('[href="/product_details/1"]').click();
});

When('the user selects a quantity of 5 for the product', () => {
  cy.get('[id="quantity"]').clear().type('5');
});

When('the user adds the product to the shopping cart', () => {
  cy.get('[class="btn btn-default cart"]').should('contain.text', "Add to cart").click();
});

Then('the system should confirm that the product was added successfully', () => {
  cy.get('[id="cartModal"]').should('be.visible');
});

When('the user opens the shopping cart', () => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('the cart should display the product with the correct quantity', () => {
  cy.get('[class="cart_quantity"]').should('contain.text', '5');
});

