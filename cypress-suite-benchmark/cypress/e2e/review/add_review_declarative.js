import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('http://automationexercise.com');
});

When('the user navigates to the products page', () => {
  cy.get('a[href="/products"]').should('contain.text', 'Products').click();
});

When('the user views the details of a product', () => {
  cy.get('a[href="/product_details/1"]').click();
});

When('the user submits a review with name, email, and message', () => {
  cy.get('input[id="name"]').clear().type('Tester');
  cy.get('input[id="email"]').clear().type('test@test.com');
  cy.get('[id="review"]').clear().type('Good product');

});

Then('a confirmation message should be displayed confirming the review', () => {
  cy.get('[class="alert-success alert"]').should('contain.text', 'Thank you for your review.');
});
