<<<<<<< HEAD
import os
from utils.logger import log_message

def create_directory(path):
    """Crea un directorio si no existe."""
    try:
        os.makedirs(path, exist_ok=True)
        log_message(f"Carpeta creada: {path}", level="DEBUG")
        return True
    except OSError as e:
        log_message(f"Error al crear la carpeta {path}: {e}", level="ERROR")
        return False

def create_file(path, content=""):
    """Crea un archivo con contenido opcional."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        log_message(f"Archivo creado: {path}", level="DEBUG")
        return True
    except IOError as e:
        log_message(f"Error al crear el archivo {path}: {e}", level="ERROR")
        return False

def generate_frontend_structure(project_path, framework):
    """Genera una estructura básica para proyectos frontend."""
    log_message(f"Generando estructura frontend para {framework}...", level="INFO")
    frontend_path = os.path.join(project_path, "frontend")
    create_directory(frontend_path)

    if framework == "react":
        create_directory(os.path.join(frontend_path, "public"))
        create_directory(os.path.join(frontend_path, "src", "components"))
        create_file(os.path.join(frontend_path, "src", "App.js"), "// React App.js")
        create_file(os.path.join(frontend_path, "src", "index.js"), "// React index.js")
        create_file(os.path.join(frontend_path, "public", "index.html"), "")
        create_file(os.path.join(frontend_path, ".env"), "")
        create_file(os.path.join(frontend_path, "package.json"), "{}") # Placeholder
        create_file(os.path.join(frontend_path, "README.md"), f"# {project_path} Frontend (React)")
    elif framework == "vue":
        create_directory(os.path.join(frontend_path, "public"))
        create_directory(os.path.join(frontend_path, "src", "components"))
        create_directory(os.path.join(frontend_path, "src", "assets"))
        create_file(os.path.join(frontend_path, "src", "main.js"), "// Vue main.js")
        create_file(os.path.join(frontend_path, "src", "App.vue"), "")
        create_file(os.path.join(frontend_path, "public", "index.html"), "")
        create_file(os.path.join(frontend_path, "package.json"), "{}") # Placeholder
        create_file(os.path.join(frontend_path, "README.md"), f"# {project_path} Frontend (Vue.js)")
    elif framework == "angular":
        log_message("La generación de estructura Angular es más compleja y generalmente requiere Angular CLI.", level="WARNING")
        create_file(os.path.join(frontend_path, "README.md"), f"# {project_path} Frontend (Angular) - Usar Angular CLI para inicializar")
    else:
        log_message(f"Framework frontend '{framework}' no soportado para generación de estructura detallada.", level="WARNING")
        create_file(os.path.join(frontend_path, "README.md"), "# Frontend Project (Básico)")

    return True

def generate_backend_structure(project_path, framework, database):
    """Genera una estructura básica para proyectos backend."""
    log_message(f"Generando estructura backend para {framework} con {database}...", level="INFO")
    backend_path = os.path.join(project_path, "backend")
    create_directory(backend_path)

    create_directory(os.path.join(backend_path, "app"))
    create_directory(os.path.join(backend_path, "app", "api"))
    create_directory(os.path.join(backend_path, "app", "core"))
    create_directory(os.path.join(backend_path, "app", "db"))
    create_directory(os.path.join(backend_path, "app", "models"))
    create_directory(os.path.join(backend_path, "app", "schemas"))
    create_directory(os.path.join(backend_path, "app", "crud"))

    create_file(os.path.join(backend_path, "app", "__init__.py"), "")
    create_file(os.path.join(backend_path, "app", "main.py"), "# Main application file")
    create_file(os.path.join(backend_path, "requirements.txt"), "fastapi\nuvicorn\nSQLAlchemy\npsycopg2-binary # Example for PostgreSQL")
    create_file(os.path.join(backend_path, ".env"), "")
    create_file(os.path.join(backend_path, "Dockerfile"), "# Dockerfile for backend")
    create_file(os.path.join(backend_path, "README.md"), f"# {project_path} Backend ({framework} + {database})")

    if framework == "fastapi":
        create_file(os.path.join(backend_path, "app", "api", "v1", "endpoints", "health.py"), "# Health endpoint")
        create_file(os.path.join(backend_path, "app", "api", "v1", "__init__.py"), "")
        create_file(os.path.join(backend_path, "app", "core", "config.py"), "# Configuration settings")
        create_file(os.path.join(backend_path, "app", "db", "session.py"), "# Database session setup")
        create_file(os.path.join(backend_path, "app", "models", "user.py"), "# User model example")
        create_file(os.path.join(backend_path, "app", "schemas", "user.py"), "# User schema example")
        create_file(os.path.join(backend_path, "app", "crud", "user.py"), "# User CRUD operations")
    elif framework == "django":
        log_message("La generación de estructura Django es más compleja y generalmente requiere Django CLI.", level="WARNING")
        create_file(os.path.join(backend_path, "README.md"), f"# {project_path} Backend (Django) - Usar Django CLI para inicializar")
    elif framework == "express":
        log_message("La generación de estructura Node.js (Express) requiere npm init y otras herramientas.", level="WARNING")
        create_file(os.path.join(backend_path, "README.md"), f"# {project_path} Backend (Node.js/Express) - Usar npm para inicializar")
    else:
        log_message(f"Framework backend '{framework}' no soportado para generación de estructura detallada.", level="WARNING")
        create_file(os.path.join(backend_path, "README.md"), "# Backend Project (Básico)")

    return True

def generate_base_structure(project_name, answers):
    """Genera la estructura base del proyecto."""
    log_message("Generando estructura base del proyecto...", level="INFO")
    project_path = os.path.join(os.getcwd(), project_name)
    create_directory(project_path)

    create_file(os.path.join(project_path, ".gitignore"), "# .gitignore example")
    create_file(os.path.join(project_path, "LICENSE"), "# MIT License")
    create_file(os.path.join(project_path, "README.md"), f"# {project_name}\n\nEste es el README para tu proyecto.")

    project_type = answers.get("project_type")
    frontend_framework = answers.get("frontend_framework")
    backend_framework = answers.get("backend_framework")
    database = answers.get("database")

    if project_type == "frontend":
        generate_frontend_structure(project_path, frontend_framework)
    elif project_type == "backend":
        generate_backend_structure(project_path, backend_framework, database)
    elif project_type == "fullstack":
        generate_frontend_structure(project_path, frontend_framework)
        generate_backend_structure(project_path, backend_framework, database)

    log_message(f"Estructura del proyecto '{project_name}' generada exitosamente.", level="SUCCESS")
    return project_path
=======
"""
Generador básico de estructura de carpetas para proyectos.
"""

import os

def generate_structure(recommendations):
    project_root = "my_project"  # Podrías parametrizar o preguntar nombre
    print(f"\n📁 Generando estructura base en carpeta '{project_root}'...")

    try:
        os.makedirs(project_root, exist_ok=True)

        # Carpeta backend
        if any(framework.lower() in ["fastapi", "django", "python scripts"] for framework in recommendations.get("stack", [])):
            os.makedirs(os.path.join(project_root, "backend"), exist_ok=True)
            with open(os.path.join(project_root, "backend", "README.md"), "w") as f:
                f.write("# Backend\nEstructura inicial del backend.\n")

        # Carpeta frontend
        if any(framework.lower() in ["react", "vite", "tailwind css", "next.js", "node.js", "vue"] for framework in recommendations.get("stack", [])):
            os.makedirs(os.path.join(project_root, "frontend"), exist_ok=True)
            with open(os.path.join(project_root, "frontend", "README.md"), "w") as f:
                f.write("# Frontend\nEstructura inicial del frontend.\n")

        # Carpeta docs
        os.makedirs(os.path.join(project_root, "docs"), exist_ok=True)
        with open(os.path.join(project_root, "docs", "README.md"), "w") as f:
            f.write("# Documentación\nArchivos de documentación.\n")

        print("📁 Estructura creada con éxito.")
    except Exception as e:
        print(f"Error creando estructura: {e}")
>>>>>>> 386c08e7392360a7fad41d9ed71668350cf41424
