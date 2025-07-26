import json
from PyInquirer import prompt
from utils.logger import log_message

def get_project_config():
    """
    Carga las preguntas desde stack_questions.json y las presenta al usuario.
    Retorna las respuestas del usuario.
    """
    questions_file = "prompts/stack_questions.json"
    try:
        with open(questions_file, "r", encoding="utf-8") as f:
            questions = json.load(f)
    except FileNotFoundError:
        log_message(f"Error: El archivo de preguntas '{questions_file}' no fue encontrado.", level="ERROR")
        return None
    except json.JSONDecodeError:
        log_message(f"Error: El archivo '{questions_file}' no es un JSON válido.", level="ERROR")
        return None

    log_message("Bienvenido a AI Fullstack Advisor", level="INFO")
    log_message("Una herramienta para guiar la planificación técnica de tu proyecto.", level="INFO")

    answers = prompt(questions)
    return answers