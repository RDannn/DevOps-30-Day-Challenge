# SportsDataBackup



🚨 NEW PROJECT ALERT! ‼️ Are you ready?!

Welcome back to another phenomenal project we’re about to create! 🎉

In this project, we’ll be working with AWS DynamoDB, which will back up external data that we’re fetching from our applications. 
Adding more skills to our toolbox, right? 🔨🛠️🧰 We’re continuously expanding our skill set and leveraging AWS resources that we can implement in future projects.

Let’s keep building! 🧱

We’ll also focus on automation, automating data backups and ensuring our architecture for resiliency. 
By integrating these AWS services, we’ll enhance and reinforce our highly available, fault-tolerant architecture, which can be applied to all future projects. Let’s go! 🚀

## Project Overview 🗃️

Just a heads-up, we’ll be using our previous NCAA Game Highlights application that we built with containers. The goal of this project isn’t necessarily to create something entirely new. Instead, we’ll focus on backing up data we already have while learning new strategies and approaches that we can apply to future architectures. 
This will essentially follow the same NCAA Game Highlights architecture, but with a few new updates and iterations. 
Remember in our original NCAA Game Highlights project, we grabbed/fetched one enhanced video? Well, with this project, guess what?! We’ll be grabbing between 1-10 videos! �� Amazing, right?!
You might be wondering… how will we do this? 🤔 Well, this time, we’ll be working with more files within the data, which will allow us to pull more media/videos!

## Storage & Backup Plan

Keep in mind, the data will be backed up to two places. Think of it as two storage locations 🗄️:

1️⃣ Amazon S3 – Storing video files

2️⃣ DynamoDB – Keeping backup metadata

We never really dove into DynamoDB for backups before, but this is our chance! We’ll explore its capabilities in-depth with this project.

Enhancing Media Quality

Once again, we’ll be using AWS Elemental MediaConvert to convert and enhance our media/video files. 
🎥 Elemental will boost the video and audio quality of our files for a more refined output! 📹📼


## Implementing new AWS Services💻


### DynamoDB: Creating Our Table & Features🗄️

DynamoDB is awesome! It is a serverless NoSQL database that works off of key-value pairs! 
It scales automatically and can store millions of records, making it perfect for high-read and high-write applications! 📉

It has low latency, basically, think of this as the time it takes to complete an action over a long path, but DynamoDB does it super fast! 
For example, fetching and writing our data files as backups and then pulling them whenever we need them. Super cool, right?!

Real-world applications benefit from DynamoDB’s fast read and write features. But what if the data keeps increasing? Will this slow down the database? 
No! DynamoDB has auto-scaling, so as data grows, it automatically adjusts capacity up or down to handle the load!

### Cost Efficiency💳

Another great feature is cost savings! We don’t have to manually provision resources—we only pay for what we use! Basically, you pay for what you use! 
You get what you pay for! LOL 🤑💸

### High Availability & Multi-Region Replication

DynamoDB is also highly available, with multi-region replication, which is crucial for this project! What if one region goes down? Say there’s an outage, no worries! 
With replication across multiple regions, DynamoDB remains resilient and keeps running, so our end users won’t even notice a thing! 🤯

### Data Storage & Backups

Every time a new sports highlight is fetched, it will be stored in our database! 
Each highlight entry will include a unique primary key, like event date, league name, URL, metadata, etc.

Now, let’s dive deeper into backups:

Point-in-Time Recovery (PITR): Provides continuous backups for up to 35 days, protecting against accidental deletion, outages, etc.

Scheduled Backups: Allows backups to be retained beyond 35 days by setting up automated backups.
You may ask: Why don’t we just run backups every minute, every hour? 
Well, simply put—💸💰 money! Things cost, and backups aren’t free! So as architects and engineers, what should we do? 👷🏾‍♂️

Let’s think 💡 and apply best practices! Would it make sense to schedule backups only when we fetch and store new data? Correct! ✅

