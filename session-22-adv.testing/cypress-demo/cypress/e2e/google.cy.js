describe('google Test',()=>{
    //Test Case
    it('Visit google and check title ',()=>{
        cy.visit('https://www.google.com')
        cy.title().should('include','Google')
    })
})