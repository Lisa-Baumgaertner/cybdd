import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('the user is on the contact page', () => {
  cy.visit('https://automationexercise.com/contact_us');

});

When('the user provides valid contact information and a message', () => {
    cy.get('[data-qa="name"]').clear().type('Janet Doe');
    cy.get('[data-qa="email"]').clear().type('janetdoe@test.com');
    cy.get('[data-qa="subject"]').clear().type('Problem with my order');
    cy.get('[data-qa="message"]').clear().type('My order has not been shipped.');
 
});

When('the user submits the contact form', () => {
    cy.get('[data-qa="submit-button"]').click();
 
});


Then('the system should confirm that the contact message was sent successfully', () => {
    cy.get('[class="status alert alert-success"]').should('contain.text', 'Success! Your details have been submitted successfully.');
 
});