We know men’s NCAA basketball games happen Tuesday-Sunday, and women’s games happen Monday-Sunday (skipping Wednesday). 
🏀⛹🏽‍♂️⛹🏾‍♀️ Why not schedule backups around game times to capture highlight data? Pretty cool, right?! 😎

As soon as data is brought in, we take a snapshot and back it up for long-term storage. Bingo! 👨🏾‍💻 You’re thinking like an engineer! 
Great job putting on your architect hat! 👷��‍♂️

### Import/Export to S3

Another cool feature, DynamoDB can import/export data to S3! You can send your database data directly to an S3 bucket for further storage, analysis, or archiving. 
Pretty cool! 🚀

### Cloudwatch: Logging & Troubleshooting👨🏾‍💻

We will also be using Amazon CloudWatch to monitor and log the actions of our resources and services. 
CloudWatch collects and analyzes logs, metrics, and events from AWS services like EC2, Lambda, and API Gateway, providing real-time insights into system performance. 
This enables us to detect errors, troubleshoot issues, and ensure our services run smoothly. With CloudWatch, we can set up alarms to receive notifications when something goes wrong, automate actions based on predefined thresholds, and visualize performance data using dashboards. 
CloudWatch Logs allow us to store and analyze application and system logs, while CloudWatch Metrics help track key performance indicators such as CPU utilization and error rates. 
Overall, CloudWatch plays a crucial role in keeping our AWS environment optimized, secure, and reliable.


## Code Breakdown: 💻

### .env💻

Setting Up Environment Variables

Everything starts with the environment variables. We already know how these work, this is where you input your unique values to update the placeholders in your environment variable file.

🚀 This is all specific to YOU and your project.

For the containers from our previous NCAA Game Highlights project, you can reuse the same security groups and subnet we deployed earlier.

✅ Want a fresh setup? You can redo the lab if needed. But if you still have your last lab’s resources, feel free to reuse them.


💡 Why use an environment variable file (.env)?
To avoid hardcoding sensitive data in our scripts!

We’ll also introduce something new—GetText—which allows us to swap out variables dynamically within our templates.

### Understanding the .env File

This file contains all the necessary environment variables needed for our sports highlights backup system to function correctly. It covers AWS account details, ECS task settings, API credentials, S3 storage, IAM roles, and CloudWatch logging.

1️⃣ AWS Account & Region Details

These define the AWS account and region where all resources will be deployed.

AWS_ACCOUNT_ID=<Your-AWS-Account-ID>  # Your unique AWS account number  

AWS_REGION=us-east-1  # The primary region where resources will be deployed  

AWS_DEFAULT_REGION=us-east-1  # Ensures the default region is the same as the working region  

🔹 Why it matters?
This ensures that all AWS commands and deployments are executed in the correct AWS account and region.

2️⃣ Task & Container Details (ECS Configuration)

These settings define how the ECS task runs, the execution roles, and the container image location.

TASK_FAMILY=sports-backup-task  # The ECS task definition name  

EXECUTION_ROLE_ARN=arn:aws:iam::<Your-AWS-Account-ID>:role/ecsTaskExecutionRole  # IAM role for ECS task execution  

TASK_ROLE_ARN=arn:aws:iam::<Your-AWS-Account-ID>:role/ecsTaskExecutionRole  # IAM role for the running container  

TASK_CPU=512  # CPU units allocated to the task (512 = 0.5 vCPU)  

TASK_MEMORY=1024  # Memory allocated to the task (1 GB RAM)  

CONTAINER_NAME=sports-backup-container  # The name of our container in the task  

ECR_IMAGE=<Your-AWS-Account-ID>.dkr.ecr.us-east-1.amazonaws.com/sports-backup:latest  # The latest container image stored in AWS ECR  

🔹 Why it matters?

This ensures our ECS task has the right resources, is linked to the correct IAM roles, and runs the latest version of our sports-backup container.

3️⃣ Application-Specific Variables

These define the API source, credentials, storage locations, and processing settings.

API_URL=https://sport-highlights-api.p.rapidapi.com/basketball/highlights  # API endpoint to fetch highlights  

RAPIDAPI_HOST=sport-highlights-api.p.rapidapi.com  # Host URL for the API service  

