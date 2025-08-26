import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits the website {string}', (url) => {
  cy.visit(url);
});

When('the user enters {string} into the username field', (user_name) => {
  cy.get('[name="username"]').type(user_name);
});

When('the user enters {string} into the password field', (password) => {
  cy.get('[name="password"]').type(password);
});

When('the user enters {string} into the textarea comment field', (comment) => {
  cy.get('[name="comments"]').type(comment);
});

When('the user clicks all three checkbox items with the values cb1, cb2 and cb3', () => {
  cy.get('[value="cb1"]').click();
  cy.get('[value="cb2"]').click();
  cy.get('[value="cb3"]').click();
});

When('the user clicks radio item 3', () => {
  cy.get('[value="ms3"]').click();
});

When('the user selects Drop Down Item 2', () => {
  cy.get('select[name="dropdown"]').select('dd2');
});

When('the user submits the form using ths submit button', () => {
  cy.get('[value="submit"]').click();
});

Then('the text {string} should be contained', (text) => {
  cy.get('[class="explanation"]').should('contain.text', text);
});
