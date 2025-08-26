import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user chooses the li element with href {string} in top navigation', (href) => {
  cy.get(`li a[href="${href}"]`).click();
  
});

Then('the user should be navigated to the Test Cases page successfully and see the text {string}', (text) => {
  cy.get('[class="title text-center"]').should('contain.text', text);
});
