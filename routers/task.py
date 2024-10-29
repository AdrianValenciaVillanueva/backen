from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from pymongo.collection import Collection
from bson import ObjectId
from datetime import datetime
from models.task import Task

# Definición del router
router = APIRouter()

# Dependencia para obtener la colección de tareas
def get_tasks_collection() -> Collection:
    from db.client import tasks_collection
    return tasks_collection

# Crear una nueva tarea
@router.post("/tasks/", response_model=Task)
def create_task(task: Task, tasks_collection: Collection = Depends(get_tasks_collection)):
    task_dict = task.dict()
    result = tasks_collection.insert_one(task_dict)
    task_dict["_id"] = str(result.inserted_id)
    return task_dict

# Obtener todas las tareas
@router.get("/tasks/", response_model=List[Task])
def get_tasks(tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

# Obtener una tarea por ID
@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task["_id"] = str(task["_id"])
    return task

#obtener tareas por equipo
@router.get("/tasks/team/{team_id}", response_model=List[Task])
def get_tasks_by_team(team_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"team_id": team_id}))
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

#obtener tareas por usuario asignado
@router.get("/tasks/user/{user_id}", response_model=List[Task])
def get_tasks_by_user(user_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"user_id": user_id}))
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

#obtener tarea pendientes de un usuario por su id
@router.get("/tasks/user/{user_id}/pending", response_model=List[Task])
def get_pending_tasks_by_user(user_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"user_id": user_id, "status": "pending"}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks


#obtener tareas por nombre de usuario
@router.get("/tasks/username/{username}", response_model=List[Task])
def get_tasks_by_username(username: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"username": username}))
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

#obtener todas las tereas de un equipo
@router.get("/tasks/team/{team_id}", response_model=List[Task])
def get_tasks_by_team(team_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"team_id": team_id}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

#obtener tareas pendientes por id_team
@router.get("/tasks/team/{team_id}/pending", response_model=List[Task])
def get_pending_tasks_by_team(team_id: str, tasks_collection: Collection = Depends(get_tasks_collection)):
    tasks = list(tasks_collection.find({"team_id": team_id, "status": "pending"}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

