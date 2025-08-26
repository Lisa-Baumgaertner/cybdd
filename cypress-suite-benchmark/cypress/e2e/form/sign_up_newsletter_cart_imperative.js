import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user clicks the {string} button', (text) => {
  cy.get('[class="nav navbar-nav"]').find('[href="/view_cart"]').should('contain.text', text).click();
});

Then('the cart page should be displayed on {string}', (text) => {
  cy.url().should('contain', text);
});

When('the user scrolls down to the footer section', () => {
  cy.get('#footer').scrollIntoView();
});

Then('the text {string} should be visible', (text) => {
  cy.get('[class="single-widget"]').should('contain.text', text);
});

When('the user enters the valid email address {string} into the subscription input field', (text) => {
  cy.get('#susbscribe_email').clear().type(text);
});

When('the user clicks the subscription arrow button', () => {
  cy.get('#subscribe').click();
});

Then('a success message {string} should be visible', (text) => {
  cy.get('[class="alert-success alert"]').should('contain.text', text);
});
