#!/usr/bin/env python3
"""
update_env.py

This script retrieves Terraform outputs in JSON format and updates the .env file
with the new Azure Storage Account details, Subscription ID, and Resource Group:
  - AZURE_STORAGE_ACCOUNT_NAME
  - AZURE_STORAGE_ACCOUNT_KEY
  - AZURE_BLOB_CONTAINER_NAME
  - AZURE_SUBSCRIPTION_ID
  - AZURE_RESOURCE_GROUP

Usage:
    python update_env.py
"""

import json
import subprocess
import os

def get_terraform_outputs():
    """
    Executes 'terraform output -json' and returns the parsed JSON outputs.
    """
    try:
        # Run Terraform command to get outputs as JSON.
        result = subprocess.check_output(["terraform", "output", "-json"])
        outputs = json.loads(result.decode())
        return outputs
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Terraform outputs: {e}")
        return None

def update_env_file(outputs):
    """
    Updates the .env file with the Terraform outputs.

    Args:
        outputs (dict): A dictionary of Terraform outputs.
    """
    env_file = ".env"
    
    # Load current .env lines
    with open(env_file, "r") as f:
        lines = f.readlines()

    # Extract values from Terraform outputs
    storage_account_name = outputs.get("storage_account_name", {}).get("value")
    storage_account_primary_key = outputs.get("storage_account_primary_key", {}).get("value")
    container_name = outputs.get("container_name", {}).get("value")
    azure_subscription_id = outputs.get("subscription_id", {}).get("value")  # New
    azure_resource_group = outputs.get("resource_group_name", {}).get("value")  # New

    if not (storage_account_name and storage_account_primary_key and container_name and azure_subscription_id and azure_resource_group):
        print("Terraform outputs missing required values. Please check your Terraform configuration.")
        return

    # Prepare new .env contents by updating specific lines
    new_lines = []
    for line in lines:
        if line.startswith("AZURE_STORAGE_ACCOUNT_NAME="):
            new_lines.append(f"AZURE_STORAGE_ACCOUNT_NAME={storage_account_name}\n")
        elif line.startswith("AZURE_STORAGE_ACCOUNT_KEY="):
            new_lines.append(f"AZURE_STORAGE_ACCOUNT_KEY={storage_account_primary_key}\n")
        elif line.startswith("AZURE_BLOB_CONTAINER_NAME="):
            new_lines.append(f"AZURE_BLOB_CONTAINER_NAME={container_name}\n")
        elif line.startswith("AZURE_SUBSCRIPTION_ID="):  # New
            new_lines.append(f"AZURE_SUBSCRIPTION_ID={azure_subscription_id}\n")
        elif line.startswith("AZURE_RESOURCE_GROUP="):  # New
            new_lines.append(f"AZURE_RESOURCE_GROUP={azure_resource_group}\n")
        else:
            new_lines.append(line)

    # Write the updated lines back to the .env file
    with open(env_file, "w") as f:
        f.writelines(new_lines)

    print(".env updated with new Azure values:")
    print(f"  AZURE_STORAGE_ACCOUNT_NAME={storage_account_name}")
    print(f"  AZURE_BLOB_CONTAINER_NAME={container_name}")
    print(f"  AZURE_SUBSCRIPTION_ID={azure_subscription_id}")
    print(f"  AZURE_RESOURCE_GROUP={azure_resource_group}")

if __name__ == "__main__":
    outputs = get_terraform_outputs()
    if outputs:
        update_env_file(outputs)

