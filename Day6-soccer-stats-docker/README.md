![dockersoccer](https://github.com/user-attachments/assets/b6056872-cd74-4368-bb19-0c1c605d00b5)



# Docker and Soccer Stats: Everything You Need to Know About Containers⚽️

You’re probably wondering: What exactly is a container? What’s it used for? Why do we need them? What do they actually do? My simple answer? Let’s just build one! The best way to learn is by doing. So instead of overthinking, let’s dive in and create a real-world project that shows how containers work in action!

This project is all about getting hands-on with Docker while building a containerized Soccer Stats API. We’ll break it down step by step so you can truly understand how to use containers in real-world applications.

## Project Overview 🗃️

We’re building a containerized Soccer Stats API that fetches real-time player statistics. Once retrieved, the data will be processed and run consistently across any environment. Throughout this project, we’ll cover:

✅ Using environment variables for security and flexibility

✅ Implementing FastAPI to build a lightweight, high-performance API

✅ Dockerizing our application for scalability and portability

✅ Structuring our project properly for maintainability

By the end, you’ll have a fully functional API running inside a container—deployable anywhere, anytime!

## Prerequisites 📋✅

Before we get started, let's set up our project folder and push everything to GitHub. Having a well-organized structure is key to maintaining clean and scalable projects.

1️⃣ Create a New Folder📂

Fire up your terminal and create a local folder to house your project. If you’re using VS Code, iTerm, or any other terminal, navigate to the directory where you want to store this project.

For example, I’m working in my DevOps-30-Day-Challenge repository, I would run:
```sh
cd DevOps-30-Day-Challenge
```
<img width="1438" alt="cddev" src="https://github.com/user-attachments/assets/1584d541-2b62-4d25-8026-417809043b13" />

Then, let’s create our soccer stats container project:
```sh
mkdir soccer-stats-docker
cd soccer-stats-docker
mkdir src tests
touch src/__init__.py src/soccer_stats.py
touch Dockerfile requirements.txt README.md .env
```
<img width="1439" alt="mkdirtouch" src="https://github.com/user-attachments/assets/01cbf03e-3aa1-4264-9b1d-9771c6c57586" />


Ready to dive in? Let’s set up the rest of the project and get rolling! 🚀

2️⃣ Clone Your GitHub Repository
If you haven’t already, head over to GitHub and create a new repository. Once your repo is set up, clone it to your local machine using the following command (replace username-placeholder with your GitHub username):
```sh
git clone https://github.com/username-placeholder/DevOps-30-Day-Challenge.git
```
After cloning, navigate into your project folder:
```sh
cd DevOps-30-Day-Challenge
```
🚀 Push Your Project to GitHub
1️⃣ Initialize Git in Your Project Folder

First, ensure you're inside your project folder. Open your terminal and navigate to your project directory:
```sh
cd (placeholder)DevOps-30-Day-Challenge
```
Then, initialize Git:
```sh
git init
```
2️⃣ Add Your Remote GitHub Repository

Link your local project to the remote GitHub repository (replace username-placeholder with your GitHub username):
```sh
git remote add origin https://github.com/username-placeholder/DevOps-30-Day-Challenge.git
```
3️⃣ Add All Files to Git

To track all files and folders inside your project directory, run:
```sh
git add .
```
4️⃣ Commit Your Changes

Create a commit message describing your initial upload:
```sh
git commit -m "Initial project setup with Docker and soccer stats API"
```
5️⃣ Push to GitHub

Finally, push your project to the main branch:
```sh
git branch -M main
git push -u origin main
```
6️⃣ Verify Your Upload

Go to your GitHub repository in your browser, refresh the page, and you should see all your project files uploaded. 🎉

Now your project is successfully pushed to GitHub! 🔥 Our project structure is now in place! Ready to start coding? 🚀
 

Here's what we've accomplished so far:

✅ Created a main project folder for our soccer stats Docker project using mkdir.

✅ Changed directories into this folder with cd.

✅ Set up a src folder for our code and added __init__.py and soccer_stats.py.

✅ Created essential project files: Dockerfile, requirements.txt, README.md, and .env.

Pretty cool, right? 🔥 Now, let’s break things down further and build out each step! 🏗️

## Required Dependencies🧱

The required dependencies are our building blocks for this project! Via your local machine commmand line, we need to get into our requirements.txt file. Input on the CLI nano requirements.txt. Input these dependencies: 

```sh
fastapi==0.68.1        # Our web framework
uvicorn==0.15.0        # ASGI server for FastAPI
requests==2.26.0       # Making API calls less painful
python-dotenv==0.19.0  # For keeping secrets secret
pytest==6.2.5          # Because we test our code!
```
This information is required for our code, the fast api for framework, uvicorn for the ASGI server for FastAPI, request for making API calls to our required other dependices and resources, python-dotenv for keeping our secrets hidden and encrypted, and finally pytest to of course test our code! 


## Enviroment Variable Lock ♻️🔐

You should have already created a .env file, if not you can do so by inputting in the CLI touch .env. In this .env file input this command:

```sh
RAPID_API_KEY=your_api_key_here
```

1️⃣ DO NOT FORGET! ‼️ ⚠️⛔️ add the .env to your .gitignore file.

2️⃣ DO NOT PUSH YOUR API KEYS to your PUBLIC GITHUB REPO! THIS IS A NO GO! ⛔️📵

### RAPIDAPI_KEY: Create an account on RapidAPI https://rapidapi.com/hub and search for "Sports Highlights." Subscribe to the API and grab your key from the "Subscribe to Test" section.

<img width="1438" alt="rapidapi" src="https://github.com/user-attachments/assets/50136518-1eff-4de6-9676-8deec8e22ecf" />


<img width="1421" alt="sportshighlightrapidapi" src="https://github.com/user-attachments/assets/6a4d7ca5-4d31-498a-ba6a-c5361d5cf02f" />



### Docker Run🏃‍♂️

Ensure your Docker enviroment is running via Docker Desktop for stance. Docker needs to run our Dockerfile, image, etc...

<img width="1264" alt="dockerstart" src="https://github.com/user-attachments/assets/b3a61700-af63-41c9-b385-d3680f92aeca" />


## Code Breakdown: 💻

Let's break down our code 👨🏾‍💻 for this project! This code is needed to implement our project end to end. Let's get back into our soccer_stats.py file via the src folder. cd src. We then need to input the python code for this py file. nano soccer_stats.py. Input this following code: 

soccer_stats.py💻

```sh
# src/soccer_stats.py
import os
import json
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(title="Soccer Stats API")

class SoccerStats:
    def __init__(self):
        self.api_key = os.getenv('RAPID_API_KEY')
        if not self.api_key:
            raise ValueError("RAPID_API_KEY environment variable is not set")
        self.base_url = "https://api-football-v1.p.rapidapi.com/v3"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

    async def get_player_stats(self, player_id: int, season: int = 2023):
        """Fetch player statistics for a given season"""
        try:
            url = f"{self.base_url}/players"
            params = {
                "id": player_id,
                "season": season
            }
            
            response = requests.get(
                url, 
                headers=self.headers, 
                params=params
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"API Error: {response.text}"
                )
            
            data = response.json()
            if not data.get("response"):
                return {"message": "No data found for this player"}
                
            return data
            
        except requests.RequestException as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch player stats: {str(e)}"
            )

    async def get_top_scorers(self, league_id: int = 39, season: int = 2023):
        """Fetch top scorers for a league (default: Premier League)"""
        try:
            url = f"{self.base_url}/players/topscorers"
            params = {
                "league": league_id,
                "season": season
            }
            
            response = requests.get(
                url, 
                headers=self.headers, 
                params=params
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"API Error: {response.text}"
                )
            
            return response.json()
            
        except requests.RequestException as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch top scorers: {str(e)}"
            )

# Initialize our stats class
stats = SoccerStats()

@app.get("/")
async def root():
    """Root endpoint showing available endpoints and basic info"""
    return {
        "message": "Welcome to Soccer Stats API!",
        "version": "1.0",
        "endpoints": [
            "/player/{player_id} - Get player statistics",
            "/topscorers/{league_id} - Get top scorers for a league"
        ],
        "default_league": "Premier League (ID: 39)"
    }

@app.get("/player/{player_id}")
async def get_player(player_id: int, season: int = 2023):
    """Get stats for a specific player"""
    return await stats.get_player_stats(player_id, season)

@app.get("/topscorers/{league_id}")
async def get_top_scorers(league_id: int = 39, season: int = 2023):
    """Get top scorers for a league"""
    return await stats.get_top_scorers(league_id, season)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```
## What This Code Does

This script is a FastAPI-based API that fetches soccer player stats and top scorers using the API-Football service. It loads the API key from environment variables, makes requests to the external API, and serves the data through FastAPI endpoints.

1. Importing Dependencies

At the top, we bring in the necessary libraries:

os → Used to grab environment variables (for storing the API key securely).

json → Helps in handling JSON data (mainly API responses).

requests → Allows us to make HTTP requests to the external API.

FastAPI → Our web framework for setting up the API.

dotenv → Loads environment variables from a .env file.

datetime → Used to generate timestamps (for things like health checks).

2. Loading Environment Variables
```sh
load_dotenv()
```
This pulls in values from a .env file so that sensitive information (like the API key) isn’t hardcoded in the script.

3. Setting Up FastAPI
```sh
app = FastAPI(title="Soccer Stats API")
```
This initializes our API service and gives it a title. If you run this script, you can access FastAPI’s interactive documentation at /docs.

4. Creating the SoccerStats Class

This class handles communication with the API-Football service.

Constructor (__init__)
```sh
class SoccerStats:
    def __init__(self):
        self.api_key = os.getenv('RAPID_API_KEY')
        if not self.api_key:
            raise ValueError("RAPID_API_KEY environment variable is not set")
```
⚽︎It grabs the API key from environment variables.
⚽︎If the key is missing, it raises an error to prevent unauthorized requests.
```sh
self.base_url = "https://api-football-v1.p.rapidapi.com/v3"
```
⚽︎This is the base URL for all API requests.
```sh
self.headers = {
    "X-RapidAPI-Key": self.api_key,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
```
⚽︎These headers authenticate our API requests.

5. Fetching Player Stats (get_player_stats)
```sh
async def get_player_stats(self, player_id: int, season: int = 2023):
```
⚽︎This function fetches statistics for a specific player in a given season (default: 2023).
⚽︎player_id is required, while season defaults to 2023 if not provided.

Building the API Request
```sh
url = f"{self.base_url}/players"
params = {"id": player_id, "season": season}
response = requests.get(url, headers=self.headers, params=params)
```
⚽︎The request is sent to /players with the player ID and season as parameters.

Handling Errors
```sh
if response.status_code != 200:
    raise HTTPException(
        status_code=response.status_code,
        detail=f"API Error: {response.text}"
    )
```
⚽︎If the API doesn’t return a 200 OK status, it throws an HTTP error.

Processing the Response
```sh
data = response.json()
if not data.get("response"):
    return {"message": "No data found for this player"}
```
⚽︎If there’s no valid response, it returns a friendly error message instead of crashing.

6. Fetching Top Scorers (get_top_scorers)
```sh
async def get_top_scorers(self, league_id: int = 39, season: int = 2023):
```
⚽︎This function fetches top goal scorers for a specific league.
⚽︎By default, it fetches Premier League (ID: 39) stats for the 2023 season.

Building the API Request
```sh
url = f"{self.base_url}/players/topscorers"
params = {"league": league_id, "season": season}
response = requests.get(url, headers=self.headers, params=params)
```
⚽︎Sends a request to /players/topscorers with the league ID and season.

Handling API Errors
```sh
if response.status_code != 200:
    raise HTTPException(
        status_code=response.status_code,
        detail=f"API Error: {response.text}"
    )
```
⚽︎If something goes wrong, it throws an HTTP exception instead of returning bad data.

7. Creating the FastAPI Endpoints

Root Endpoint (/)
```sh
@app.get("/")
async def root():
```
⚽︎This is the homepage of the API.
⚽︎It returns basic information about the API and the available endpoints.
```sh
return {
    "message": "Welcome to Soccer Stats API!",
    "version": "1.0",
    "endpoints": [
        "/player/{player_id} - Get player statistics",
        "/topscorers/{league_id} - Get top scorers for a league"
    ],
    "default_league": "Premier League (ID: 39)"
}
```
⚽︎Provides a friendly response for users who visit the API root.

Player Stats Endpoint (/player/{player_id})
```sh
@app.get("/player/{player_id}")
async def get_player(player_id: int, season: int = 2023):
```
⚽︎Takes a player ID and an optional season parameter (default: 2023).
⚽︎Calls the get_player_stats function and returns the result.
```sh
return await stats.get_player_stats(player_id, season)
```
⚽︎Uses await because get_player_stats is an asynchronous function.

Top Scorers Endpoint (/topscorers/{league_id})
```sh
@app.get("/topscorers/{league_id}")
async def get_top_scorers(league_id: int = 39, season: int = 2023):
```
⚽︎Takes a league ID and an optional season parameter (default: 2023).
⚽︎Calls get_top_scorers to fetch and return the data.
```sh
return await stats.get_top_scorers(league_id, season)
```
⚽︎Again, await is used because this function is async.

Health Check Endpoint (/health)
```sh
@app.get("/health")
async def health_check():
```
⚽︎Simple health check to confirm that the API is running.
```sh
return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```
⚽︎Returns "status": "healthy" along with the current timestamp.
⚽︎Useful for monitoring system uptime.
Final Thoughts

This script sets up a complete soccer stats API using FastAPI. It:

✅ Loads API credentials securely

✅ Fetches player stats and top scorers

✅ Provides structured FastAPI endpoints

✅ Includes a health check

Now, we can run this with Uvicorn and start making API calls! Let's get it! 🚀

## Dockerfile💻

```sh
# Use Python 3.9 slim base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.soccer_stats:app", "--host", "0.0.0.0", "--port", "8000"]
```
1.) Use a lightweight Python base image
It starts with python:3.9-slim, which is a minimal version of Python 3.9 to keep the image small and efficient.

