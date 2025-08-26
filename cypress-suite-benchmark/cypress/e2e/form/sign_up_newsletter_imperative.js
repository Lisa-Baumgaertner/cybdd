import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user scrolls down to footer', () => {
  cy.get('#footer').scrollIntoView();
});

When('the user types {string} into the subscription input', (email) => {
  cy.get('#susbscribe_email').clear().type(email);
});


When('the user clicks the subscribe button', (subscribe_button) => {
  cy.get('#subscribe').click();
});

Then('the success message {string} should be visible', (message) => {
  cy.get('[class="alert-success alert"]').should('contain.text', message);
});
