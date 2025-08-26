import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user scrolls down to the bottom of the page', () => {
  cy.get('#footer').scrollIntoView();
});

Then('the subscription section should be visible', () => {
  cy.get('[class="single-widget"]').find('h2').should('be.visible');
});

When('the user chooses to return to the top', () => {
  cy.get('#scrollUp').click();
});


Then('the homepage headline should be visible', () => {
  cy.get('[class="col-sm-6"]').find('h2').should('contain.text', 'Full-Fledged practice website for Automation Engineers');
});
