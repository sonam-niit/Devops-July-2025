# Deploying DB and App servers in coordinated manner using Ansible

- Database Setup
- Application server connect after DB is Ready
- coordinated all things using ansible, inventory, roles and playbook

- create folder python-db-app
- move to that folder and create inventory and site.yml file

- create 2 roles

```bash
ansible-galaxy init roles/db
ansible-galaxy init roles/app
```

- go to roles --> db --> tasks --> edit main.yml
- add the code as shown in that file

- go to roles -> db --> default --> edit main.yml
- add varaibles as shown

**Explanation for DB main.yml**
- sudo -u postgres psql -tc "SELECT 1 FROM pg_database where 
    datname = 'myapp'" | grep -q 1 || 
    sudo -u postgres psql -c "CREATE DATABASE myapp;"

- sudo -u postgres (run command as postgres user- default user like root user)
- psql -tc "SELECT 1 FROM pg_database where datname = 'myapp'"
- psql to connnect with postgresql (its command line client)
- tc (t for tuples-like header formatting, -c its command)
- I am asking does myapp DB exist ? if yes then it return 1
- grep -q 1 ( if 1 found then exit status 0 else exit status 1)

### For Python application

- roles --> app -> files -> create new folder named app/app.py
- roles --> app -> tasks -> main.yml (add content as mentioned)

- make sure you save all your files
- in aws instance make sure port no 5000 is open in security group

- run playbook
```bash
ansible-playbook -i inventory.yml site.yml
```
- check public-ip:5000 and you can see DB version that means its connected with DB from python application
