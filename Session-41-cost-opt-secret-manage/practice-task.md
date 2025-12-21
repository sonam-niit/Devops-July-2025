# Practice Task using Terraform

- create RDS MySQL instance
- use Free tier elligible instance
- enable automated backup
- set up a backup window
- disable public access
- add meaningful tags

*Folder Structure*

- rds-terrafor
    - provider.tf
    - main.tf
    - variables.tf
    - outputs.tf (provide database endpoint)

**Extra Practice**

- Store DB password AWS Secret Manager
- Create security group for RDS(add in existing main.tf)

**Implement using Modules**

- security-group module
- rds module