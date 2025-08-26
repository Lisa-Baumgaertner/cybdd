import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

/* Cypress.on('uncaught:exception', (err, runnable) => {
  // returning false here prevents Cypress from failing the test
  return false;
}); */


Given('the user visits {string}', (url) => {
  cy.visit(url);
});

When('the user clicks on "My Account" in the top bar', (first_name) => {
  cy.get('[title="My Account"]').click();
});

When('selects "Register" from the dropdown', (last_name) => {
  cy.get('[class="dropdown-menu dropdown-menu-right"]').click();
  cy.get('[class="btn btn-primary"]').click();
});

When('enters valid details including', (dataTable) => {
  //cy.get('[id="userEmail"]').type(email);
  var propValue;
    dataTable.hashes().forEach(elem =>{
      for(var propName in elem) {
        propValue = elem[propName]

        cy.log(propName,propValue);
    }
    });
});

When('confirms the password', () => {
  //cy.get('[for="gender-radio-2"]').click();
});

When('agrees to the Privacy Policy', () => {
  //cy.get('[id="userNumber"]').type(mobile_number);
});

When('submits the form', () => {
  //cy.get('[id="userNumber"]').type(mobile_number);
});

Then('the user should see a message {string}', (text) => {
  //cy.get('[id="example-modal-sizes-title-lg"]').should('contain.text', text);
});