RAPIDAPI_KEY=<Your-RAPIDAPI-Key>  # Authentication key for the API  

AWS_ACCESS_KEY_ID=<Your-AWS-Access-Key>  # AWS access key for authentication  

AWS_SECRET_ACCESS_KEY=<Your-AWS-Secret-Access-key>  # AWS secret key for authentication  

S3_BUCKET_NAME=<your-alias>newhighlight-final  # S3 bucket where media files are stored  

LEAGUE_NAME=NCAA  # The sports league we're fetching highlights for  

LIMIT=10  # Number of highlights to retrieve  

MEDIACONVERT_ENDPOINT=<Your-MediaConvert-Endpoint>  # AWS Elemental MediaConvert endpoint  

INPUT_KEY=highlights/basketball_highlights.json  # Input file location in S3  

OUTPUT_KEY=videos/first_video.mp4  # Output file location in S3  

🔹 Why it matters?
These values ensure our app knows where to pull sports highlights from, how to process them, and where to store the results.

4️⃣ Timers & Delays

These settings control retry mechanisms and script timing to handle API failures or AWS processing delays.

RETRY_COUNT=3  # Number of retry attempts if an API call fails  

RETRY_DELAY=30  # Time (in seconds) to wait before retrying  

WAIT_TIME_BETWEEN_SCRIPTS=60  # Delay (in seconds) between script executions  

🔹 Why it matters?
Prevents the system from failing too quickly if API calls or AWS services take longer to respond.

5️⃣ IAM Roles (Permissions for AWS Services)
These IAM roles grant permissions for ECS event handling and MediaConvert processing.

EVENTS_ROLE_ARN=arn:aws:iam::<Your-AWS-Account-ID>:role/ecsEventsRole  # Role for ECS event-driven execution  

MEDIACONVERT_ROLE_ARN=arn:aws:iam::<Your-AWS-Account-ID>:role/HighlightProcessorRole  # Role for AWS MediaConvert processing  

🔹 Why it matters?
These roles allow ECS to trigger tasks and AWS MediaConvert to process video files securely.

6️⃣ DynamoDB Table (For Data Storage & Tracking)

DYNAMODB_TABLE=SportsHighlights  # DynamoDB table where highlight data is stored  

🔹 Why it matters?
Stores metadata about processed highlights, ensuring we can track what has been processed already.

7️⃣ CloudWatch Logging (Monitoring & Debugging)

AWS_LOGS_GROUP=/ecs/sports-backup  # The CloudWatch Logs group for this ECS task  

AWSLOGS_STREAM_PREFIX=ecs  # Prefix for log streams (helps organize logs)  

🔹 Why it matters?
Keeps logs organized and easily accessible for monitoring and troubleshooting issues.

8️⃣ ECS Cluster & Networking Details

These settings define where the ECS task runs and its networking setup.

ECS_CLUSTER=sports-backup-cluster  # The ECS cluster where the task runs  

ECS_EVENTS_ROLE=ecsEventsRole  # Role for ECS event-driven executions  

TASK_REVISION=1  # Task definition version (updates with new changes)  

SUBNET_ID=subnet-<Your-SubnetId>  # Subnet where the task runs  

SECURITY_GROUP_ID=sg-<Your-SecurityGroupId>  # Security group applied to the task  

🔹 Why it matters?

Ensures our ECS tasks run inside the correct VPC, with the right security settings to keep the system safe.

Final Thoughts

This .env file acts as the brain of our deployment, without it, our system wouldn’t know where to pull data, store files, or process tasks! 
Every value here plays a critical role in running a smooth, automated highlight backup system.

✅ No hardcoded credentials

✅ Clear separation of responsibilities

✅ Easily configurable & reusable

🔥 Now, with these settings in place, we’re ready to launch the full pipeline! 🚀

## Step 1: Create & Configure the .env File

🔎 Find & Replace the following values:

Your-AWS-Account-ID = aws sts get-caller-identity --query "Account" --output text  
Y
our-RAPIDAPI-Key = [Your API Key]  

