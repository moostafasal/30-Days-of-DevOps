# La Liga Standings Automation - Day 02 Challenge

This project retrieves the current standings of La Liga (Spanish football league) using an API and sends the information to an Amazon SNS topic weekly. The system is implemented using AWS services such as Lambda, SNS, and EventBridge for scheduling.

## Features

- Retrieves the latest La Liga standings from an external football API.
- Formats the standings data for readability.
- Publishes the formatted data to an Amazon SNS topic for subscribers.
- Automates weekly execution using AWS EventBridge.

## AWS Components

1. **AWS Lambda**
   - Hosts the Python code that fetches, processes, and publishes the standings data.

2. **Amazon SNS**
   - Distributes the standings message to subscribed endpoints (e.g., email, SMS).

3. **AWS EventBridge**
   - Schedules the Lambda function to run weekly.

4. **IAM Role and Policy**
   - Grants the Lambda function permissions to access the SNS topic and the external football API.

## Prerequisites

- AWS Account with access to Lambda, SNS, and EventBridge.
- API Key for the API-SPORTS Football API.
- Python 3.x installed locally (optional, for development).

## Setup Instructions

### Step 1: Create the IAM Role and Policy

Create an IAM Role for Lambda with the following policy attached (save this policy in a file named `policy.json`):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:<region>:<account-id>:<topic-name>"
    },
    {
      "Effect": "Allow",
      "Action": "logs:*",
      "Resource": "arn:aws:logs:<region>:<account-id>:log-group:/aws/lambda/*"
    }
  ]
}
```
### Step 2: Create the SNS Topic

- Create an SNS topic and subscribe email or SMS endpoints to receive notifications.
- Note down the Topic ARN for later use.

### Step 3: Deploy the Lambda Function

1. Create a new Lambda function.
2. Upload the `lambdaFunctionCode.py` file to the Lambda function.
3. Add the following environment variables:
   - `FOOTBALL_API_KEY`: Your API key for the football API.
   - `SNS_TOPIC_ARN`: The ARN of the SNS topic created earlier.
4. Attach the IAM role created in Step 1 to the Lambda function.

### Step 4: Schedule Weekly Execution with EventBridge

1. Open the EventBridge console.
2. Create a new rule with the following settings:
   - **Event Source**: Schedule
   - **Schedule Expression**: `rate(7 days)`
3. Set the target to the Lambda function.

