import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the website', () => {
  cy.visit('https://testpages.eviltester.com/styled/basic-html-form-test.html');
});

When('the user fills out all required form fields', () => {
  cy.get('[name="username"]').type('JaneDoe');
  cy.get('[name="password"]').type('password123');
  cy.get('[name="comments"]').type('Hello world!');
});

When('the user selects all checkbox and radio options as instructed', () => {
  cy.get('[value="cb1"]').click();
  cy.get('[value="cb2"]').click();
  cy.get('[value="cb3"]').click();

  cy.get('[value="ms3"]').click();
});

When('the user selects the appropriate dropdown option', () => {
  cy.get('select[name="dropdown"]').select('dd2');
});

When('the user submits the form', () => {
  cy.get('[value="submit"]').click();
});

Then('the confirmation message should be displayed correctly', () => {
  cy.get('[class="explanation"]').should('contain.text', 'You submitted a form. The details below show the values you entered for processing.');
});
