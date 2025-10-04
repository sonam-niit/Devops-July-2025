describe('API Testing example',()=>{
    it('GET Request',()=>{
        cy.request('https://jsonplaceholder.typicode.com/posts/1')
        .its('body')
        .should('include',{id:1})
    })
})