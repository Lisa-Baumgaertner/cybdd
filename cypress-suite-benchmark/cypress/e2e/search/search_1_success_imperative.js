import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the site {string}', (url) => {
  cy.visit(url);
  
});

When('the user types {string} into the search bar', (search_term) => {
  cy.get('[name="search"]').type(search_term);
})

When('the user clicks the search button', () => {
  cy.get('[class="btn btn-default btn-lg"]').click();
})

Then('the text {string} should be displayed', (text) => {
  cy.get('[id="content"]').find('h1').should('contain.text', text);
});
