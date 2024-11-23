from fastapi import FastAPI, HTTPException

from server.db.user import get_user_by_id, User
from server.db.common_crud import event_crud, ticket_crud
# Initialize FastAPI app
app = FastAPI(
    title="Notification service",
    description="Notifications for Event Management System",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notification Service!"}

@app.post("/send-user-creation-notification/{id}")
def send_user_creation_email(id):
    try:
        user: User = get_user_by_id(id)
        data = f'Email sent successfully for user creation {user.name} to {user.email} #{user.mobile}!'
        print(data)
        return {'data': data}
    except:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@app.post("/send-event-creation-notification/{id}")
async def send_event_creation_email(id):
    try:
        event = await event_crud.find_by_id(id)
        user_id = event['creator_id']
        user: User = get_user_by_id(user_id)
        data = f'Email sent successfully for event creation for event name {event['event_name']} to creator {user.name} to {user.email} #{user.mobile}!'
        print(data)
        return {'data': data}
    except:
        raise HTTPException(status_code=404, detail=f"Event data for {id} not found")

@app.post("/send-ticket-creation-notification/{id}")
async def send_ticket_creation_email(id):
    try:
        ticket = await ticket_crud.find_by_id(id)
        event = await event_crud.find_by_id(ticket['event_id'])
        user_id = ticket['user_id']
        user: User = get_user_by_id(user_id)
        data = f'Email sent successfully for ticket creation for event {event['event_name']} to user {user.name} #{user.mobile}!'
        print(data)
        return {'data': data}
    except:
        raise HTTPException(status_code=404, detail=f"Data for {id} not found")
