import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user navigates to cart page', () => {
  cy.get('[class="nav navbar-nav"]').find('[href="/view_cart"]').click();
  cy.url().should('contain', '/view_cart');
});

When('the user navigates to subscription', () => {
  cy.get('#footer').scrollIntoView();
  cy.get('[class="single-widget"]').should('contain.text', 'Subscription');
});

When('the user provides a valid email address for newsletter subscription', () => {
  cy.get('#susbscribe_email').clear().type('test@test.com');
});

When('the user submits the subscription form', () => {
  cy.get('#subscribe').click();
});

Then('the system should confirm successful subscription with a message', () => {
  cy.get('[class="alert-success alert"]').should('contain.text', 'You have been successfully subscribed!');
});

