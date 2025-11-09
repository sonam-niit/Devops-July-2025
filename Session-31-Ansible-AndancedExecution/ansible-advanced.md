# Advanced Ansible

## Ansible Forks

- forks define how many host ansible can manage in parallel during a playbook run.

- by default (forks=5)
- means Ansible runs tasks on 5 hosts at a time

- If you want to increase temp
```bash
ansible-playbook playbook.yml -f 20
```
- for permanent update use ansible.cfg
```ini
[defaults]
forks=20
# choose below option
forks= min(20, number_of_hosts) # using this you can manage performance
```