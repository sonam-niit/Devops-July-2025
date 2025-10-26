# Configuration Management

- Its a process of handling changes systematically to ensure system integrity over a time.
- It involves maintaining consistency of system changes by tracking and control changes in software/handware/infra/ networking etc..

**Why**
- I have created 1 Python project and i want to run it over 10 AWS Instances

    1. create 10 instances
    2. connecte with instance 1 using ssh
    3. install python dependencies
    4. install github
    5. clone repo
    6. run the project
    7. repeate step 2 - 6 for all 9 instances.

- Its time consuming process
- changes to generate human errors

- to solve above issues we can use configuration management using Ansible.

**Ansible Install**

- open wsl
```bash
# update packages
sudo apt update
sudo apt install ansible -y
ansible --version

# install in Mac
brew install ansible
ansible --version
```
## Let's Create simple ansible playbook

- create file first-playbook.yml
```yml
- name: Sample Playbook run with Localhost
  hosts: localhost

  tasks:
  - name: Say hello
    debug:
      msg: "this is first Hello From Ansible"

  - name: Another Task Demo
    debug:
      msg: "Sample Debug Message"
  
  - name: create Sample File
    copy:
      dest: /home/sonam/developers/demo.txt
      content: "This file was created by Ansible on localhost"
```
- save the file
- run below command
```bash
ansible-playbook first-playbook.yml
# if you are getting warning then try to pass inventory file as localhost
ansible-playbook first-playbook.yml -i localhost, --connection=local
```
- check output

