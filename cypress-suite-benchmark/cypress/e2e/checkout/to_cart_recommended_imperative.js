import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user scrolls down to {string} slider', (text) => {
  cy.get('[class="recommended_items"]').scrollIntoView();
});

Then('the {string} section should be visible', (text) => {
  cy.get('[class="recommended_items"]').find('h2').should('contain.text', text);
});

When('the user clicks {string} button on the first visible recommended product', (text) => {
  cy.get('[id="recommended-item-carousel"]').find('a.add-to-cart:visible').first().click();

});

Then('the user clicks the {string} button', (text) => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();
});

Then('the product with name {string} should be visible on the cart page in the cart description', (text) => {
  cy.get('[class="cart_description"]').find('h4').should('contain.text', text);
});
