# Poll SCM in Jenkins

- provide a scheduler like a cron-job
- everytime jenkins will go to your repo and check
- if no chnages -> nothing happens
- changes found -> the pipeline will execute again

Minute Hour DOM Month Dow
H/15 * * * * -- Check after every 15 minutes

0 0 * * * -- check at every midnight

H 2 * * 1 -- run on every monday at 2 am

( H helps to distribute load accross Jenkins nodes if multiple jobs
poll SCM)


