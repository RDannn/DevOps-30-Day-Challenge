Azure Game Highlight Processor with Terraform 🚀

Introduction

Welcome back for another exciting Azure project! This time, we're focusing on Infrastructure as Code (IaC) and automation to optimize how we manage cloud resources. Instead of manually provisioning our Azure infrastructure, we’ll leverage Terraform, a powerful IaC tool, to automate the entire process.

In our previous project, we built an Azure-based game highlight processor from scratch. This project automates the same infrastructure deployment using Terraform, making our workflow faster, more efficient, and repeatable. Let’s dive in! 🏊🏾‍♀️

Project Overview

What We Did Previously

Fetched game data from RapidAPI and formatted it for readability.

Stored the data as a text file in an Azure Blob container.

Downloaded and processed videos from a provided URL, storing them in the same container.

What We Are Doing Now

We replace manual resource creation with Terraform, automating:

Azure Storage Account creation

Blob Container provisioning

Environment variable setup

We maintain the same Python scripts from the last project, but remove the need for manual configuration.

update_env.py dynamically retrieves Azure credentials from Terraform outputs and injects them into the .env file.

Terraform Configuration

main.tf

Acts as the blueprint for our Azure infrastructure.

Defines:

Resource Group (land plot 🏡)

Storage Account (house 🏠)

Blob Container (rooms within the house 📦)

Once deployed, Terraform provisions all necessary cloud resources automatically.

variables.tf

Stores parameterized values for Terraform configurations.

Allows flexibility without modifying core Terraform scripts.

Example: Define storage account name, Azure region, etc.

outputs.tf

Returns critical information after Terraform deployment, such as:

Storage Account Name

Primary Key

Blob Container Name

Think of it as a post-construction report, providing the “keys” 🔑 to our infrastructure.

terraform.tfvars

Specifies environment-specific configurations, such as:

Development (dev)

Production (prod)

Helps manage infrastructure across different deployment stages.

update_env.py: Automating Environment Variables

Instead of manually retrieving Azure credentials, update_env.py automates this step:

How it Works:

Extracts Terraform outputs for:

AZURE_SUBSCRIPTION_ID

AZURE_RESOURCE_GROUP

AZURE_STORAGE_ACCOUNT_NAME

AZURE_STORAGE_KEY

AZURE_BLOB_CONTAINER

Updates .env dynamically with these values.

Ensures all scripts (e.g., fetch.py, process_one_video.py) use the correct credentials automatically.

Project Prerequisites

1. RapidAPI Account

Sign up at RapidAPI to access NCAA game highlights.

Use the Sports Highlights API.

2. Install Required Tools

Ensure you have the following installed:

Python 3 (python3 --version)

Git (for cloning the repository)

Terraform (terraform --version)

Azure CLI (az login)

3. Retrieve Your Azure Subscription ID
```sh
az account show --query id -o tsv
```
Use this to configure Terraform.

Project Structure

```sh
├── .env                      # Environment variables for app configuration
├── .gitignore                # Ignore files in Git
├── requirements.txt          # Python dependencies
├── config.py                 # Loads environment variables for Azure
├── fetch.py                  # Fetches highlights from RapidAPI
├── process_one_video.py       # Processes video highlights
├── run_all.py                # Orchestrates script execution
├── update_env.py              # Updates .env with Terraform outputs
└── terraform/                 # Terraform configuration directory
    ├── main.tf                # Defines infrastructure
    ├── variables.tf           # Parameterized variables
    ├── outputs.tf             # Terraform output values
    └── terraform.tfvars       # Environment-specific configurations
```

Step 1: Clone The Repository
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

Step 2: Initialize and Deploy Terraform
```sh
cd terraform
terraform init
terraform apply -auto-approve
```

Terraform will now create all necessary Azure resources.

Step 3: Run the Python Scripts
```sh
python update_env.py
python run_all.py
```
🎬 How the Script Works:
1️⃣ Run fetch.py – Grabs the latest game highlights from the API and uploads the JSON file to Azure Blob Storage.

2️⃣ Wait for resources to settle – Ensures everything is good to go before moving forward.

3️⃣ Run process_one_video.py – Downloads the JSON file, extracts the video URL, fetches the video, and uploads it back to Azure Blob Storage.

✅ Optional Check: Verify that the JSON file and video were successfully uploaded to the container:
```sh
az storage blob list \
    --account-name <YOUR_STORAGE_ACCOUNT_NAME> \
    --container-name <YOUR_CONTAINER_NAME> \
    --query "[].{name:name}" \
    --output table
```

This ensures environment variables are set and the entire workflow executes seamlessly.

Conclusion

By incorporating Terraform, we eliminate manual infrastructure setup, making our Azure Game Highlight Processor more scalable, repeatable, and efficient. This project showcases the power of Infrastructure as Code—an essential skill for modern cloud engineers! 🚀🔥

Let's keep building! 🧱🚀
