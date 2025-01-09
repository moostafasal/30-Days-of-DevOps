import os
import json
import urllib.request
import boto3

def format_standings_data(standings):
    messages = []
    for team in standings:
        rank = team.get("rank", "Unknown")
        team_name = team.get("team", {}).get("name", "Unknown")
        points = team.get("points", "N/A")
        goals_diff = team.get("goalsDiff", "N/A")
        played = team.get("all", {}).get("played", "N/A")
        wins = team.get("all", {}).get("win", "N/A")
        draws = team.get("all", {}).get("draw", "N/A")
        losses = team.get("all", {}).get("lose", "N/A")
        
        messages.append(
            f"{rank}. {team_name}\n"
            f"Points: {points}, Goal Difference: {goals_diff}, Played: {played}, Wins: {wins}, Draws: {draws}, Losses: {losses}\n"
        )
    return "\n".join(messages)

def lambda_handler(event, context):
    # Get environment variables
    api_key = os.getenv("FOOTBALL_API_KEY")
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
    sns_client = boto3.client("sns")
    
    # Fetch standings data from the API
    league_id = 140  # La Liga league ID
    season = 2023  # Current season
    api_url = f"https://v3.football.api-sports.io/standings?league={league_id}&season={season}"
    
    headers = {
        "x-rapidapi-host": "v3.football.api-sports.io",
        "x-rapidapi-key": api_key,
    }
    
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(json.dumps(data, indent=4))  # Debugging: log the raw data
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return {"statusCode": 500, "body": "Error fetching data"}
    
    # Process standings
    standings = (
        data.get("response", [])[0]
        .get("league", {})
        .get("standings", [[]])[0]  # Access the first group of standings
    )
    
    if not standings:
        final_message = "No standings data available for La Liga."
    else:
        final_message = format_standings_data(standings)
    
    # Publish to SNS
    try:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=final_message,
            Subject="La Liga Standings"
        )
        print("Message published to SNS successfully.")
    except Exception as e:
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": "Error publishing to SNS"}
    
    return {"statusCode": 200, "body": "Standings data processed and sent to SNS"}