2.) Set the working directory
The WORKDIR /app command creates and sets /app as the working directory inside the container, where everything will be stored and executed.

3.) Copy the dependencies file first
The COPY requirements.txt . step copies the requirements.txt file into the container. This is done first to take advantage of Docker’s caching mechanism, meaning dependencies won’t need to be reinstalled unless requirements.txt changes.
4.) Install dependencies
The RUN pip install --no-cache-dir -r requirements.txt command installs all required Python packages listed in requirements.txt, without caching to keep the image lightweight.

5.) Copy the rest of the project files
The COPY . . command copies all remaining project files into the container.

6.)Expose port 8000
EXPOSE 8000 tells Docker that this container will communicate over port 8000 (default for FastAPI when using Uvicorn).

7.) Run the FastAPI application
The CMD command launches the FastAPI app using Uvicorn, making it accessible on 0.0.0.0:8000. This allows it to accept connections from any network interface inside the container.

## Locally Test Environment🧪

Let's locally test our environment via our local machine CLI! Input the following:

```sh
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn src.soccer_stats:app --reload
```
## Running Our Container🫙

Lets now run our container! We have our file structure our code, etc, lets now run this!

Build and run the container:
```sh
# Build the image
docker build -t soccer-stats .
```
<img width="1440" alt="dockerbuild" src="https://github.com/user-attachments/assets/cd948047-3ba6-4fa5-b1c5-8c6eb5de118e" />

