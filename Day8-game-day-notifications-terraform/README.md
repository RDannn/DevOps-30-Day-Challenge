# NBA Game Notification System Using AWS🏀⛹🏽‍♂️

#DevOpsAllStarsChallenge #DevOpsAllStarChallenge

## Project Overview

We are back with another great project! 🚀 This project is all about evolution. We are evolving our skillset and toolkit! 🧰 We are going back to the fundamentals, revisiting what we originally learned, and applying something new to build upon that foundation.

We will take a look at our first week's project, the **Game Day Notifications** project! If you haven’t completed it yet, check out my GitHub repo under **Day2-nba-game-day-notifications**. It has all the detailed steps and a breakdown of how to implement and deploy the project manually. That project focused on **ClickOps**, where we manually clicked through the AWS console to set up resources.

Now, we are taking things up a notch! 🤖 Instead of clicking through the AWS console, we will automate the entire deployment using **Infrastructure as Code (IaC)** with **Terraform**! The original project took about **15-30 minutes** to set up manually. But with **IaC and automation**, our entire infrastructure will be deployed **within seconds**! 😱 Amazing, right?!🤯 So let’s dive into this awesome automation tool! 🤿🏊��‍♀️

## Project Overview

This project is an **alert system** that sends real-time **NBA game day score notifications** to subscribed users via **SMS/Email**. It leverages **Amazon SNS, AWS Lambda, Python, Amazon EventBridge, and NBA APIs** to keep sports fans up-to-date with live game information. The key takeaway? We will **use Terraform to automate the deployment and teardown** of this solution in **seconds**!

## Technical Architecture

Let’s take a look at our architecture diagram for this project:

