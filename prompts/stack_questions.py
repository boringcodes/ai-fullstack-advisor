import json
from PyInquirer import prompt
from utils.logger import log_message

def get_project_config(questions_json_path):
    """
    Carga las preguntas desde un archivo JSON y las presenta al usuario.
    Maneja las condiciones 'when' directamente en Python para mayor robustez.
    """
    try:
        # Abre el archivo usando la ruta que se le pasó
        with open(questions_json_path, 'r', encoding='utf-8') as f:
            all_questions_data = json.load(f) # Cambiado el nombre a 'all_questions_data'
    except FileNotFoundError:
        log_message(f"Error: El archivo de preguntas '{questions_json_path}' no fue encontrado.", level="ERROR")
        return None
    except json.JSONDecodeError as e:
        log_message(f"Error al parsear el JSON de preguntas en '{questions_json_path}': {e}", level="ERROR")
        return None
    except Exception as e:
        log_message(f"Error inesperado al cargar el archivo de preguntas: {e}", level="ERROR")
        return None

    # Verifica que la data cargada sea una lista de preguntas, como se espera
    if not isinstance(all_questions_data, list):
        log_message(f"Error: El archivo '{questions_json_path}' no contiene una lista de preguntas válida.", level="ERROR")
        log_message("Se esperaba una estructura JSON de tipo array (lista) a nivel raíz.", level="ERROR")
        return None

    log_message("Bienvenido a AI Fullstack Advisor", level="INFO")
    log_message("Una herramienta para guiar la planificación técnica de tu proyecto.", level="INFO")

    answers = {}
    
    # Itera sobre cada pregunta individualmente para aplicar la lógica 'when'
    for question_obj in all_questions_data:
        # Verifica la condición 'when' antes de mostrar la pregunta
        if 'when' in question_obj:
            condition = question_obj['when']
            show_question = False

            # Manejar condiciones 'or' o 'and'
            if isinstance(condition, dict):
                if 'or' in condition and isinstance(condition['or'], list):
                    # Evaluar condiciones 'or'
                    for sub_condition in condition['or']:
                        key = list(sub_condition.keys())[0] # Obtener la clave de la sub-condición (ej. 'project_type')
                        value = sub_condition[key]         # Obtener el valor esperado (ej. 'Frontend')
                        if answers.get(key) == value:
                            show_question = True
                            break # Una condición 'or' es suficiente
                elif 'and' in condition and isinstance(condition['and'], list):
                    # Evaluar condiciones 'and'
                    show_question = True # Asumimos true y lo falseamos si una falla
                    for sub_condition in condition['and']:
                        key = list(sub_condition.keys())[0]
                        value = sub_condition[key]
                        if answers.get(key) != value:
                            show_question = False
                            break # Una condición 'and' que falla es suficiente
                else: # Condición simple de diccionario, ej: {"project_type": "Frontend"}
                    key = list(condition.keys())[0]
                    value = condition[key]
                    if answers.get(key) == value:
                        show_question = True
            elif isinstance(condition, bool):
                show_question = condition # Si es un booleano directo (true/false)
            else:
                # Si 'when' no es un dict ni un bool, logueamos y asumimos no mostrar para evitar el error
                log_message(f"Advertencia: 'when' inválido en la pregunta '{question_obj.get('name', 'desconocida')}'. Se omitirá.", level="WARNING")
                continue # Saltar esta pregunta

            if not show_question:
                continue # Saltar la pregunta si la condición no se cumple
        
        # Si no hay 'when' o la condición se cumple, muestra la pregunta
        try:
            # PyInquirer prompt espera una lista de preguntas, así que la envolvemos
            current_answer = prompt([question_obj]) 
            
            if current_answer is None or not current_answer: # Si el usuario presiona Ctrl+C o la respuesta es vacía
                log_message("Operación de preguntas cancelada por el usuario o sin respuestas válidas.", level="ERROR")
                return None
            
            # Actualiza las respuestas globales con la respuesta actual
            answers.update(current_answer)
            
        except KeyboardInterrupt:
            log_message("Operación cancelada por el usuario (Ctrl+C).", level="ERROR")
            return None
        except Exception as e:
            log_message(f"Error inesperado durante la presentación de preguntas para '{question_obj.get('name', 'N/A')}': {e}", level="ERROR")
            return None
            
    return answers