import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the product detail page is displayed on page {string}', (page) => {
  cy.url().should('contain', page);
});

Then('the product image should be visible', () => {
  cy.get('img[src="/get_product_picture/1"]').should('be.visible');
});

Then('the product name {string} should be visible', (name) => {
  cy.get('[class="product-information"]').find('h2').should('contain.text', name);
});

Then('the product category {string} should be visible', (category) => {
  cy.get('[class="product-information"]').find('p').should('contain.text', category);
});

Then('the product price {string} should be visible', (price) => {
  cy.get('[class="product-information"]').find('span').should('contain.text', price);
});

Then('the product availability {string} should be visible', (availability) => {
  cy.get('[class="product-information"]').find('p').should('contain.text', availability);
});

Then('the product condition {string} should be visible', (condition) => {
  cy.get('[class="product-information"]').find('p').should('contain.text', condition);
});

Then('the product brand {string} should be visible', (brand) => {
  cy.get('[class="product-information"]').find('p').should('contain.text', brand);
});
