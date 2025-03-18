![terraformazurehighlight drawio](https://github.com/user-attachments/assets/897456d7-1237-4123-b873-9a8ab5afba5c)


# Azure Game Highlight Processor with Terraform 🚀

## Introduction

Welcome back for another exciting Azure project! This time, we're focusing on Infrastructure as Code (IaC) and automation to optimize how we manage cloud resources. Instead of manually provisioning our Azure infrastructure, we’ll leverage Terraform, a powerful IaC tool, to automate the entire process.

In our previous project, we built an Azure-based game highlight processor from scratch. This project automates the same infrastructure deployment using Terraform, making our workflow faster, more efficient, and repeatable. Let’s dive in! 🏊🏾‍♀️

### Project Overview

#### What We Did Previously:

✅ Fetched game data from RapidAPI and formatted it for readability.

✅ Stored the data as a text file in an Azure Blob container.

✅ Downloaded and processed videos from a provided URL, storing them in the same container.

#### What We Are Doing Now:

✅ We replace manual resource creation with Terraform, automating:

✅ Azure Storage Account creation

✅ Blob Container provisioning

✅ Environment variable setup

We maintain the same Python scripts from the last project, but remove the need for manual configuration.

update_env.py dynamically retrieves Azure credentials from Terraform outputs and injects them into the .env file.

## 🛠 Python Configuration 

Environment Setup (.env File)💻

The .env file stores all environment variables, keeping sensitive values like API keys and credentials separate from the script.

config.py – Centralized Configuration💻

Loads environment variables from .env using python-dotenv.
Stores key settings such as API endpoints, RapidAPI Key, and Azure Storage details.
Dynamically constructs the Azure Storage connection string if one isn’t explicitly provided.

fetch.py – Fetching Highlights💻

Calls the RapidAPI Sports API to retrieve basketball highlight data.
Uses the requests library to send API requests with predefined headers and query parameters.
Parses the JSON response and uploads the data as a file to Azure Blob Storage.

process_one_video.py – Processing a Single Video💻

Downloads the previously stored JSON file from Azure Blob Storage.
Extracts the first video URL from the JSON content.
Downloads the video from the extracted URL.
Uploads the downloaded video back to the Azure Blob Storage container.

run_all.py – Full Workflow Execution💻

Manages the complete process, ensuring each step runs sequentially with built-in retry logic.

update_env.py – Automating .env Updates💻

Updates the .env file automatically after Terraform provisions resources.
Runs terraform output -json to fetch details like storage account name, access key, and container name.
Updates the .env file to ensure Python scripts always use the latest resource configurations.

## 🛠Terraform Configuration

main.tf💻

Acts as the blueprint for our Azure infrastructure.

Defines:

Resource Group (land plot 🏡)

Storage Account (house 🏠)

Blob Container (rooms within the house 📦)

Once deployed, Terraform provisions all necessary cloud resources automatically.

variables.tf💻

Stores parameterized values for Terraform configurations.

Allows flexibility without modifying core Terraform scripts.

Example: Define storage account name, Azure region, etc.

outputs.tf💻

Returns critical information after Terraform deployment, such as:

Storage Account Name

Primary Key

Blob Container Name

Think of it as a post-construction report, providing the “keys” 🔑 to our infrastructure.

terraform.tfvars💻

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

## Project Prerequisites

1. RapidAPI Account

Sign up at RapidAPI to access NCAA game highlights.

<img width="1438" alt="rapidapi" src="https://github.com/user-attachments/assets/52dd4a2c-d575-4a71-ac3f-d39b8ceae4f4" />

Use the Sports Highlights API.

<img width="1421" alt="sportshighlightrapidapi" src="https://github.com/user-attachments/assets/4ec59552-5ad0-45c4-b975-29a5debfa6da" />

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
<img width="964" alt="azuresubscribe" src="https://github.com/user-attachments/assets/935a120a-376c-4b6c-a4a1-ba1f423f084b" />

<img width="892" alt="azaccountshow" src="https://github.com/user-attachments/assets/617d0f8b-a483-4e7b-af16-6e9dd79307c7" />



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
Step 2: Configure Environment Variables
Update the .env file with the following values:

RAPIDAPI_KEY

AZURE_SUBSCRIPTION_ID

AZURE_RESOURCE_GROUP

Step 3: Secure the .env File
Run the following command to restrict access:
```sh
chmod 600 .env
```

Step 4: Configure Terraform Variables
Modify the terraform.tfvars file with these details:

subscription_id

resource_group_name

storage_account_name

container_name

<img width="1241" alt="terraformtvars" src="https://github.com/user-attachments/assets/8db8e850-083c-4cf8-8985-fb942fec98e8" />


Step 5: Set Up a Python Virtual Environment
macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```
Windows
```sh
python -m venv venv
venv\Scripts\activate
```

Step 6: Install Dependencies
Ensure you have the latest package manager and install project dependencies:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

Step 7: Initialize and Deploy Terraform
```sh
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```
Type "yes" when prompted

Terraform will now create all necessary Azure resources.

<img width="752" alt="terraforminit" src="https://github.com/user-attachments/assets/0e53a305-6fa1-448a-8df2-b353897cbaf5" />


<img width="1192" alt="tplan" src="https://github.com/user-attachments/assets/97c2c801-745b-47ad-91b5-2e1a1c9c0011" />

<img width="1044" alt="applycomplete" src="https://github.com/user-attachments/assets/4c1717a5-838f-451a-8ba6-475aa56a7477" />



Step 8: Run the Python Scripts
```sh
python update_env.py
python run_all.py
```

<img width="1164" alt="all scripts successful" src="https://github.com/user-attachments/assets/4cf51bdf-b756-4c98-a31d-5797ff7fc774" />

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

<img width="786" alt="blobstorage" src="https://github.com/user-attachments/assets/be74483e-da79-4d3e-ac60-565956876480" />


<img width="638" alt="highlightsuccess" src="https://github.com/user-attachments/assets/3a53b4c0-b046-4fd1-9e0f-85502b84a64a" />

<img width="1283" alt="containervideo" src="https://github.com/user-attachments/assets/85fa9df2-f429-452c-8601-eaa916c340ab" />


<img width="1319" alt="first videoazure" src="https://github.com/user-attachments/assets/9c1186b3-0a7a-477d-b263-19c75721308d" />

<img width="1323" alt="bballhighlihg azure" src="https://github.com/user-attachments/assets/0a159252-9cb8-4679-9f51-2fe950d7941c" />




This ensures environment variables are set and the entire workflow executes seamlessly.

Conclusion

By incorporating Terraform, we eliminate manual infrastructure setup, making our Azure Game Highlight Processor more scalable, repeatable, and efficient. This project showcases the power of Infrastructure as Code—an essential skill for modern cloud engineers! 🚀🔥

Let's keep building! 🧱🚀
