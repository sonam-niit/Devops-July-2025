# IaC :: Infra structure as a code

- mordern approach for provisioning infrastructure (servers, databases, storages, load balancers, networks) create using machine redable configurations files rather that manuall process.

- When you do traditonal setup it must be
    - time consuming
    - error prune (human error)
    - difficult to replicate

- this makes a developers life easier using code.

## IaC is having 2 approaches

1. Declarative (What)

    - define what you want (desired state)
    - the tool (terraform) figures how to achieve that
    - terraform is using HCL 

2. Imperative (How):

    - define how to the infra should be created
    - writing shell scripts
    - AWS CLI

### Polular IaC tools

1. Terraform: multi-cloud, Declarative and state based

2. Chef/puppet: configurtaion management tool with some IaC capabilities

3. Ansible: configuration management + IaC

### Difference between Terraform(IaC) & Ansible(CM)

- terraform is more focused on provisioning servers and infra
- creating instances, create S3 buckets, VPC and load balancers etc..

- Ansible is focusing on setup software inside servers
- installing packages with ansible