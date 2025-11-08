# Creating Roles in Ansible

- Roles helping to manage the complex playbooks
- structure your code, increase reusability and redability of your code
- create folder: ansible-role
- move to that folder: cd ansible-role
- now run below commands for creating roles.

```bash
ansible-galaxy init frontend
ansible-galaxy init backend
```

- when you run these commands you can see folder generated named frontend and backend
- its having below folders

    1. defaults: keep default variables
    2. files: keep static files for copy
    3. handles: restart type of services
    4. meta: role dependencies
    5. tasks: main task ( like package install etc..)
    6. templates: you cna add templates like jinja2
    7. tests: write test cases
    8. vars: role specific variables you can add here 

### Now, let's configure frontend role

1. Step1: tasks folder/ main.yml

```yml
---
# tasks file for frontend

- name: Install nginx
  apt: 
    name: nginx
    state: present
    update_cache: yes

- name: Copy Custom index.html
  template:
    src: index.html.j2
    dest: /var/www/html/index.html
  notify: restart nginx
```

2. Step2: Handlers/main.yml

```bash
---
# handlers file for frontend

- name: restart nginx
  service: 
    name: nginx
    state: restarted
```

3. Step3: default variables for template 
```yml
---
# defaults file for frontend

nginx_title: "Welcome to My Website"
nginx_message: "Deploying this using ansible role"
```
4. templates-> create file --> index.html.j2
```j2
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{{ nginx_title }}</title>
    </head>
    <body>
        <h1>{{ nginx_message }}</h1>
    </body>
</html>
```

5. step5 create main playbook outside the role folder playbook.yml

```yml
---
- hosts: aws1
  become: true
  roles:
    - frontend
```
6. create inventory file

```yml
all:
  hosts:
    aws1:
      ansible_host: <AWS_INSTANCE_PUBLIC_IP_OR_DNS>
      ansible_user: ubuntu
      ansible_ssh_private_key_file: ~/.ssh/ansiblekey.pem
```

7. Run below command in teminal

```bash
ansible-playbook -i inventory.yml playbook.yml
# once its completed
# check browser using public IP you can see the Jinja template code
# which is using default values
# deployed on Nginx
```