```sh
# Run the container: (with your API key)
# On CLI nano .env and input your RAPIDAPI key
docker run -p 8000:8000 --env-file .env soccer-stats
```
<img width="1440" alt="dockerrun" src="https://github.com/user-attachments/assets/6301a5cd-2898-480a-9edd-1e68b38577fd" />

On your terminal copy or click the http://0.0.0.0:800 link. Open this in your browswer. You will your successful results: 
```sh
{
  "message": "Welcome to Soccer Stats API!",
  "version": "1.0",
  "endpoints": [
    "/player/{player_id} - Get player statistics",
    "/topscorers/{league_id} - Get top scorers for a league"
  ],
  "default_league": "Premier League (ID: 39)"
}
```
## Verifying the Setup

After running the API, check your CLI—you should see a "200 OK" status message, confirming a successful connection.

Now, open Docker Desktop and navigate to:

✅ Images – You should see your soccer-stats:latest image listed.

<img width="1271" alt="dockerimage" src="https://github.com/user-attachments/assets/16ef6774-092e-4e39-9b9d-c58250c9946d" />

<img width="1259" alt="soccerlatestimage" src="https://github.com/user-attachments/assets/7d178334-4e33-471e-a4ba-8a9e8298bbcd" />



✅ Containers – Your soccer-stats container should be running on port 8000:8000.

