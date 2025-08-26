import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Automation Exercise home page', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user goes to the recommended products section', () => {
  cy.get('[class="recommended_items"]').scrollIntoView();
  cy.get('[class="recommended_items"]').find('h2').should('contain.text', 'recommended items');
});

Then('adds the first visible recommended product to the shopping cart', () => {
  cy.get('[id="recommended-item-carousel"]').find('a.add-to-cart:visible').first().click();
});

Then('the user should be able to view the shopping cart', () => {
  cy.get('[id="cartModal"]').find('[href="/view_cart"]').click();

});

Then('the cart should display the correct product details', () => {
  cy.get('[class="cart_description"]').find('h4').should('contain.text', 'Stylish Dress');
});

