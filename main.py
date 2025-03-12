from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx


app = FastAPI()

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Notification schema
class Notification(BaseModel):
    Type: str
    Name: str
    Description: str

@app.post("/notifications/")
async def receive_notification(notification: Notification):
    """
    Receives a notification and forwards it to Slack if it's a "Warning".
    """
    if notification.Type == "Warning":
        payload = {
            "text": f"{notification.Name}\n{notification.Description}"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(SLACK_WEBHOOK_URL, json=payload)
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Failed to send to Slack")

    return {"message": "Notification processed"}