![nba drawio-1](https://github.com/user-attachments/assets/eadd2ee1-d478-4cc6-88ee-b3bd18bde8ca)


For our **Day2-nba-game-day-notifications** project, we designed an event-driven system:

1. **Amazon EventBridge Rule:** Triggers every **2 hours** to start the process.
2. **AWS Lambda Function:** Retrieves live NBA game data from the **SportsDataIO API**.
3. **JSON Processing:** The API responds in **JSON format**, which our Lambda function processes and converts into a human-readable format.
4. **Amazon SNS (Simple Notification Service):** Receives the formatted game details.
5. **Subscribers (Email/SMS):** Automatically receive game updates when new data is pushed to the SNS topic. 📧📱

How cool is that?! 😎🆒 Now, let’s dive into the tools and technologies used in this project! 🧱

## Features

✅ Fetches live **NBA game scores** using an external API.

✅ Sends **formatted score updates** to subscribers via **SMS/Email** using **Amazon SNS**.

✅ Uses **Amazon EventBridge** to schedule automatic updates.

✅ Designed with **IAM security best practices**, ensuring **least privilege access** for all resources.

## Prerequisites

✔️ Free account with **subscription & API Key** at [SportsData.io](https://sportsdata.io/)

<img width="1437" alt="sportsio" src="https://github.com/user-attachments/assets/726755ae-a415-42b1-aef3-66d7f7091f26" />


✔️ **AWS account** with basic knowledge of **AWS & Python**

✔️ **AWS CLI** installed and configured

✔️ **Terraform CLI (v1.10.5)** installed on your local environment

## Technologies Used

🔹 **Cloud Provider:** AWS  
🔹 **Infrastructure as Code Tool:** Terraform  
🔹 **Core AWS Services:** SNS, Lambda, EventBridge  
🔹 **External API:** NBA Game API (SportsData.io)  
�� **Programming Language:** Python 3.x  
🔹 **IAM Security:**
   - **Least privilege policies** for Lambda, SNS, EventBridge, and Systems Manager  

Let’s build something awesome! 🚀🔥


Step 1: Clone the Repository:
```sh
git clone https://github.com/placholder.git
cd game-day-notifications
```

Step 2: Create the Folder
Run the following command to create the for example Day8-game-day-notifications-terraform folder:
```sh
mkdir Day8-game-day-notifications-terraform
```

Step 3: Navigate Into the Folder
Move into the newly created folder:
```sh
cd Day8-game-day-notifications-terraform
```

Step 4: Create the Required Files
Run the following command to create the files:
```sh    
touch .gitignore README.md game_day_notifications.tf nba_notifications.py nba_notifications.zip
```

Step 5: Verify the Files
Run:
```sh
ls -l
```
Project Structure:
```sh
DevOps-30-Day-Challenge/
│
└── Day8-game-day-notifications-terraform/
    ├── .gitignore
    ├── README.md                           # Project documentation
    ├── game_day_notifications.tf           # Game Day notification Terraform config file
    ├── nba_notifications.py                # Main Lambda function code
    ├── nba_notifications.zip               # Main Lambda function zipped file
```
<img width="905" alt="files" src="https://github.com/user-attachments/assets/deff1a5d-9c0c-4584-82e2-2be8db202130" />


📂 Copy Files Locally & Push to GitHub
To copy all files from your repository locally, use the nano function for each file. Save using Ctrl + O, exit with Ctrl + X, and repeat for each file. Then, push everything to your GitHub repository using:
```sh
git add .
git commit -m "Your commit message"
git push
```

📌 Understanding the Files

game_day_notifications.tf – Our Terraform configuration file for Infrastructure as Code (IaC). This automates resource deployment! 💻

nba_notifications.py & nba_notifications.zip – Both have the same name, but the .zip file is required for Terraform to deploy the Lambda function.

🔒 Secure API Key in AWS Systems Manager Parameter Store
Instead of storing API keys as Lambda environment variables, we use AWS Systems Manager Parameter Store for better security. Run this command to store your API key:

```sh
aws ssm put-parameter --name "nba-api-key" --value "<API_KEY>" --type "SecureString"
```

<img width="1427" alt="secureapi" src="https://github.com/user-attachments/assets/a7f7be0a-a38f-48ae-a21a-bf2046521994" />


🔑 Replace <API_KEY> with your actual key from SportsData.io. Now, our API key is securely stored! 👏🏾

🐍 Updating the Python Code
We modify how the API key is retrieved:

Previously: Environment variable (os.getenv)
Now: Using get_secret to fetch from Parameter Store
This ensures our API key is securely stored and retrieved inside AWS Systems Manager.

🏗️ Terraform Configuration (game_day_notifications.tf)
This file automates our entire AWS infrastructure setup:

AWS Provider & Region (us-east-1)

SNS Topic – nba_game_alerts for sending notifications

IAM Role & Policies – Automatically grants Lambda permissions for:

Interacting with SNS

Logging to CloudWatch

Retrieving secrets from Parameter Store 🔐

Lambda Function – Deployed as a zip file, using lambda_handler as the entry point.

EventBridge Scheduler – Triggers the Lambda function every 2 hours ⏳
📌 No manual IAM role creation needed! Terraform automates everything! 😱

🚀 Deploying with Terraform

1️⃣ Initialize Terraform
```sh
terraform init
```

<img width="1423" alt="terraform init" src="https://github.com/user-attachments/assets/6d72bfd2-4a7a-4ace-b4bb-e92d38ea20e7" />


✅ Sets up the Terraform working directory and backend.

2️⃣ Format Code for Readability
```sh
terraform fmt
```
✅ Ensures clean and structured code.

3️⃣ Validate Configuration
```sh
terraform validate
```

<img width="1336" alt="terraformvalid" src="https://github.com/user-attachments/assets/7f6d468c-4761-4cef-a665-adde6eb245b2" />


✅ Checks for syntax errors.

4️⃣ Preview Changes
```sh
terraform plan
```

<img width="1439" alt="plan12" src="https://github.com/user-attachments/assets/9af77c05-6d42-4039-bde5-eaf41a8d9955" />


✅ See what Terraform will deploy before applying.

5️⃣ Deploy Infrastructure
```sh
terraform apply
```

<img width="1421" alt="applycomplete" src="https://github.com/user-attachments/assets/0bec92c1-b664-424e-af45-e07c90aa4e23" />


✅ Confirms and creates AWS resources in under 15 seconds! 🤯

🎯 Testing in AWS Console

Lambda Function – Search "Lambda" in AWS Console, verify nba_game_alerts is deployed.

<img width="1425" alt="lambdafunct" src="https://github.com/user-attachments/assets/ed68c9ca-884f-406b-b002-5b5a4404d6bf" />

<img width="1433" alt="alert lambda" src="https://github.com/user-attachments/assets/3c323184-9d1b-41dc-94ac-d804c12410d2" />



SNS Topic Subscription – Subscribe your email:

Go to SNS → Topics → nba_game_alerts → Create Subscription

Enter your email, then confirm in your inbox.

<img width="1005" alt="awsubscription" src="https://github.com/user-attachments/assets/95bb23c6-208e-4cb4-b5aa-d802956990a6" />


Manual Lambda Test

In AWS Lambda, create a test event (Test1).

Click Test, and you should get statusCode: 200. 🎉

<img width="1420" alt="status code 200" src="https://github.com/user-attachments/assets/ced93ada-288d-4423-9537-814e15c6a582" />


Check your email – NBA game notifications should be there! 🏀

<img width="1022" alt="gameupdateemail" src="https://github.com/user-attachments/assets/2f3cdca8-8170-41ef-8330-5f105667d5e7" />


⏳ Automating Notifications with EventBridge

Go to EventBridge → Rules

Confirm nba_game_alerts_schedule runs every 2 hours! ⛹🏽‍♂️

<img width="1144" alt="eventbridge" src="https://github.com/user-attachments/assets/86f5d938-0663-43ea-bc15-b256567af580" />


🗑️ Cleaning Up with Terraform

Instead of manually deleting resources, destroy everything with:
```sh
terraform destroy
```

<img width="843" alt="destroycomplete" src="https://github.com/user-attachments/assets/195077fe-f50a-40f2-90fb-706332bbeefd" />


✅ Enter yes to remove all resources.

📚 Key Takeaways

✅ Designed a notification system with AWS SNS & Lambda

✅ Secured API keys using AWS Systems Manager Parameter Store 🔒

✅ Automated workflows with EventBridge

✅ Integrated external APIs into AWS workflows

✅ Fully automated infrastructure deployment using Terraform 💡

Awesome job! You built a fully automated, secure, and scalable NBA notification system! 🚀🏀








