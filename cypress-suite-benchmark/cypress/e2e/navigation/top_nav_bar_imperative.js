import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user checks the number of items in the top navigation bar and makes sure it is {string}', (text) => {
  cy.get('[class="nav navbar-nav"]').find('li').should('have.length', text);
});

Then('the navigation bar should include texts for {string}, {string}, {string}, {string}, {string}, {string}, {string}, and {string}', (home, products, cart, signup, testcases, api, video, contact) => {
  cy.get('[class="nav navbar-nav"]').find('li').eq(0).should('contain.text', home);
  cy.get('[class="nav navbar-nav"]').find('li').eq(1).should('contain.text', products);
  cy.get('[class="nav navbar-nav"]').find('li').eq(2).should('contain.text', cart);
  cy.get('[class="nav navbar-nav"]').find('li').eq(3).should('contain.text', signup);
  cy.get('[class="nav navbar-nav"]').find('li').eq(4).should('contain.text', testcases);
  cy.get('[class="nav navbar-nav"]').find('li').eq(5).should('contain.text', api);
  cy.get('[class="nav navbar-nav"]').find('li').eq(6).should('contain.text', video);
  cy.get('[class="nav navbar-nav"]').find('li').eq(7).should('contain.text', contact);
});