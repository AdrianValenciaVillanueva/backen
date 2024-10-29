from fastapi import FastAPI
from routers import user, task

app = FastAPI()

# Incluir los routers
app.include_router(user.router)
app.include_router(task.router)

#cors
from fastapi.middleware.cors import CORSMiddleware

origins = [

    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}