import requests
import json

SLACK_API_TOKEN = "xoxb-your-api-token-here"
CHANNEL_ID = "your-channel-id-here"

url = f"https://slack.com/api/conversations.history?token={SLACK_API_TOKEN}&channel={CHANNEL_ID}"

response = requests.get(url)
data = json.loads(response.text)

if data["ok"]:
    messages = data["messages"]
    # Do something with the messages
else:
    # Handle error
