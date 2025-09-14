# Actions in GitHub Actions

- action is smallest reusable unit in github action workflow
- its like a function or module that performs a specific task 
- like
    1. checkout code
    2. setup node Js/ python environment
    3. deploy application to aws
- workflow is created with one or more jobs and each job has multiple steps inside these steps you can use actions

## types of Actions

1. official Actions:
    - provided by GitHub
    - like actions/checkout --> check your repo code
2. Community Actions:
    - Cretaed and shared by other developers in Github Marketplace
    - setup node
3. Custom Actions:
    - you can created your own actions
    - javascript action (runs with some node env)
    - docker actions (run inside the container)

## where you can see the actions and copy the code
[Github MarketPlace](https://github.com/marketplace?query=node&type=actions)

- here you can search for actions and see the below provided code and try to use the same in your workflows.