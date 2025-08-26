import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on the search input field', () => {
  cy.get('[data-testid="suggestion-search"]').click();
});

When('the user types {string} into the search input', brand => {
  cy.get('[data-testid="suggestion-search"]').clear().type(brand);
});

When('the user clicks the search button', () => {
  cy.get('[id="suggestion-search-button"]').click();
});

Then('a results page should appear showing the tv show or media related to {string}', media => {
  cy.get('[class="sc-4c6d853-0 gGHeXM"]').should('contain.text', media);
});
