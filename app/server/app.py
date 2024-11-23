from fastapi import FastAPI, HTTPException

from server.db.user import get_user_by_id, User
from server.db.common_crud import event_crud
# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Skeleton",
    description="A basic skeleton for a FastAPI project",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notification Service!"}

@app.post("/send-user-creation-notification/{id}")
def send_user_creation_email(id):
    try:
        user: User = get_user_by_id(id)
        return {'data': f'Email sent successfully for user creation {user.name} to {user.email}!'}
    except:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@app.post("/send-event-creation-notification/{id}")
async def send_event_creation_email(id):
    try:
        event = await event_crud.find_by_id(id)
        user_id = event['']
        user: User = get_user_by_id(user_id)
        return {'data': f'Email sent successfully for event creation to creator {user.name} to {user.email}!'}
    except:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@app.post("/send-ticket-creation-notification/{id}")
def send_ticket_creation_email(id):
    return {'data': f'Email sent successfully for ticket creation {id}!'}

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def scheduled_task():
    # Your task logic here
    print(f"Task executed at {datetime.now()}")

# Initialize the scheduler
scheduler = BackgroundScheduler()
# scheduler.add_job(scheduled_task, 'cron', hour=8, minute=0)  # Schedule at 8:00 AM daily
scheduler.add_job(scheduled_task, 'interval', minutes=1)  # Run every 1 minute
scheduler.start()

