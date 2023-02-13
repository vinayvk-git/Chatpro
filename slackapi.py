

import requests
import json

SLACK_API_TOKEN = "xoxe.xoxp-1-Mi0yLTE4MjIyNjQ0MTk0NDAtMTc5ODY0MTMwNjAxOS00Nzg5ODQ2NTI5ODMwLTQ3ODE5MTYzMDA4NzEtOTFhMzU1YTVkMzM5YjA1NzRhMGM3Nzk3OTZlMjA0ZDA1NDg0ZDI5OTdlNDJlODZjMTAxMjFlZDU1ZTdkMDU1Ng"
CHANNEL_ID = "VinayRao_test1"

url = f"https://slack.com/api/conversations.history?token={SLACK_API_TOKEN}&channel={CHANNEL_ID}"

response = requests.get(url)
data = json.loads(response.text)

if data["ok"]:
    messages = data["messages"]
    # Do something with the messages
else:
    # Handle error
