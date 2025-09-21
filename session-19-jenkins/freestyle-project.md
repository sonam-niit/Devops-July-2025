# Create Free Style Project in Jenkins

1. Jenkins Dashboard
2. new Item click
3. give the name: simple-freestyle-demo
4. select Free Style Project
5. Add Description 
6. Select Git and add Link 

[Python Sample Project](https://github.com/sonam-niit/python-jenkins-cicd/blob/main/Jenkinsfile)

7. Poll SCM: H/20 * * * *
8. In build step select execute shell write below shell commands
```bash
echo " set up virtual environment"
python3 -m venv venv
echo " install dependencies"
. venv/bin/activate && pip install -r requirements.txt
echo "run test cases"
. venv/bin/activate && pytest --maxfail=1 --disable-warnings -q
```

9. save and build now
10. check console output