Your-AWS-Access-Key = [Your AWS Access Key]  

Your-AWS-Secret-Access-Key = [Your AWS Secret Access Key]  

S3_BUCKET_NAME = your-alias  

Your-MediaConvert-Endpoint = aws mediaconvert describe-endpoints  

SUBNET_ID = subnet-xxxxx  

SECURITY_GROUP_ID = sg-xxxxx  

## Step 2: Get Your Subnet ID & Security Group ID

1️⃣ Go to the GitHub repo 📁 and open the resources folder.

2️⃣ Copy the entire contents of the provided script.

3️⃣ In AWS CloudShell or your VS Code terminal:

Create a new file called vpc_setup.sh.

Paste the copied script into the file.

4️⃣ Run the script:

bash vpc_setup.sh

5️⃣ The output will provide the Subnet ID and Security Group ID—copy & paste these values into your .env file under SUBNET_ID and SECURITY_GROUP_ID.

## Step 3: Load Your Environment Variables

Run the following command to load your .env file into the terminal:
```sh
set -a
source .env
set +a
```
(Optional) Verify that your variables are correctly loaded:
```sh
echo $AWS_LOGS_GROUP
echo $TASK_FAMILY
echo $AWS_ACCOUNT_ID
```
🔥 And that’s it! We’re all set up! Now we can move forward with deploying and running our updated NCAA Game Highlights backup system.

💡 Key Takeaways:

✅ No hardcoded secrets – environment variables keep things secure!

✅ Efficient setup – reuse resources or spin up new ones as needed!

✅ Backup strategy – DynamoDB + S3 for redundancy!



🛠️ Let’s keep building and breakdown config.py next! 🚀

## config.py💻

🔹 API & Fetch Settings (Where we pull data from)

API_URL → The endpoint for fetching sports highlights

RAPIDAPI_HOST → The API provider’s host

RAPIDAPI_KEY → Must be set at runtime (no default for security)

DATE → Defaults to today’s date (YYYY-MM-DD format)

LEAGUE_NAME → Defaults to NCAA, can be changed

LIMIT → Max number of highlights to fetch (default: 10)

🔹 AWS & S3 (Where we store processed data)

S3_BUCKET_NAME → The S3 bucket where files are stored

AWS_REGION → Defaults to us-east-1 unless changed

🔹 DynamoDB (Tracking what’s processed)

DYNAMODB_TABLE → Stores metadata for processed highlights

🔹 MediaConvert (Handles video processing)

MEDIACONVERT_ENDPOINT → AWS endpoint for video conversion

MEDIACONVERT_ROLE_ARN → IAM role that grants permissions to MediaConvert

�� Video Storage in S3 (Where processed videos are saved)

INPUT_KEY → Default input file for highlights (basketball_highlights.json)

OUTPUT_KEY_PREFIX → Folder where output videos will be stored (videos/)

🔹 Retry & Delay Settings (Prevents failures from breaking the process)

RETRY_COUNT → Will retry failed API calls up to 3 times

RETRY_DELAY → Waits 30 seconds before retrying

WAIT_TIME_BETWEEN_SCRIPTS → Pauses 60 seconds before running the next script

🔥 This config file ensures everything runs dynamically without hardcoding values. By using environment variables, we keep it flexible, secure, and easy to update! 🚀

### fetch.py💻

🏀 Fetching & Processing Basketball Highlights

🔹 Dependencies

Uses boto3 for AWS interactions (S3 & DynamoDB)

Uses requests for API calls

Pulls configs from config.py

### 🔍 Fetching Highlights from API (fetch_highlights())

Calls RapidAPI to get basketball highlights

Uses query parameters (DATE, LEAGUE_NAME, LIMIT)
S
ends headers (RAPIDAPI_KEY, RAPIDAPI_HOST)

Handles request exceptions & returns results

✅ Success: Prints confirmation & returns highlights

❌ Failure: Logs the error & returns None

💾 Saving to S3 (save_to_s3())

Checks if S3 bucket exists

If not, creates it (handles us-east-1 separately)

