import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user scrolls down to the footer', () => {
  cy.get('[id="footer"]').scrollIntoView();
});

Then('the icons for instagram, youtube and podcast should be visible', () => {
  cy.get('[data-codecept="ig-icon"]').should('be.visible');
  cy.get('[data-codecept="yt-icon"]').should('be.visible');
  cy.get('[data-codecept="pc-icon"]').should('be.visible');
});
