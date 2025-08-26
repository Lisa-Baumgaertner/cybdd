import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Automation Exercise website', (url) => {
  cy.visit('https://automationexercise.com/');
});

When('the user subscribes to the newsletter with a valid email address', () => {
  cy.get('#footer').scrollIntoView();
  cy.get('#susbscribe_email').clear().type('testuser@example.com');
  cy.get('#subscribe').click();
});

Then('a success message confirming the subscription should be visible', () => {
  cy.get('[class="alert-success alert"]').should('contain.text', 'You have been successfully subscribed!');
});
