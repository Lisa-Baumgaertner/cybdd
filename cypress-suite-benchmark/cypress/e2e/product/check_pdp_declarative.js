import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the product detail page', (url) => {
  cy.visit('https://automationexercise.com/product_details/1');
  cy.url().should('contain', '/product_details/1');

});

Then('the page should display the correct product information', () => {
  cy.get('img[src="/get_product_picture/1"]').should('be.visible');
  cy.get('[class="product-information"]').find('h2').should('contain.text', "Blue Top");
  cy.get('[class="product-information"]').find('p').should('contain.text', "Women > Tops");
  cy.get('[class="product-information"]').find('span').should('contain.text', "Rs. 500");
  cy.get('[class="product-information"]').find('p').should('contain.text', "In Stock");
  cy.get('[class="product-information"]').find('p').should('contain.text', "New");
  cy.get('[class="product-information"]').find('p').should('contain.text', "Polo");
});
