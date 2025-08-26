import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Wikipedia homepage', () => {
  cy.visit('https://en.wikipedia.org/');
  
});

When('a search is performed for the search term', () => {
  cy.get('[class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"]').first().click();
  cy.get('input[name="search"]').first().type('nonexistent12345678');
  cy.get('[class="cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button"]').first().click();
})

Then('the system should inform the user that no results were found', () => {
  cy.get('[class="mw-search-nonefound"]').should('contain.text', 'There were no results matching the query');
});
