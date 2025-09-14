# Run node project pipeline using Github Actions

1. copy the project code which is provide here in node-project-sample folder.
2. also create pipeline under the workflows folder named node-ci.yml
3. add below mentioned code
```yml
name: Nodejs CI
on : [push]
jobs:
    build:
        runs-on: ubuntu-latest
        steps: 
            # Step 1
            - name: Checkout repository
              uses: actions/checkout@v5
            # Step 2
            - name: Set up Node JS
              uses: actions/setup-node@v5
              with:
                node-version: 18
            # Step 3
            - name: Install Dependencties
              run: npm install
            # Step 4
            - name: Run Tests
              run: npm test

```
4. now push this to your github and check the actions
5. see the output of npm install and  npm test commands.
