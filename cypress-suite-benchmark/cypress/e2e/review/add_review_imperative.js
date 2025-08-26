import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the site {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on the {string} button in top navigation bar', (product) => {
  cy.get('a[href="/products"]').should('contain.text', product).click();
});

Then('the user should be navigated to the {string} page', (page) => {
  cy.url().should('contain', page);
});

When('the user clicks on the {string} button for the first product', (button) => {
  cy.get('a[href="/product_details/1"]').click();
});

Then('the {string} section should be visible', (text) => {
  cy.get('a[href="#reviews"]').should('be.visible');
});

When('the user enters the name {string}, the email address {string}, and the review text {string}', (name, email, review) => {
  cy.get('input[id="name"]').clear().type(name);
  cy.get('input[id="email"]').clear().type(email);
  cy.get('[id="review"]').clear().type(review);

});

When('the user clicks the {string} button', (text) => {
  cy.get('button[id="button-review"]').click();
});

Then('the success message {string} should be displayed', (review) => {
  cy.get('[class="alert-success alert"]').should('contain.text', review);
});
