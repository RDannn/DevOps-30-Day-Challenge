![nba drawio-2](https://github.com/user-attachments/assets/8f47e7cb-972e-4571-ae30-d62c2c64dd8e)







# NBA DATA LAKE AZURE🏀⛹🏽‍♂️

## Project Overview

We are back with another great project! 🚀 This will be our first project using Azure! We are using Azure resources to create a sports data lake! We did this similar project in AWS, now we are using Azure! We will grab the NBA data off line and store in the container/blob storage. Let's breakdown our code and see how everything works! 

## Code Breakdown 💻

### setup_nba_data_lake.py 💻

Azure Resources Overview
This part of the code is responsible for setting up and managing the essential Azure resources used in our pipeline. These resources include:

Resource Group: Think of this as a folder that keeps everything organized—it holds all the Azure resources for our project. This helps maintain a clean environment.
Azure Storage Account: Used for storing files and structured data, which we will interact with later.
Azure Synapse Analytics Workspace: The central hub for data analytics and SQL processing.
Environment Variables (.env file): Securely stores sensitive credentials, such as our SQL admin credentials. These credentials are not hardcoded but instead passed from the .env file. This approach ensures security and allows for easy updates in one place rather than changing multiple files.

Importing Required SDKs & Modules
At the top of our script, we import necessary Azure SDK libraries:

azure.mgmt.resource → Manages the Azure Resource Group.

azure.mgmt.storage → Handles Azure Storage Accounts.

azure.synapse → Manages the Azure Synapse Analytics Workspace.

azure.identity → Handles Azure authentication.

dotenv → Loads environment variables from the .env file.

os → Interacts with system environment variables.

💡 Quick Refresher: Similar to AWS, the .env file in Azure stores configuration values like resource group names and storage account names. This makes it easier to manage settings centrally—change a value once, and it updates across the entire project.

Retrieving Credentials from .env
Lines 11-15 pull credentials directly from the .env file, including the SQL admin username and password.
```sh
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
location = os.getenv("AZURE_LOCATION")
storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
workspace_name = os.getenv("SYNAPSE_WORKSPACE_NAME")
```

Error Handling for Missing Credentials

We use the raise function to ensure that SQL credentials are set before processing. If credentials are missing, the script will throw a ValueError, making debugging easier.
```sh
if not resource_group or not storage_account_name or not subscription_id:
    raise ValueError("Missing required Azure environment variables.")
```
🔐 Authentication Setup
This line initializes authentication using DefaultAzureCredential, which automatically detects authentication methods (e.g., environment variables, managed identities).
```sh
credentials = DefaultAzureCredential()
```
🪪 Pretty cool, right? This ensures that we securely connect to Azure without hardcoding credentials!

Creating the Azure Resource Group
Before we create any resources, we first ensure the resource group exists (or create it if needed).
```sh
resource_client = ResourceManagementClient(credentials, subscription_id)
resource_client.resource_groups.create_or_update(
    resource_group,
    {"location": location}
)
```
💡 Troubleshooting Tip: Always print success/failure messages when creating resources. This makes debugging easier when things don’t go as expected.

Creating the Azure Storage Account
This function handles the entire storage account creation process and returns the connection string to our .env file.

Step-by-Step Process:

Initialize the Storage Management Client:
```sh
storage_client = StorageManagementClient(credentials, subscription_id)
```
Ensure the Resource Group Exists Before Proceeding.
Define Storage Account Properties:
Location: Sets the Azure region where the storage account is created.
SKU: Specifies Locally Redundant Storage (LRS) for high availability.
Kind: Uses StorageV2, a general-purpose storage option.
```sh
storage_parameters = {
    "location": location,
    "sku": {"name": "Standard_LRS"},
    "kind": "StorageV2"
}
```

Wait for the Storage Account to be Created:
```sh
storage_async_operation = storage_client.storage_accounts.begin_create(
    resource_group, storage_account_name, storage_parameters
)
storage_async_operation.wait()
```
😱 Amazzzzing! This ensures that the storage account is fully provisioned before moving forward.
Retrieve and Construct the Connection String:
Access keys allow us to securely connect to Blob Storage.
If an error occurs, a failure message is returned for debugging.

Updating .env File with Connection Details
Once the storage account and Synapse workspace are created, the script saves the connection details to the .env file.
```sh
with open(".env", "a") as env_file:
    env_file.write(f"AZURE_CONNECTION_STRING={connection_string}\n")
    env_file.write(f"SYNAPSE_SQL_ENDPOINT={sql_endpoint}\n")
```
📂 This makes it easy to reference these values in other parts of the pipeline!

Fetching and Uploading Data to Azure Blob Storage
Finally, our script:
✔ Fetches NBA data
✔ Uploads it to Blob Storage
```sh
nba_data = fetch_nba_data()
if nba_data:
    upload_to_blob_storage(nba_data, connection_string)
```

🔄 Once completed, the script prints "Data lake setup complete." 🎉

Final Thoughts:

This script efficiently automates the setup of our Azure infrastructure, handling:
✅ Resource Group creation

✅ Storage Account provisioning

✅ Synapse Analytics workspace setup

✅ Secure credential management

✅ Data ingestion

🚀 With this foundation, the next steps involve data processing, analysis, and visualization within Synapse Analytics.



### azure_resources.py 💻

This next code creates our Azure synape analytics workspace and returns the SQL endpoint. 
1. Loading Environment Variables
```sh
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
SQL_ADMIN_LOGIN = os.getenv("SQL_ADMIN_LOGIN")
SQL_ADMIN_PASSWORD = os.getenv("SQL_ADMIN_PASSWORD")
if not SQL_ADMIN_LOGIN or not SQL_ADMIN_PASSWORD:
    raise ValueError("❌ ERROR: SQL_ADMIN_LOGIN and SQL_ADMIN_PASSWORD must be set in the .env file.")
```
The script starts by loading environment variables using dotenv, which allows us to securely retrieve credentials (SQL admin login and password).
If credentials are missing, it raises an error and halts execution immediately.

2. Initializing Azure Authentication
```sh
from azure.identity import DefaultAzureCredential

# Initialize Azure authentication
credential = DefaultAzureCredential()
```
The script uses DefaultAzureCredential() to authenticate with Azure, meaning it will attempt to use credentials from different sources (like environment variables, managed identities, or Azure CLI login).
This is the recommended way to authenticate in Azure services without hardcoding credentials.

3. Creating a Resource Group (if it doesn’t exist)
```sh
from azure.mgmt.resource import ResourceManagementClient

def create_resource_group(resource_group_name, location, subscription_id):
    """Ensure the Azure Resource Group exists before creating resources."""
    resource_client = ResourceManagementClient(credential, subscription_id)
    try:
        resource_client.resource_groups.create_or_update(
            resource_group_name, {"location": location}
        )
        print(f"✅ Resource group '{resource_group_name}' created or already exists.")
    except Exception as e:
        print(f"❌ Error creating resource group: {e}")
        raise
```
Before deploying anything, the script checks if the resource group exists; if not, it creates one in the specified location.
This ensures that subsequent resource creation (like Synapse workspace and storage account) has a valid group to belong to.

4. Creating a Storage Account
```sh
from azure.mgmt.storage import StorageManagementClient

def create_storage_account(resource_group, storage_account_name, location, subscription_id):
    """Create Azure Storage Account and return the connection string."""
    storage_client = StorageManagementClient(credential, subscription_id)

    # Ensure the resource group exists before proceeding
    create_resource_group(resource_group, location, subscription_id)

    try:
        print(f"⏳ Creating storage account '{storage_account_name}'...")
        storage_async_operation = storage_client.storage_accounts.begin_create(
            resource_group,
            storage_account_name,
            {
                "location": location,
                "sku": {"name": "Standard_LRS"},
                "kind": "StorageV2",
            },
        )
        storage_account = storage_async_operation.result()
        print(f"✅ Storage account '{storage_account_name}' created successfully.")

        # Get the connection string
        keys = storage_client.storage_accounts.list_keys(resource_group, storage_account_name)
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={keys.keys[0].value};EndpointSuffix=core.windows.net"
        return connection_string

    except Exception as e:
        print(f"❌ Error creating storage account '{storage_account_name}': {e}")
        raise
```

The function first ensures the resource group exists (since the storage account must be inside one).
Then it creates a Storage Account with Standard_LRS (Locally Redundant Storage), a common cost-effective choice.
The script retrieves and returns the storage connection string, which is used to interact with the storage account.

5. Creating the Synapse Workspace
```sh
from azure.mgmt.synapse import SynapseManagementClient

def create_synapse_workspace(resource_group, workspace_name, location, storage_account_name, subscription_id):
    """Create an Azure Synapse Analytics Workspace and return the SQL endpoint."""
    synapse_client = SynapseManagementClient(credential, subscription_id)

    # Ensure the resource group exists before proceeding
    create_resource_group(resource_group, location, subscription_id)

    try:
        print(f"⏳ Creating Synapse workspace '{workspace_name}'...")

        # Parameters for workspace creation
        workspace_info = {
            "location": location,
            "identity": {"type": "SystemAssigned"},  # Enable System Assigned Identity
            "default_data_lake_storage": {
                "account_url": f"https://{storage_account_name}.dfs.core.windows.net",
                "filesystem": "synapse",
            },
            "sql_administrator_login": SQL_ADMIN_LOGIN,
            "sql_administrator_login_password": SQL_ADMIN_PASSWORD,
        }

        synapse_async_operation = synapse_client.workspaces.begin_create_or_update(
            resource_group_name=resource_group,
            workspace_name=workspace_name,
            workspace_info=workspace_info,  # Ensure this argument is passed
        )

        workspace = synapse_async_operation.result()
        sql_endpoint = workspace.connectivity_endpoints["sql"]
        print(f"✅ Synapse workspace '{workspace_name}' created successfully. SQL Endpoint: {sql_endpoint}")
        return sql_endpoint

    except Exception as e:
        print(f"❌ Error creating Synapse workspace '{workspace_name}': {e}")
        raise
```

Breaking this down:

Initialize the Synapse Management Client
This allows us to interact with Synapse services in Azure.
Check for the Resource Group
It verifies that the required resource group exists before continuing.

Define Workspace Parameters

Location – Specifies the Azure region where the Synapse workspace will be created.

Identity – Enables a System Assigned Identity, which is used for authentication.

Default Data Lake Storage –
account_url: The URL of the storage account.

filesystem: The name of the container within the storage. (It’s set to "synapse" in this case.)

SQL Administrator Login – Uses credentials stored in .env to securely set up SQL authentication.

Create the Synapse Workspace
The begin_create_or_update method starts the creation process.
It waits for completion using .result().

Retrieve and Print the SQL Endpoint
The SQL endpoint is essential for querying data in Synapse.
If the workspace is successfully created, the script prints the SQL endpoint for connection.

Error Handling
If any error occurs, it prints an error message and raises the exception to halt execution.
Final Notes:

The script follows a structured approach:
✅ Ensure resource group exists → ✅ Create Storage Account → ✅ Create Synapse Workspace.
It implements best practices like using environment variables, authentication with DefaultAzureCredential, and structured error handling.
SQL endpoint retrieval is a crucial step because it's needed to interact with Synapse for querying data.



### data_operations.py 💻

NBA Data Fetching and Azure Blob Storage Upload
This script pulls NBA player data and game stats from the Sports Data API, transforms the data into line-delimited JSON, and uploads it to Azure Blob Storage. Let’s break it down! 🚀

Importing the Necessary Libraries
At the top, we load the required modules:

azure.storage.blob → To interact with Azure Blob Storage.
json → Handles JSON data formatting.
requests → Makes HTTP calls to fetch NBA data.
dotenv → Loads environment variables from the .env file.
os → Accesses environment variables.
📝 Why?
We need these tools to fetch, process, and store the NBA data.

Fetching NBA Data (fetch_nba_data function)
This function retrieves NBA player stats from the API.

How It Works:

Retrieves the API key and endpoint from the environment variables:
```sh
api_key = os.getenv("SPORTS_DATA_API_KEY")
nba_endpoint = os.getenv("NBA_ENDPOINT")
```

The API key gives us permission to access the Sports Data API.
The endpoint is the web address we call to get the NBA data.
Defines headers with the API key:
```sh
headers = {"Ocp-Apim-Subscription-Key": api_key}
```
This is how we authenticate the request.

Makes the HTTP request:
```sh
response = requests.get(nba_endpoint, headers=headers)
```
This line says: “Hey API, give me the NBA data!” 📡
Handles errors:
```sh
response.raise_for_status()
```
If the request fails (e.g., API is down, bad credentials), it raises an exception.
If the request succeeds (status_code == 200), it returns the JSON response.
💡 Quick refresher: APIs allow two systems to communicate—just like a client-server relationship. Here, our Python script is the client, and the NBA API is the server. 🖥️💻

Uploading to Azure Blob Storage (upload_to_blob_storage function)
This function stores the retrieved NBA data in Azure Blob Storage.

Step-by-Step Breakdown

Creates the Blob Service Client:
```sh
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
```
This connects to Azure Storage using the provided connection string.
Defines where to store the data:
```sh
container_name = "nba-datalake"
blob_name = "raw-data/nba_player_data.jsonl"
```
Container Name: "nba-datalake" (Storage bucket for NBA data).
Blob Name: "raw-data/nba_player_data.jsonl" (Specific file path inside the container).
Converts JSON list into Line-Delimited JSON:
```sh
line_delimited_data = "\n".join([json.dumps(record) for record in data])
```
Why? 🧐
Line-delimited JSON makes the data easier to process in Big Data tools.
Similar to how we formatted AWS data before, this ensures our queries work correctly. ✅

Uploads the data to Blob Storage:
```sh
container_client = blob_service_client.get_container_client(container_name)
container_client.create_container()  # Creates the container if it doesn’t exist
blob_client = container_client.get_blob_client(blob_name)
blob_client.upload_blob(line_delimited_data, overwrite=True)
```
Creates the storage container (if it doesn’t already exist).
References the specific blob file (nba_player_data.jsonl).
Uploads the processed data, overwriting any existing file.
💡 Important! Running this script multiple times overwrites the previous file.

Summary

✅ Fetches NBA player stats via an API request.

✅ Formats the data into line-delimited JSON.

✅ Uploads the processed data to Azure Blob Storage.

🚀 Now you have a structured NBA dataset stored in Azure! 🎯


requirements.txt 💻
This loads up all the necessary dependencies for our project. Keep this updated to avoid any missing package errors.

.gitignore 💻
We ignore the .env file here. Why? Because it holds sensitive info like API keys, Azure subscription IDs, and passwords. No leaks! 🚫

.env 💻
This file is where you input your personal credentials (Azure ID, resource names, etc.). Everything here should be unique to you! No placeholders left behind. Make it error-proof.

 in this repo? 📂

This project is structured and organized for seamless execution.

📌 setup_nba_data_lake.py – Orchestrates the workflow

📌 azure_resources.py – Dynamically creates Azure resources

📌 data_operations.py – Fetches NBA data and uploads it to Blob Storage

📌 .env – Stores environment variables (must be added to .gitignore)

Project Structure

📂 AzureDataLake/

📂 Instructions → Folder with step-by-step guidance

📄 Instructions.md → Full documentation of the project

📄 .env → Holds your environment variables

📄 setup_nba_data_lake.py → Main script for setting up the data lake

📄 azure_resources.py → Script to create Azure resources

📄 data_operations.py → Fetches and uploads NBA data

�� requirements.txt → Python dependencies

📄 .gitignore → Prevents accidental commits of sensitive data

Prerequisites 🔑

✅ 1. Get a Sportsdata.io Account

Sign up at Sportsdata.io (Free account available!)

<img width="1437" alt="sportsio" src="https://github.com/user-attachments/assets/18a2174b-9a2e-4425-8a3c-680361a06318" />



Click on Developers → API Resources → Introduction & Testing

Select NBA as your API

Find "Standings" and grab your API key from the Query String Parameters

Copy this API key—you’ll need it soon!

✅ 2. Set up an Azure Account

<img width="1438" alt="createazureacc" src="https://github.com/user-attachments/assets/14f197a8-042e-479f-8f94-afa6a1bf3ab2" />


✅ 3. Install VS Code Extensions for Azure

Make life easier with these VS Code extensions:

🔹 Azure CLI Tools

🔹 Azure Tools

🔹 Azure Resources

✅ 4. Install Azure SDKs & Python Packages
You’ll need Python and some Azure-specific packages. Run:
```sh
brew install python
python3 -m ensurepip --default-pip
pip install azure-identity azure-mgmt-resource azure-mgmt-storage azure-mgmt-synapse azure-storage-blob python-dotenv requests
```
<img width="1413" alt="ensurepip" src="https://github.com/user-attachments/assets/3f3bf81c-e2f1-4eb6-bdd2-d094ea9e1055" />


Then install all dependencies with:
```sh
pip install -r requirements.txt
```

Let’s Get Started! 🚀

Step 1: Open VS Code & Clone the Repo
```sh
git clone https://github.com/alahl1/Azure-30day--DevOps-Challenge
cd Projects/Week1/AzureDataLake
```

Step 2: Update the .env File
Add these credentials:
✅ Your Sports Data API Key

✅ Your Azure Subscription ID

<img width="964" alt="azuresubscribe" src="https://github.com/user-attachments/assets/484bbf65-1b3d-43fe-927f-e2fa6c3fb465" />


✅ Unique Azure Resource Group Name

<img width="1240" alt="resourcegroup" src="https://github.com/user-attachments/assets/581bdc97-4761-470b-baf0-4566d6b745b0" />


✅ Unique Storage Account Name

<img width="1252" alt="createstoreaccount" src="https://github.com/user-attachments/assets/ccebef6f-c426-4098-81eb-fa1c8096c8a6" />


✅ Unique Synapse Workspace Name

<img width="1337" alt="synapseworkspace" src="https://github.com/user-attachments/assets/064351f7-2188-4402-978e-6ea23762dabd" />


🚫 Leave the Azure Connection String & Synapse SQL Endpoint blank (they’ll be injected automatically)

✅ Create an Admin Username

Step 3: Run setup_nba_data_lake.py
Run this command to set up the environment:
```sh
python setup_nba_data_lake.py
```

<img width="1403" alt="pyset" src="https://github.com/user-attachments/assets/0bacc990-9614-4bc9-9f94-dfd6b6dbb580" />



Step 4: Check for Your Resources
🔍 Azure Portal:

Search for your Storage Account
Under Data Storage, go to Containers
Look for raw-data/nba_player_data.jsonl

<img width="1433" alt="datalakejson" src="https://github.com/user-attachments/assets/1f522bd0-9bea-428a-ba90-7e5b9174c539" />


🔍 Azure CLI:
Run this to list blobs in your container:
```sh
az storage blob list --container-name nba-datalake --account-name <your_storage_account_name> --query "[].name" --output table
```

<img width="1409" alt="jsonputput" src="https://github.com/user-attachments/assets/267bdc4c-29c2-4347-9264-f3c2afd5d0f8" />

Download the file:
```sh
az storage blob download --container-name nba-datalake --account-name <your_storage_account_name> --name raw-data/nba_player_data.jsonl --file nba_player_data.jsonl
```


View the file:
```sh
cat nba_player_data.jsonl
```

<img width="1409" alt="highlights" src="https://github.com/user-attachments/assets/6dd5379d-2398-48c8-9850-265abe95a6c3" />

What We Learned 🎯

✅ How to build a data pipeline using Azure Services

✅ Automating cloud infrastructure with Python

✅ Working with JSON and Line-Delimited JSON (JSONL)

Future Enhancements 🚀

🔄 Automate data refresh using Azure Functions

📡 Real-time NBA data stream with Azure Event Hubs

📊 Power BI dashboards connected to Synapse Analytics

🔐 Secure credentials with Azure Key Vault

You're all set! This workflow fetches NBA data, stores it, and automates the process using Azure. If you follow these steps, your NBA Data Lake will be up and running in no time! ��💯



