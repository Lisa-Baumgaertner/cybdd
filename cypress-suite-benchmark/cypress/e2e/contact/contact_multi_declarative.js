import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the homepage', () => {
  cy.visit('https://automationexercise.com/');

});

When('the user navigates to the contact page', () => {
    cy.get('a[href="/contact_us"]').should('contain.text', 'Contact us').click();
 
});

When('the user provides valid contact details and a message about an order issue', () => {
    cy.get('[data-qa="name"]').clear().type('Janet Doe');
    cy.get('[data-qa="email"]').clear().type('janetdoe@test.com');
    cy.get('[data-qa="subject"]').clear().type('Problem with my order');
    cy.get('[data-qa="message"]').clear().type('My order has not been shipped.');
 
});

When('the user submits the contact form', () => {
    cy.get('[data-qa="submit-button"]').click();
 
});

Then('the message should be displayed, that the form was sent successfully', () => {
    cy.get('[class="status alert alert-success"]').should('contain.text', 'Success! Your details have been submitted successfully.');
 
});
