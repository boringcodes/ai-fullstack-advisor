import os
from logic.structure_generator import generate_base_structure
from utils.logger import log_message

def test_structure_generation():
    """
    Función para probar la generación de estructura de forma independiente.
    """
    log_message("Ejecutando prueba de generación de estructura...", level="INFO")

    # Respuestas de ejemplo para la prueba
    answers_frontend = {
        "project_type": "frontend",
        "frontend_framework": "react",
        "backend_framework": None,
        "database": None
    }
    answers_backend = {
        "project_type": "backend",
        "frontend_framework": None,
        "backend_framework": "fastapi",
        "database": "postgresql"
    }
    answers_fullstack = {
        "project_type": "fullstack",
        "frontend_framework": "vue",
        "backend_framework": "express",
        "database": "mongodb"
    }

    test_project_name_frontend = "test_frontend_project"
    test_project_name_backend = "test_backend_project"
    test_project_name_fullstack = "test_fullstack_project"

    log_message(f"Generando {test_project_name_frontend} (Frontend)...", level="INFO")
    generate_base_structure(test_project_name_frontend, answers_frontend)

    log_message(f"Generando {test_project_name_backend} (Backend)...", level="INFO")
    generate_base_structure(test_project_name_backend, answers_backend)

    log_message(f"Generando {test_project_name_fullstack} (Fullstack)...", level="INFO")
    generate_base_structure(test_project_name_fullstack, answers_fullstack)

    log_message("Prueba de generación de estructura finalizada. Puedes usar 'tree' para ver los resultados.", level="SUCCESS")

if __name__ == "__main__":
    test_structure_generation()