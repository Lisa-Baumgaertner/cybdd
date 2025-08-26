import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the homepage', () => {
  cy.visit('https://opencart.abstracta.us');
  
});

When('a search is performed for the given search term', () => {
  cy.get('[name="search"]').type('MacBook');
  cy.get('[class="btn btn-default btn-lg"]').click();
})

Then('the results page should show the heading including the search term', () => {
  cy.get('[id="content"]').find('h1').should('contain.text', 'MacBook');
});
