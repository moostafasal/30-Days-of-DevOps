# NFL Schedule API

Hey there! 👋 Welcome to my NFL Schedule API project. Let me walk you through what I built and how it works.

## What is this project?
This is a web service that gives you NFL game schedules. It's built using Python and runs in the cloud using AWS services. The cool part? It automatically scales up or down based on how many people are using it!

## How it works
1. You send a request to get NFL schedules
2. Our service fetches the latest data from SerpAPI
3. You get back a nice, clean list of upcoming games

## Main parts of the project

### The Application
- Built with Python and Flask
- Gets real NFL data using SerpAPI
- Runs inside a Docker container
- Lives at: `http://sportsapi-alb-9899737.us-east-1.elb.amazonaws.com/sports`

### The Cloud Setup (AWS)
- **Container (ECS & Fargate)**: Runs our application without server headaches
- **Load Balancer**: Handles lots of users at once
- **Container Registry**: Stores our Docker images at `022499031271.dkr.ecr.us-east-1.amazonaws.com/sports-api`

## Want to try it?
Just send a GET request to:
```
http://sportsapi-alb-9899737.us-east-1.elb.amazonaws.com/sports
```

You'll get something like this:
```json
{
  "message": "NFL schedule fetched successfully",
  "games": [
    {
      "away_team": "Chiefs",
      "home_team": "Ravens",
      "venue": "M&T Bank Stadium",
      "date": "2024-01-28",
      "time": "3:00 PM ET"
    }
  ]
}
```

## How to run it yourself

1. Clone this repo
2. Make sure you have:
   - Docker installed
   - AWS CLI set up
   - A SerpAPI key

3. Build and run:
   ```bash
   # Build the Docker image
   docker build -t sports-api .

   # Run it locally
   docker run -p 8080:8080 -e SPORTS_API_KEY=your_key_here sports-api
   ```

4. To deploy to AWS:
   ```bash
   # Login to AWS
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 022499031271.dkr.ecr.us-east-1.amazonaws.com

   # Push to ECR
   docker push 022499031271.dkr.ecr.us-east-1.amazonaws.com/sports-api:latest
   ```

## Important Settings
- The app runs on port 8080
- You need to set SPORTS_API_KEY in your environment
- The service uses AWS Fargate with 2 containers for reliability

## Monitoring
We keep an eye on everything using AWS CloudWatch:
- How many people are using the API
- If there are any errors
- How fast the API responds

## What's Next?
Planning to add:
- Caching to make it faster
- More sports data
- Better error handling
- API documentation

## Need Help?
Feel free to reach out! This project was built by Mostafa Salah as part of learning DevOps practices.

