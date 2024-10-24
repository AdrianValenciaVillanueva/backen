from pymongo import MongoClient
from datetime import datetime


db_client = MongoClient("mongodb+srv://adrianvalencia5250:Adrian2004.@test.cnasm.mongodb.net/?retryWrites=true&w=majority&appName=test")

db = db_client.proyect #conecta a la base de datos test

# Colección de usuarios
users_collection = db['users']

# Colección de tareas
tasks_collection = db['tasks']






# # Ejemplo de inserción de un usuario
# user = {
#     "username": "john_doe",
#     "password": "hashed_password",
#     "is_admin": True,
#     "id_team": "team_123"
# }
# users_collection.insert_one(user)

# # Ejemplo de inserción de una tarea
# task = {
#     "title": "Complete project report",
#     "description": "Complete the final report for the project by the end of the week.",
#     "user_id": "unique_user_id",
#     "team_id": "team_123",  # Código del equipo
#     "created_at": datetime.utcnow(),
#     "updated_at": datetime.utcnow(),
#     "deadline": datetime(2023, 10, 7),
#     "status": "pending"
# }
# tasks_collection.insert_one(task)

# # Ejemplo de consulta de tareas para un equipo específico
# team_id = "team_123"
# tasks = tasks_collection.find({"team_id": team_id})
# for task in tasks:
#     print(task)


