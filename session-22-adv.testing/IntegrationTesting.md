# Integration Testing

- test  inter connected components
- Selenium Test
- install Selenium dependency

```bash
pip install selenium
```

- Download Browser Web Driver for Chrome
- add it in C:/Drivers folder for Windows
- /usr/local/bin for mac and /usr/bin for linux or wsl

# Cypress Testing

- Install Cypress
- Initalize Project
- Write First Test Case
- run the test in cypress Runner or CLI

- required node JS to setup cypress
- install node js [Download NodeJS](https://nodejs.org/en/download)
- open cmd and check below commands
```bash
node -v
npm -v
```

- create folder cypress-demo
- move into that folder using cmd: cd cypress-demo
- initialize project: npm init -y (create package.json file)
- install cypress in development dependency
- npm i cypress --save-dev 
- launch cypress using below command
- npx cypress open
- above command will create
    1. create cypress folder
    2. create its config file (cypress.json)
    3. see the test Runner UI
- open the browser where you can see cypress homepage click on e2e testing 
- click on open browser (you can see the dashboard of cypress)
- under cypress folder create folder named e2e
- create simple test case (test.cy.js)
```js
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
```

- automatically your dashboard will detect test file and show you the step by step execution