Uploads highlights as JSON

Stores in S3 under highlights/basketball_highlights.json

Prints success message

✅ Success: JSON file saved in s3://{S3_BUCKET_NAME}/highlights/

❌ Failure: Logs error

🗄️ Storing in DynamoDB (store_highlights_to_dynamodb())

Connects to DynamoDB table (DYNAMODB_TABLE)

Goes through highlight records

Stores each highlight using id (or fallback to url)

Adds fetch_date for tracking

✅ Success: Logs each stored record

❌ Failure: Logs error

🚀 Processing Everything (process_highlights())

Fetch highlights

Save to S3

Store in DynamoDB

📌 Runs automatically if script is executed directly (__name__ == "__main__")

🔥 This script automates the process of fetching, storing, and saving basketball highlights, ensuring seamless AWS integration! 🚀

## mediaconvert_process.py💻

🎬 AWS MediaConvert Video Processing Script

🔹 Dependencies

Uses boto3 to interact with AWS MediaConvert

Loads configurations from config.py

🎞️ Creating a MediaConvert Job (create_job())

Initialize MediaConvert Client

Connects to MediaConvert using AWS_REGION & MEDIACONVERT_ENDPOINT

Define Input & Output Paths

Input: s3://{S3_BUCKET_NAME}/videos/first_video.mp4

Output: s3://{S3_BUCKET_NAME}/processed_videos/

Configure MediaConvert Job Settings

Input Handling: Selects default audio

Output Settings:

Format: MP4

Video Codec: H.264 (5 Mbps, CBR, Main Profile)

Audio Codec: AAC (64 Kbps, Stereo, 48 kHz)

Submit Job to MediaConvert

Uses MEDIACONVERT_ROLE_ARN

Disables acceleration

Sets status updates every 60 seconds

✅ Success: Logs job details in JSON format

❌ Failure: Logs error message

🚀 Execution
📌 Runs automatically if executed directly (__name__ == "__main__")

🔥 This script automates video processing via AWS MediaConvert, ensuring optimized MP4 output stored in S3! 🚀

## process_videos.py💻

AWS S3 Video Processing Script
🔹 Dependencies

Uses boto3 to interact with AWS S3

Uses requests to download videos from URLs

Loads configurations from config.py

🎞️ Processing Video Highlights (process_videos())

Retrieve Highlights JSON from S3

Loads video metadata from INPUT_KEY in S3

Extracts URLs from "data" field

Process Each Video

Skips records without video URLs

Downloads each video via requests.get()

Uses BytesIO to store video data

Upload Videos Back to S3

Saves with unique filenames (highlight_0.mp4, highlight_1.mp4, etc.)

Uploads to S3 under OUTPUT_KEY_PREFIX

Sets Content-Type to "video/mp4"

✅ Success: Logs uploaded video locations

❌ Failure: Prints error message

🚀 Execution
📌 Runs automatically if executed directly (__name__ == "__main__")

🔥 This script automates video fetching, downloading, and uploading to AWS S3 for further processing! 🚀


## run_all.py💻

🚀 Automated Video Processing Pipeline

🔹 Purpose: Orchestrates multiple AWS-based scripts with automatic retries and delays to ensure smooth execution.

⚙️ Pipeline Execution Flow
1️⃣ Fetch Data & Store in AWS (fetch.py)

Retrieves video metadata
Saves JSON data to S3 and DynamoDB
2️⃣ Process Videos (process_one_video.py)

Downloads and uploads videos to S3
3️⃣ Transcode Videos (mediaconvert_process.py)

Uses AWS Elemental MediaConvert to encode videos
🔄 Retry Logic & Delays (run_script())

✅ Retries on failure (up to RETRY_COUNT times)

⏳ Waits RETRY_DELAY seconds between retries

⏲ Adds WAIT_TIME_BETWEEN_SCRIPTS between steps for AWS resource stability

🏗 Execution

📌 Runs sequentially when executed directly (__name__ == "__main__")

🔥 Ensures reliability in AWS-based video processing workflows! 🚀

