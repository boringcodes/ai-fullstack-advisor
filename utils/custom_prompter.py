import json
from utils.logger import log_message
from PyInquirer import prompt

def _should_show_question(question_name, answers_so_far):
    """
    Determina si una pregunta debe mostrarse basándose en las respuestas anteriores.
    Esta es tu lógica 'when' implementada en Python.
    """
    if question_name == "frontend_framework":
        # Usamos .get().lower() para comparar siempre en minúsculas
        return answers_so_far.get("project_type", "").lower() in ["frontend", "fullstack"]
    elif question_name == "backend_framework":
        return answers_so_far.get("project_type", "").lower() in ["backend", "fullstack"]
    elif question_name == "database":
        return answers_so_far.get("project_type", "").lower() in ["backend", "fullstack"]
    elif question_name == "project_name":
        return answers_so_far.get("confirm_generation") # Este es un booleano, no necesita .lower()
    
    return True # Por defecto, si no hay condición específica, la pregunta se muestra

def get_project_config_custom(questions_json_path):
    """
    Carga las preguntas desde un archivo JSON y las presenta al usuario.
    Maneja la lógica condicional ('when') completamente en Python.
    Normaliza las respuestas de texto a minúsculas, excepto el nombre del proyecto.
    """
    try:
        with open(questions_json_path, 'r', encoding='utf-8') as f:
            all_questions_definitions = json.load(f)
    except FileNotFoundError:
        log_message(f"Error: El archivo de preguntas '{questions_json_path}' no fue encontrado.", level="ERROR")
        return None
    except json.JSONDecodeError as e:
        log_message(f"Error al parsear el JSON de preguntas en '{questions_json_path}': {e}", level="ERROR")
        return None
    except Exception as e:
        log_message(f"Error inesperado al cargar el archivo de preguntas: {e}", level="ERROR")
        return None

    if not isinstance(all_questions_definitions, list):
        log_message(f"Error: El archivo '{questions_json_path}' no contiene una lista de preguntas válida.", level="ERROR")
        log_message("Se esperaba una estructura JSON de tipo array (lista) a nivel raíz.", level="ERROR")
        return None

    log_message("Bienvenido a AI Fullstack Advisor", level="INFO")
    log_message("Una herramienta para guiar la planificación técnica de tu proyecto.", level="INFO")

    answers = {}

    for question_def in all_questions_definitions:
        question_name = question_def.get("name")

        if not _should_show_question(question_name, answers):
            continue

        question_to_prompt = question_def.copy()
        if 'when' in question_to_prompt:
            del question_to_prompt['when']

        try:
            current_answer = prompt([question_to_prompt])
            
            if current_answer is None or not current_answer:
                log_message("Operación de preguntas cancelada por el usuario o sin respuestas válidas.", level="ERROR")
                return None
            
            # --- NORMALIZACIÓN A MINÚSCULAS ---
            for key, value in current_answer.items():
                if key == "project_name": # El nombre del proyecto no debe ir en minúsculas
                    answers[key] = value
                elif isinstance(value, str):
                    answers[key] = value.lower() # Convertir todas las demás respuestas de texto a minúsculas
                else:
                    answers[key] = value # Mantener valores booleanos o de otro tipo sin cambios
            
        except KeyboardInterrupt:
            log_message("Operación cancelada por el usuario (Ctrl+C).", level="ERROR")
            return None
        except Exception as e:
            log_message(f"Error inesperado durante la presentación de preguntas para '{question_name}': {e}", level="ERROR")
            return None
                
    return answers