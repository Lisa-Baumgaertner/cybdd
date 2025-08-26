import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website', () => {
  cy.visit('https://automationexercise.com/');
});

Then('the user checks the top navigation bar for correctness', () => {
  cy.get('[class="nav navbar-nav"]').find('li').should('have.length', 8);
  cy.get('[class="nav navbar-nav"]').find('li').eq(0).should('contain.text', 'Home');
  cy.get('[class="nav navbar-nav"]').find('li').eq(1).should('contain.text', 'Products');
  cy.get('[class="nav navbar-nav"]').find('li').eq(2).should('contain.text', 'Cart');
  cy.get('[class="nav navbar-nav"]').find('li').eq(3).should('contain.text', 'Signup / Login');
  cy.get('[class="nav navbar-nav"]').find('li').eq(4).should('contain.text', 'Test Cases');
  cy.get('[class="nav navbar-nav"]').find('li').eq(5).should('contain.text', 'API Testing');
  cy.get('[class="nav navbar-nav"]').find('li').eq(6).should('contain.text', 'Video Tutorials');
  cy.get('[class="nav navbar-nav"]').find('li').eq(7).should('contain.text', 'Contact us');
});