Amazing! We've thoroughly broken down our code, explained why we're using it, and how it interacts with each of our services. 
Now, let's dive into the IAM roles needed to run our services and resources!🚀

# Roles👩🏽‍💻👨🏾‍💻

## ecsEventsRole-Policy🧑🏾‍💻

We start by breaking down our ECS events role. This role does the following:

✅ Allows ECS Task Execution – Grants permission to run ECS tasks (ecs:RunTask) and check their status (ecs:DescribeTasks).

✅ Passes IAM Roles to ECS – Lets our services assign a specific IAM role (iam:PassRole) to ECS tasks so they have the right permissions to operate.

🌍 Applies to All ECS Tasks – The Resource: "*" means these permissions apply to any ECS task in our AWS account.

This role helps for automating and managing our ECS workloads effectively! 🚀 

## ecsEventsRole-Trust🧑🏾‍💻

🔑 Allows ECS Tasks to Assume This Role – Grants permission for Amazon ECS tasks (ecs-tasks.amazonaws.com) to use this role.

🔄 Enables Secure Access – Uses sts:AssumeRole so ECS tasks can temporarily take on the role and get the permissions they need.

This role is a must-have for ECS tasks to interact securely with other AWS services! 🚀

## ecsTarget🧑🏾‍💻

🔹 Targets an ECS Cluster – This rule is set up to trigger tasks inside the specified ECS cluster (${ECS_CLUSTER}).

🔑 Uses a Specific IAM Role – It runs with the permissions of ${ECS_EVENTS_ROLE}, ensuring the task can execute properly.

🚀 Runs a Fargate Task – It launches a Fargate task (${TASK_FAMILY}:${TASK_REVISION}) with TaskCount: 1, meaning one instance runs at a time.

🌐 Custom Network Configuration – The task runs inside specific subnets (${SUBNET_ID}) and security groups (${SECURITY_GROUP_ID}) with a public IP assigned.
This setup ensures that an ECS task is triggered automatically with the right permissions, networking, and Fargate execution! 🔥

## s3_dynamodb_policy🧑🏾‍💻

📂 S3 Bucket Access – Allows listing (ListBucket) the contents of ${S3_BUCKET_NAME}.

