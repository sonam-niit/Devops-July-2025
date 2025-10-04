//Test-Suite

describe('My First Test',()=>{
    //Test Case
    it('clicks the link "type" ',()=>{
        cy.visit('https://example.cypress.io/')
        cy.contains('type').click()
        cy.url().should('include','/commands/actions')
        cy.get('.action-email').type('sonam@gmail.com');
        cy.get('.action-email').should('have.value','sonam@gmail.com')
    })
})