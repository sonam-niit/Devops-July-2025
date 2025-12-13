# Terraform

- It is a IaC tool
- which manages all infra in declarative approach using HCL

## Extension for Terraform
![Extension](images/hcl.png)

## How to install Terraform

[Reference Link](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

- installation on Linux

```bash
# Ensure that your system is up to date and that you have installed the gnupg and software-properties-common packages. 
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

# Install HashiCorp's GPG key.
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Verify the GPG key's fingerprint.
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

# Add the official HashiCorp repository to your system.
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Update apt to download the package information from the HashiCorp repository.
sudo apt update
# Install Terraform from the new repository.
sudo apt-get install terraform
```