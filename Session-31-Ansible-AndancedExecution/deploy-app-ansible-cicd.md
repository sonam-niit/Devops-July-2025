# Deploy Application using Ansible + CICD pipeline using Github Actions

- create project folder: ansible-cicd
- move to the folder: cd ansible-cicd
- create folder named ansible and under that create
- create 2 files: inventory.yml, playbook.yml

- add code as shown in inventory and playbook

- now setup workflow deploy.yml

- once all code setting done.

- Go to Github and create Repo- ansible-cicd
- repo settings --> secrets and variables -> actions -> add new repo secret

- create 3 secrets
- HOST
- RENOTE_USER
- ANSIBLE_PRIVATE_KEY

- Last push the code and you can see application deployed using cicd with ansible

[Code Repo Link](https://github.com/sonam-niit/july-ansible-cicd)

