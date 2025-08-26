import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user visits {string}', (url) => {
  cy.visit(url);

});

When('the user clicks {string} in the top navigation bar', (text) => {
    cy.get('a[href="/contact_us"]').should('contain.text', text).click();
 
});

Then('the contact form should be visible', () => {
    cy.get('[id="contact-page"]').should('be.visible');
 
});

When('the user enters their name {string}, email address {string}, subject {string}, and message {string}', (name, email, subject, message) => {
    cy.get('[data-qa="name"]').clear().type(name);
    cy.get('[data-qa="email"]').clear().type(email);
    cy.get('[data-qa="subject"]').clear().type(subject);
    cy.get('[data-qa="message"]').clear().type(message);

});


When('the user clicks the Submit button', () => {
    cy.get('[data-qa="submit-button"]').click();
 
});


Then('the message {string} should be displayed', (message) => {
    cy.get('[class="status alert alert-success"]').should('contain.text', message);
 
});
