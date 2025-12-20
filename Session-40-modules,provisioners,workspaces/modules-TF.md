# Modules in Terrafform

- In terraform , a module is a container for multiple resources that are used together.
- reusable, parameterized blue print for infrastructure.

## Modules help

- reuse code (DRY principle)
- organized infra
- maintain consitency across environments
- simplify complex steps
- follow best practices

**Let's Implement**

- create project folder structure as shown here under project folder
- here 3 modules implemented
- vpc, sec group and ec2
- for each module seperatly main, variables and outputs file created.
- outside of module folder project root main, variables and outputs file created.

- create project structure as shown 

```bash
terrform init
terraform apply --auto-approve
#check resources created
terraform destroy --auto-approve
```