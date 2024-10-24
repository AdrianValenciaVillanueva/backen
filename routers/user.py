from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pymongo.collection import Collection
from bson import ObjectId
from passlib.context import CryptContext
from models.user import User, UserResponse  # Importa el modelo de respuesta

# Definición del router
router = APIRouter()

# Contexto para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependencia para obtener la colección de usuarios
def get_users_collection() -> Collection:
    from db.client import users_collection
    return users_collection

# Crear un nuevo usuario
@router.post("/users/", response_model=UserResponse)
def create_user(user: User, users_collection: Collection = Depends(get_users_collection)):
    hashed_password = pwd_context.hash(user.password)
    if user.id_team:
        check=check_team_exists(user.id_team,user.is_admin,  users_collection)
    
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    result = users_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return UserResponse(**user_dict)

# Obtener todos los usuarios
@router.get("/users/", response_model=List[UserResponse])
def get_users(users_collection: Collection = Depends(get_users_collection)):
    users = list(users_collection.find())
    for user in users:
        user["id"] = str(user["_id"])
        # Elimina el campo "_id" del elemento userResponse para eliminar redundancia
        del user["_id"]
    return [UserResponse(**user) for user in users]

# Obtener un usuario por ID
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, users_collection: Collection = Depends(get_users_collection)):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user["_id"])
    del user["_id"]
    return UserResponse(**user)

#obtener usuarios por equipo
@router.get("/users/team/{team_id}", response_model=List[UserResponse])
def get_users_by_team(team_id: str, users_collection: Collection = Depends(get_users_collection)):
    users = list(users_collection.find({"id_team": team_id}))
    if not users:
        raise HTTPException(status_code=404, detail="Team not found")
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    return [UserResponse(**user) for user in users]

# comprobar que el equipo existe
def check_team_exists(team_id: str , admin:bool, users_collection: Collection):
    team = users_collection.find_one({"id_team": team_id})
    
    if admin:
        if team:
            raise HTTPException(status_code=400, detail="Team already exists")
        return None
    else:
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        return team
