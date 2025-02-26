# NCAA Highlight Processor Azure! 🏀

We're diving into another Azure project, building an NCAA Highlight Processor! This project will fetch real-time game highlights, process them, and store them within our Azure storage ecosystem.

## 🔍 Overview

We start with our Request API, which makes an HTTP request to fetch data from an external API. Remember 💡 an API is an endpoint we interact with to retrieve data stored outside our system. In this case, we’ll pull NCAA game highlights and store the data in an Azure Blob Storage container in JSON format.

JSON files contain structured data such as video URLs, player details, and game stats. We’ll parse these JSON files to extract the specific video URLs we need, download those videos, and store them in Azure Blob Storage under a separate folder path. 📁

Since Azure can be tricky with IAM and access management, we’ll use Microsoft Entra ID (formerly Azure AD) to authenticate and communicate securely with all the services in this project. Now, let's break down the source code and how each part contributes to our project! 👨🏾‍💻

## 📝 Code Breakdown

### 📌 .env File

The .env file stores environment variables, so we can manage key configurations in one place without hardcoding values.

Key configurations:

✅ API URL: The endpoint for fetching NCAA highlights

✅ RAPID API host: Defines the API service provider

✅ API Key: Required for authentication (must be updated)

✅ Azure Subscription ID: Identifies our Azure environment

✅ Resource Group: Organizes our Azure resources

✅ Location: We'll use EASTUS2

✅ Azure Blob Storage Paths: Defines where the JSON files and processed videos are stored

✅ Retry Logic: Defines retry attempts and delay intervals to prevent failures due to temporary issues

Our script will dynamically inject storage account details into this file, ensuring everything stays up to date. This keeps our workflow automated and scalable.

### 🏗️ create_storage_account.py

This script dynamically creates an Azure Storage Account and updates the .env file with the generated storage account name and primary key.

Key functions:

🔹 generate_storage_account() → Generates a unique storage account name (lowercase letters + numbers)

🔹 update_env_file() → Updates the .env file with the new storage account name and key

🔹 create_storage_account() →

Retrieves Azure Subscription ID, Resource Group, and Location

Creates the Resource Group if it doesn’t exist

Creates the Storage Account using Standard LRS (Locally Redundant Storage)

Fetches and updates the primary storage key

The script ensures that our storage account is ready before any processing begins. This is a critical prerequisite for our project!

### ⚙️ config.py

This script loads environment variables from the .env file and ensures any updates (such as new storage keys) are reflected immediately.

Key function:

🔹 load_dotenv() → Forces a reload of environment variables, ensuring dynamic updates without needing to restart the terminal.

Simple but powerful! 🚀

### 📡 fetch.py

This script retrieves data from the API and stores it in Azure Blob Storage.

Key functions:

🔹 Fetch highlights from the API → Uses requests to make an authenticated API call

🔹 Parse JSON response → Converts JSON data into a Python dictionary

🔹 Upload JSON data to Azure Blob Storage →

Establishes a connection using the storage account key
Checks if the container exists; if not, creates it dynamically
Stores the JSON file under a specific blob path
If the request fails, the script automatically retries based on the retry settings in .env. This ensures reliability!

### 🎥 process_one_video.py
This script downloads video highlights from the API and saves them to Azure Blob Storage.

Key functions:

🔹 Fetch JSON file from Blob Storage → Retrieves previously stored highlight data

🔹 Extract video URLs → Parses JSON and identifies the video files we need

🔹 Download & Upload videos →

Fetches video content

Saves it under a separate path in Azure Blob Storage
This ensures that our system automatically processes and organizes NCAA highlight videos in the cloud. 🏀

### 💻 run_all.py 

This script acts as the main orchestrator, executing all required scripts in the correct sequence to process NCAA basketball highlight videos. It automates storage setup, API data retrieval, and video processing while handling errors and retry logic.

Key Functionalities

Sequential Execution of Scripts

It ensures that all required scripts (create_storage_account.py, fetch.py, and process_one_video.py) run in the correct order.
Implements subprocess to execute each script independently.

Delay Handling

Introduces delays using time.sleep() between script executions, allowing sufficient time for resources to be created.
Delay settings are configurable through config.py.

Error Handling & Retry Logic

Initializes an attempt counter (attempts = 0).
Retries script execution up to three times if errors occur.
If a script fails after three attempts, an error message is logged, assisting with debugging.

Environment Variable Validation

Ensures that essential configuration variables (like RAPIDAPI_KEY, AZURE_SUBSCRIPTION_ID, etc.) are set correctly.
If an error occurs due to missing or incorrect environment variables, the script will notify the user.

Execution Flow

Storage Setup (create_storage_account.py)
Creates an Azure Storage Account and Blob Container.
Waits 60 seconds to ensure the storage account is ready.

Data Fetching (fetch.py)
Calls the Sports Highlights API from RapidAPI.
Saves the fetched JSON data into Azure Blob Storage.

