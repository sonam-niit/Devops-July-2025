# Ad-Hoc Commands?

- Ad-hoc commands are one-liner commands which is used to perform quick task on remote system without writing a playbook.

- We can use them for testing, troubleshooting, just to execute some admin operations.

- syntax: ansible <host-pattern> -m <module> -a "<module arguments>" [options]

**Modules**
1. ping
2. command
3. shell
4. copy
5. apt or yum
6. service
7. file
8. user
9. setup

**Examples**

```bash
# Ping
ansible -i inventory.yml all -m ping #it will check connectivity with all servers
# check uptime 
ansible -i inventory.yml all -m command -a "uptime"
# in server2 i want to install package nginx and start service
ansible -i inventory.yml server2 -m apt -a "name=nginx state=present" --become
ansible -i inventory.yml server2 -m service -a "name=nginx state=started" --become

# verify deployment
curl http://<public-ip or dns> # also check in browser as well

# install package git and check version
ansible -i inventory.yml server2 -m apt -a "name=git state=present" --becomen
ansible -i inventory.yml server2 -m shell -a "git --version"
# check disk space
ansible -i inventory.yml server2 -m shell -a "df -h"

# you can reboot all server
ansible -i inventory.yml server2 -m reboot --become

```

