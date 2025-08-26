import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('https://automationexercise.com/');
});

When('the user navigates to the Test Cases page', () => {
  cy.get(`li a[href="/test_cases"]`).click();
});

Then('the Test Cases page should be displayed', () => {
  cy.get('[class="title text-center"]').should('contain.text', 'Test Cases');
});
