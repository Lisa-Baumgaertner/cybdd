import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

Then('the home page should be visible with text {string}', (text) => {
  cy.get('[class="col-sm-6"]').find('h2').should('contain.text', text);
});

When('the user scrolls down to the footer of the page', () => {
  cy.get('#footer').scrollIntoView();
});

Then('the {string} section should be visible', (text) => {
  cy.get('[class="single-widget"]').find('h2').should('contain.text', text);
});

When('the user clicks the arrow at the bottom-right corner of the page', () => {
  cy.get('#scrollUp').click();
});


Then('the text {string} should be visible', (text) => {
  cy.get('[class="col-sm-6"]').find('h2').should('contain.text', text);
});
