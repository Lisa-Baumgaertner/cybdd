import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.viewport(1280, 800);
  cy.visit(url);
});

When('the user clicks the {string} category in the top bar navigation', (category) => {
  cy.get('[data-codecept="Bekleidung-navItem"]').click();
});

When('the user clicks on {string} and makes sure to choose the first', (subcat) => {
  cy.get('[data-codecept="categoryTitle"]').first().click();
});

When('then clicks on item with title {string} and makes sure to choose the first', (subsubcat) => {
  cy.get('[data-mapp-click="side_navi.category.lvl3"]').first().click();
});

Then('the product list page should be displayed with title {string}', (title) => {
  cy.get('[data-codecept="categoryTitle"]').should('contain.text', title)
    
});
