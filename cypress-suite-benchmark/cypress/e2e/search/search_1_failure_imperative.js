import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the page {string}', (url) => {
  cy.visit(url);
  
});

When('the user clicks on the search button and chooses the first one', () => {
  cy.get('[class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"]').first().click();
})

When('the user clicks on the search bar and chooses the first one', () => {
  cy.get('input[name="search"]').first().type('nonexistent12345678');
})

When('the user enters the search term {string}', (search_term) => {
  cy.get('input[name="search"]').first().type(search_term);
})

When('the user clicks the search button and chooses the first one', () => {
  cy.get('[class="cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button"]').first().click();
})

Then('the system informs the user with {string}', (text) => {
  cy.get('[class="mw-search-nonefound"]').should('contain.text', text);
});




