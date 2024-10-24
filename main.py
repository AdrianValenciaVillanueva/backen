from fastapi import FastAPI
from routers import user, task

app = FastAPI()

# Incluir los routers
app.include_router(user.router)
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}