<img width="1440" alt="docker8080" src="https://github.com/user-attachments/assets/75b7f084-0479-4c52-af2d-0f6130c91216" />

<img width="1262" alt="docker container" src="https://github.com/user-attachments/assets/2ad16705-84ca-469d-9ab1-9ded676084c5" />



### API Endpoints

/ - Welcome message and available endpoints

/health - Health check endpoint

/player/{player_id} - Get player statistics

/topscorers/{league_id} - Get top scorers for a league (default: Premier League)

<img width="1440" alt="printstats" src="https://github.com/user-attachments/assets/bcebc394-5807-4290-a0d2-d5cd5890db08" />


🚀 Success! We’ve successfully containerized and deployed our API! Our Dockerfile built an image, created a containerized environment, and pulled real-time soccer stats from an external API. We also tested it locally and got successful results. Keep climbing! 💪🔥

👉 Press CTRL + C in your CLI to stop the running container.

## Debugging Tips 🛠️

Common Issues & Fixes
🔹 Docker Permission Issues
If you encounter permission errors when running Docker commands, try:
```sh
sudo usermod -aG docker $USER
newgrp docker
```
🔹 API Key Issues
If your API isn’t fetching data:

✅ Double-check that your RAPID_API_KEY is correctly set in .env.

✅ Verify that your key is valid on RapidAPI.

✅ Ensure the key is being passed properly to the container.

🔹 Container Access Issues
If your container isn’t running as expected:
```sh
# Check running containers
docker ps  

# View container logs
docker logs <container-id>  

# Access the container shell
docker exec -it <container-id> /bin/bash  
```
## Resource Cleanup 🧹

When you're done, clean up Docker resources to free up space:

# Stop the running container
```sh
docker stop $(docker ps -q --filter ancestor=soccer-stats)

# Remove the container
docker rm $(docker ps -aq --filter ancestor=soccer-stats)

# Remove the image
docker rmi soccer-stats

# Remove all unused containers, networks, and images (use with caution)
docker system prune
```
This ensures that your environment stays clean and optimized for future projects.

🔥 That’s a wrap! You’ve successfully built, tested, and deployed a fully containerized API. Keep pushing forward—this is just the beginning! 🚀💡

Let me know if you need any refinements!











