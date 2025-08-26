import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on the search bar', () => {
  cy.get('[data-testid="suggestion-search"]').click();
});

When('the user types {string} into the search input and presses Enter to submit', (movie) => {
  cy.get('[data-testid="suggestion-search"]').clear().type(movie);
  cy.get('[data-testid="suggestion-search"]').type('{enter}');
});


When('the user clicks on the first result', () => {
  cy.get('[class="ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result"]').first().click();
});

Then('the Inception movie detail page should be displayed with title {string}', (media) => {
  cy.get('[data-testid="hero__primary-text"]').should('contain.text', media);
});
