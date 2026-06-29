# Terraform EC2 Minimal Project

This is a minimal Terraform project to create one AWS EC2 instance.

## Files

```text
terraform-ec2-minimal/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars.example
└── .gitignore
```

## Before running

Configure AWS credentials using AWS CLI or environment variables.

### Option 1: AWS CLI

```bash
aws configure
```

### Option 2: Environment variables

Linux/macOS/Git Bash:

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

Windows PowerShell:

```powershell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

## Setup variables

Copy the example file:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Update these values inside `terraform.tfvars`:

```hcl
aws_region          = "us-east-1"
ami_value           = "ami-xxxxxxxxxxxxxxxxx"
instance_type_value = "t2.micro"
subnet_id_value     = "subnet-xxxxxxxxxxxxxxxxx"
instance_name       = "terraform-demo-ec2"
```

## Run Terraform

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Type `yes` when Terraform asks for confirmation.

## Destroy resources

```bash
terraform destroy
```

Type `yes` when Terraform asks for confirmation.

## Important

Do not commit `terraform.tfvars` if it contains real values or secrets.
"# DevOps-1" 
