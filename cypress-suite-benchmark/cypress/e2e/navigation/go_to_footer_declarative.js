import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the Bergfreunde website', () => {
  cy.visit('https://www.bergfreunde.de/');
});

Then('the footer should display all of the social media icons', () => {
  cy.get('[id="footer"]').scrollIntoView();
  cy.get('[data-codecept="ig-icon"]').should('be.visible');
  cy.get('[data-codecept="yt-icon"]').should('be.visible');
  cy.get('[data-codecept="pc-icon"]').should('be.visible');
});
