import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://www.imdb.com/');
});

When('the user performs a movie search', () => {
  cy.get('[data-testid="suggestion-search"]').click();
  cy.get('[data-testid="suggestion-search"]').clear().type('Inception');
  cy.get('[data-testid="suggestion-search"]').type('{enter}');
});

When('the user selects the first search result', () => {
  cy.get('[class="ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result"]').first().click();
});

Then('the correct movie detail page should be shown', () => {
  cy.get('[data-testid="hero__primary-text"]').should('contain.text', 'Inception');
});
