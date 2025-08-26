import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Bergfreunde website', (url) => {
  cy.viewport(1280, 800);
  cy.visit('https://www.bergfreunde.de/');
});

When('the user navigates through categories to {string}', (category) => {
  cy.get('[data-codecept="Bekleidung-navItem"]').click();
  cy.get('[data-codecept="categoryTitle"]').first().click();
  cy.get('[data-mapp-click="side_navi.category.lvl3"]').first().click();
});

Then('the product listing page titled {string} should be displayed', (title) => {
  cy.get('[data-codecept="categoryTitle"]').should('contain.text', title)
    
});
