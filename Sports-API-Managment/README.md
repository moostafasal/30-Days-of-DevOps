# NFL Schedule API

Welcome to the **NFL Schedule API**! 🏈 This project provides real-time NFL game schedules through a simple web service, built for reliability and scalability. Let’s dive into how it works and how you can use it.

---

## 🌟 Overview

The NFL Schedule API is a cloud-native service designed to fetch and deliver NFL game schedules in real-time. It leverages Python, Flask, and various AWS services to ensure smooth operation and scalability.

Key features:
- Fetches live NFL data from **SerpAPI**.
- Scalable architecture with AWS Fargate and Elastic Load Balancer (ALB).
- Delivered through a lightweight **Dockerized** application.

---

## 🚀 How It Works

1. **You make a request** to the API to retrieve NFL schedules.
2. The API uses **SerpAPI** to fetch the latest game data.
3. The response provides a structured JSON with details of upcoming games.

Example response:
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
## 🏗️ Architecture and Components

### Application
- **Framework**: Built using Python and Flask.
- **Data Source**: Integrates with **SerpAPI** for real-time NFL data.
- **Containerized**: Runs inside a **Docker** container for portability and ease of deployment.

### AWS Cloud Infrastructure
- **Amazon ECS with Fargate**: Handles containerized workloads, ensuring scalability.
- **Elastic Load Balancer (ALB)**: Distributes traffic across multiple containers.
- **Amazon ECR**: Stores the Docker images securely.
- **CloudWatch**: Monitors application performance and usage metrics.


-----

## 🌩️ Deploying to AWS

1.**Authenticate with AWS ECR**:
  ```bash
  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 022499031271.dkr.ecr.us-east-1.amazonaws.com
   
```

2.**Push the Docker image**:

```bahs
docker tag sports-api:latest 022499031271.dkr.ecr.us-east-1.amazonaws.com/sports-api:latest
docker push [AWSID].dkr.ecr.us-east-1.amazonaws.com/sports-api:latest

```

3. **Deploy to ECS**:
    
    - Use the AWS Management Console or CLI to create a service using the pushed image.
    - Attach the Elastic Load Balancer for high availability.

----

## ⚙️ Configuration

- **Environment Variable**:  
    `SPORTS_API_KEY`: Your SerpAPI key (required).
    
- **Port**:  
    The app runs on port **8080**.
    
- **AWS Resources**:  
    Uses Fargate with two containers to ensure redundancy.

----
## 📊 Monitoring

The service is monitored using **AWS CloudWatch** for:

- Request volume and usage trends.
- Error rates and response times.
- Container health and resource utilization.

----
### **Future Enhancements**

Add caching for frequent API requests using Amazon ElastiCache Add DynamoDB to store user-specific queries and preferences Secure the API Gateway using an API key or IAM-based authentication Implement CI/CD for automating container deployments
