from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Skeleton",
    description="A basic skeleton for a FastAPI project",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notification Service!"}

@app.post("/send-user-creation-email/{id}")
def send_user_creation_email(id):
    return {'data': f'Email sent successfully for user {id}!'}
