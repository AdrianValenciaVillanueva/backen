### Resumen de los Pasos

1. **Clonar el repositorio**: 
    ```bash
    git clone https://github.com/AdrianValenciaVillanueva/backen.git
    cd backen
    ```

2. **Crear y activar un entorno virtual**: 
    ```bash
    python -m venv .venv
    ```
    Esto creará un directorio llamado `.venv` en tu proyecto.

    Activar el entorno virtual:
    ```bash
    .\.venv\Scripts\activate
    ```

3. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar el servidor**: 
    ```bash
    uvicorn main:app --reload
    ```

5. **Acceder a la documentación interactiva**:
    - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

6. **Endpoints principales**: 
    - Crear un nuevo usuario: `POST /users/`
    - Obtener todos los usuarios: `GET /users/`
    - Obtener un usuario por ID: `GET /users/{user_id}`
    - Crear una nueva tarea: `POST /tasks/`
    - Obtener todas las tareas: `GET /tasks/`
    - Obtener una tarea por ID: `GET /tasks/{task_id}`

7. **Contribución**:
    Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

    1. Haz un fork del repositorio.
    2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
    3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
    4. Sube tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
    5. Abre un Pull Request.

8. **Licencia**:
    licencia libre