📥📤 S3 Object Permissions – Grants access to Get, Put, and Delete objects inside the bucket (${S3_BUCKET_NAME}/*).

📊 DynamoDB Table Access – Provides permissions to interact with ${DYNAMODB_TABLE}, allowing:

PutItem (Add new data)

GetItem (Retrieve specific data)

UpdateItem (Modify existing records)

Query & Scan (Search through data efficiently)

This policy ensures the role can fully manage files in S3 and interact with a DynamoDB table, making it a solid setup for a data processing pipeline! 🚀

taskdef.template 🧑🏾‍💻

🔍 S3 Bucket Access – Allows listing (ListBucket) all objects inside ${S3_BUCKET_NAME}.

📥📤 S3 Object Actions – Grants full control over objects in the bucket (${S3_BUCKET_NAME}/*), including:

GetObject (Download files)

PutObject (Upload files)

DeleteObject (Remove files)

📊 DynamoDB Table Permissions – Provides access to ${DYNAMODB_TABLE}, allowing:

PutItem – Add new records

GetItem – Retrieve data

UpdateItem – Modify existing entries

Query & Scan – Search the table efficiently

This policy is designed to handle file processing and database interactions seamlessly. 🚀

This describes all of our needed roles to implement and make our architecture work and scale! 
Let's now get into our prerequisites and build this project out! 👷🏾‍♂️🧱🏡



# Prerequisites ⚒️

Before diving into the scripts, make sure you've got the following in place:

Create a RapidAPI Account: 🏀 You'll need a RapidAPI account to access highlight images and videos. 
For this example, we’re using NCAA (USA College Basketball) highlights, which are included for free in the basic plan. 
The Sports Highlights API is the endpoint we’ll be working with.

<img width="1438" alt="rapidapi" src="https://github.com/user-attachments/assets/03f75523-917c-40bb-b9a7-db0ed514f7a4" />

Verify Prerequisites are Installed: 🛠️
Check that the following tools are installed on your system:
Docker: Should be pre-installed in most regions. Run docker --version to verify.
AWS CloudShell: Comes with the AWS CLI pre-installed. Verify by running aws --version.
Python3: Make sure it's installed by running python3 --version.

<img width="1268" alt="docker" src="https://github.com/user-attachments/assets/e2bb272f-91e9-4fc8-9eec-fed150cc3597" />

Install gettext package - envsubst is a command-line utility is used for environment variable substituition in shell scripts and text files. Install according
to your operating system/environment.



### Retrieve Your AWS Account ID ☁️🔑 

To get your AWS Account ID, log in to the AWS Management Console. 
Click on your account name in the top-right corner, and you’ll see your Account ID. 
Copy and save this ID somewhere secure because you’ll need it later when updating the code in the labs.


### Retrieve Access Keys and Secret Access Keys🔑 

In the IAM dashboard, check under Users for your access keys. 
Click on your main user that has the credentials, go to Security Credentials, and scroll down to find the Access Key section. 
If you don’t have a secret access key, you’ll need to create one, as it can’t be retrieved later. Make sure you save it securely!🔑

### Step 3: Create Local Folder and Clone Repository🗂️

Ready to dive in? Let’s set up your local environment and get rolling with this project!

1️⃣ Create a New Folder Fire up your terminal and create a local folder to house your project. For example: mkdir -p "Day7-SportsDataBackup". Now, move into the folder: cd "Day5-ncaa-folderplaceholder"

2️⃣ Clone Your GitHub Repository Head to GitHub and create a repository if you haven’t already. Clone your repository to your local machine. 
For example, my repo is named DevOps-30-Day-Challenge: git clone https://github.com/username-placeholder/DevOps-30-Day-Challenge.git 
After cloning, navigate into your project folder: cd DevOps-30-Day-Challenge

<img width="1415" alt="createrepo" src="https://github.com/user-attachments/assets/87b875d7-477d-4adc-8f3d-f9ae90c9cb04" />

3️⃣ Verify Your Structure Run: ls

Ensure you see the folders you’ve created and cloned, like Day5-ncaa-folderplaceholder. Now we’ll build the file/folder structure locally and push it to GitHub.

Your folder should look like this when you’re done:

```sh
DevOps-30-Day-Challenge/
└── Day7-SportsDataBackup/
    ├── README.md
    ├── src/
    │   ├── resources/
    │   │   ├── .env
    │   │   ├── Dockerfile
    │   │   ├── config.py
    │   │   ├── fetch.py
    │   │   ├── mediaconvert_process.py
    │   │   ├── process_videos.py
    │   │   ├── requirements.txt
    │   │   ├── run_all.py
    │   │   └── taskdef.template.json
    │   ├── roles/
    │   │   ├── ecsEventsRole-policy.template.json
    │   │   ├── ecsEventsRole-trust.json
    │   │   ├── ecsTarget.template.json
    │   │   └── s3_dynamodb_policy.template.json
```

Now would be a great time to set up and create our DynamoDB table, right? 🤔 Let’s do it! Time to dive in! 🤿🏊🏾

## Step 1: Create the DynamoDB table 🫙

Sign in to the AWS console. In the AWS serach box, type DynamoDB. Click "Create table". Name the table "SportsHighlights". For the "Partition key" input "Id". Leave the rest of 
the defaults and click "Create table". The table is now all set to go! 

### Step 2: Create S3 Bucket🪣

We will now need to create the S3 bucket🪣 and its contents. 
Open the Cloudshell Terminal. Input this code and ensure you make your bucket unique. 'aws s3api create-bucket --bucket <your-alias>newhighlight-final --region us-east-1'. 
To verify the bucket input command, 'aws s3 ls'. You should see your bucket listed. Let's continue now setting up the rest of this project!

### Step 2: Set Up and Configure the .env File

Replace the following placeholders with your actual AWS details:

Your-AWS-Account-ID → Run this command to get your account ID:

aws sts get-caller-identity --query "Account" --output text
Your-RAPIDAPI-Key
Your-AWS-Access-Key
Your-AWS-Secret-Access-Key
S3_BUCKET_NAME → Set this to your alias
Your-MediaConvert-Endpoint → Retrieve it with:
aws mediaconvert describe-endpoints
SUBNET_ID and SECURITY_GROUP_ID:
To get these values:

Go to the GitHub repo and locate the resources folder. Copy all its contents.
In AWS CloudShell or your VS Code terminal, create a new file called vpc_setup.sh and paste the provided script inside.
Run the script:
bash vpc_setup.sh
Once executed, you'll see the Subnet_ID and Security_Group_ID values in the output. Copy and paste them into your .env file.
Step 3: Load Environment Variables

To make sure your environment variables are loaded, run:

set -a  
source .env  
set +a  
Optional: Verify the Variables
Run the following to check if they were loaded correctly:

echo $AWS_LOGS_GROUP  
echo $TASK_FAMILY  
echo $AWS_ACCOUNT_ID  
Step 4: Generate Final JSON Files

Use envsubst to replace placeholders in your JSON templates:

envsubst < taskdef.template.json > taskdef.json  
envsubst < s3_dynamodb_policy.template.json > s3_dynamodb_policy.json  
envsubst < ecsTarget.template.json > ecsTarget.json  
envsubst < ecseventsrole-policy.template.json > ecseventsrole-policy.json  
Optional: Confirm the Replacements
Check the generated files using cat or open them in a text editor to ensure placeholders were replaced correctly.

Step 5: Build and Push Docker Image

1. Create an ECR Repository
aws ecr create-repository --repository-name sports-backup  
2. Log In to ECR
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com  
3. Build the Docker Image
docker build -t sports-backup .  
4. Tag the Image for ECR
docker tag sports-backup:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sports-backup:latest  
5. Push the Image to ECR
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sports-backup:latest  
Step 6: Set Up AWS Resources

1. Register the ECS Task Definition
aws ecs register-task-definition --cli-input-json file://taskdef.json --region ${AWS_REGION}  
2. Create a CloudWatch Logs Group
aws logs create-log-group --log-group-name "${AWS_LOGS_GROUP}" --region ${AWS_REGION}  
3. Attach the S3/DynamoDB Policy to ECS Task Execution Role
aws iam put-role-policy \
  --role-name ecsTaskExecutionRole \
  --policy-name S3DynamoDBAccessPolicy \
  --policy-document file://s3_dynamodb_policy.json  
4. Set Up the ECS Events Role
Create the Role with a Trust Policy

aws iam create-role --role-name ecsEventsRole --assume-role-policy-document file://ecsEventsRole-trust.json  
Attach the Events Role Policy

aws iam put-role-policy --role-name ecsEventsRole --policy-name ecsEventsPolicy --policy-document file://ecseventsrole-policy.json  
Step 7: Schedule the Task with EventBridge

1. Create the Rule
aws events put-rule --name SportsBackupScheduleRule --schedule-expression "rate(1 day)" --region ${AWS_REGION}  
2. Add the Target
aws events put-targets --rule SportsBackupScheduleRule --targets file://ecsTarget.json --region ${AWS_REGION}  
Step 8: Manually Test the ECS Task

Run this command to manually trigger the task:

aws ecs run-task \
  --cluster sports-backup-cluster \
  --launch-type FARGATE \
  --task-definition ${TASK_FAMILY} \
  --network-configuration "awsvpcConfiguration={subnets=[\"${SUBNET_ID}\"],securityGroups=[\"${SECURITY_GROUP_ID}\"],assignPublicIp=\"ENABLED\"}" \
  --region ${AWS_REGION}  
Key Takeaways

Used templates to generate JSON configuration files
Integrated DynamoDB for data storage and backup
Logged events using CloudWatch
Future Enhancements

Export a DynamoDB table to S3 for backups
Automate backup scheduling
Implement batch processing for handling multiple JSON files (e.g., importing 10+ videos at a time)









