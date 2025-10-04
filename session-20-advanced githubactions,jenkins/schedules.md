# Schedules Workflow 

- useful for running jobs automatically at specific time like
- nightly builds, daily reports, cleanup tasks etc..

## Basic Syntax
```yml
name: Scheduled Workflow

on: 
    schedule:
        - cron: "*/5 * * * *"  #Run everyday at 00:00

jobs: 
    builds:
        runs-on: ubuntu-latest

        steps:
            - name: Testig Cron Job
              run: echo "Hello fom CRON JOB"

```

## You cna Also Create Another Workflow to just see the time as well
```yml
name: Schedule-Test

on:
  schedule:
    - cron: "*/5 * * * *"
  workflow_dispatch:

jobs:
   show-time:
     runs-on: ubuntu-latest
     steps:
       - name: Show Current UTC Time
         run: date -u

       - name: Show Current Local time (IST)
         run: date -d '+5 hours 30 minutes'
    
```

- save above files and try to push them on github
- it will schedule and runs the job after 5 minutes
- may be it can take time to setup runners by github
- make sure your time mentioned in UTC 

- you can see the jobs run like scheduled in actions workflow.
- workflow_dispatch: allows you to also trigger manually workflow

## Create one workflow for NOdeJS

```yml
name: Daily Build

on:
    schedule:
        - cron: "*/5 * * * *"
    workflow_dispatch: 
    push:
        branches:
            - main

jobs:
    build:
        runs-on: ubuntu-latest
        steps:

            - name: Show Current Time and Date
              run: date -u
            - name: Checkout Code
              uses: actions/checkout@v5

            - name: Set up Node JS
              uses: actions/setup-node@v5
              with:
                node-version: '20.19.0'
            
            - name: Install Dependencies
              run: rm -rf node_modules package-lock.json && npm install

            - name: Run tests
              run: npm test
```

- in above code it will trigger manually if you want
- trigger on every push of main
- also, trigger after every 5 minutes