Video Processing (process_one_video.py)
Downloads the JSON file from Blob Storage.
Extracts video URLs and downloads videos.
Uploads processed videos back to Blob Storage.

Final Output
If all steps succeed, the process completes successfully.
If an error occurs, it logs details for debugging.
Prerequisites

Before running the script, ensure the following:

RapidAPI Account
Sign up at RapidAPI and retrieve an API key.
The project uses NCAA (USA College Basketball) Highlights API.

Software Requirements
Python 3 (python3 --version)
Git (for cloning the repository)
Azure CLI (az login for authentication)
Retrieve Azure Subscription ID

Run the following command in the terminal to get your subscription ID:
```sh
az account show --query id -o tsv
```
Project Structure
```sh
src/
├── Dockerfile
├── config.py
├── fetch.py
├── create_storage_account.py
├── process_one_video.py
├── requirements.txt
├── run_all.py
├── .env
├── .gitignore
```
Setup & Execution

Step 1: Clone the Repository
```sh
git clone https://github.com//YOUR_GITHUB_REPO_PLACEHOLDER
cd src
```
Step 2: Update the .env File
Add the following credentials:
```sh
RAPIDAPI_KEY=<Your_API_Key>
AZURE_SUBSCRIPTION_ID=<Your_Azure_Subscription_ID>
AZURE_RESOURCE_GROUP=<Your_Resource_Group_Name>
AZURE_BLOB_CONTAINER_NAME=<Your_Container_Name>
```
<img width="1438" alt="rapidapi" src="https://github.com/user-attachments/assets/ef3daff6-c6b3-49c5-891e-16c34ccebb34" />


<img width="1415" alt="resource groups" src="https://github.com/user-attachments/assets/02cc1046-3105-4fd4-a013-fb96637aab8f" />


<img width="1423" alt="storageaccountname" src="https://github.com/user-attachments/assets/8aba2b71-1184-42fc-a35e-6b1f5e1ca7b6" />


<img width="1423" alt="container" src="https://github.com/user-attachments/assets/80bec437-1d65-4b3d-af56-460a670ed074" />


Step 3: Secure the .env File
```sh
chmod 600 .env
```
Step 4: Set Up a Virtual Environment
macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```
Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
<img width="1430" alt="venv" src="https://github.com/user-attachments/assets/279fa105-c64e-4078-93f5-afa01e7e0d20" />


Step 5: Install Dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
<img width="1436" alt="pipinstall" src="https://github.com/user-attachments/assets/4f82bd5b-e42a-465a-b39d-c5c0d09a3581" />


Step 6: Run the Project
```sh
python run_all.py
```
<img width="1415" alt="runallpy" src="https://github.com/user-attachments/assets/616ffb65-9a77-4797-99a2-d9392a1c8cd0" />


Executes create_storage_account.py first.

Waits for the specified delay (e.g., 60 seconds).

Runs fetch.py to fetch API data and upload JSON to Blob Storage.

Runs process_one_video.py to process and upload videos.
Verification

To confirm the JSON and video files were uploaded to Azure Blob Storage, run:
```sh
az storage blob list \
    --account-name <YOUR_STORAGE_ACCOUNT_NAME> \
    --container-name <YOUR_CONTAINER_NAME> \
    --query "[].{name:name}" \
    --output table
```

<img width="1417" alt="allscriptssucess" src="https://github.com/user-attachments/assets/ff51d2f3-43f4-4d2b-8c06-3a58e3e84a78" />


<img width="1408" alt="storageboblast" src="https://github.com/user-attachments/assets/69aaaf5a-c127-4f25-8e66-d17f47e642b7" />


<img width="1395" alt="storageblobhighlight" src="https://github.com/user-attachments/assets/1019f599-0b1c-4c6f-8637-fdf650c2df97"
/>

<img width="1422" alt="firstvideo" src="https://github.com/user-attachments/assets/5e3e2faa-3ee2-4f61-a054-ec21f95fd985" />


<img width="1424" alt="containerhighlightvideo" src="https://github.com/user-attachments/assets/ca8415d0-fef2-432d-ab1f-9fca49dcf104" />


<img width="1416" alt="containerbasketballvideo" src="https://github.com/user-attachments/assets/46270d3c-41e0-4fc9-bd8f-e162cb74872f" />


<img width="1428" alt="firstvideoquicktime" src="https://github.com/user-attachments/assets/de92af6d-b431-4ad3-bdaa-ac1471773daa" />


Key Learnings

Microsoft Entra ID (formerly Azure AD) for authentication and access control.
Azure CLI to manage cloud resources via the terminal.
Azure Storage concepts (Storage Accounts, Blob Containers).
Uploading & Downloading Files in Azure Blob Storage.

Future Enhancements

Deploy the project to Azure VM or Azure Function App for automated execution.
Process multiple videos simultaneously.
Replace Storage Account Key authentication with Managed Identity for better security.

