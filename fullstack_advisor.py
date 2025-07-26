"""
AI-Fullstack-Advisor: CLI para guiar la configuración técnica de proyectos dev.
Made with AI, DevOps & Love 💜 by Farükツ
Versión: 1.0 - MVP educativo
"""

import os
import sys # <--- ¡Nuevo import!

# --- Bloque de código para manejar rutas absolutas ---
# Esto es crucial para que el script encuentre sus propios módulos y archivos
# sin importar desde dónde se ejecute.
script_dir = os.path.dirname(os.path.abspath(__file__))
# Añadir el directorio del script al sys.path para que Python pueda encontrar
# los módulos 'utils', 'prompts', 'logic' sin problemas.
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)
# --- Fin del bloque de código de rutas absolutas ---


from utils.logger import log_message, save_config_summary
from utils.checker import check_all_requirements
from prompts.stack_questions import get_project_config # <-- Esta función necesitará un cambio
from logic.recommender import recommend_stack
from logic.installer import run_installations
from logic.structure_generator import generate_base_structure


def main():
    """Función principal para ejecutar AI Fullstack Advisor."""
    log_message("Iniciando AI Fullstack Advisor™", level="INFO")

    # 1. Verificar requisitos técnicos
    if not check_all_requirements():
        log_message("Por favor, instala los requisitos técnicos antes de continuar.", level="ERROR")
        return

    # Construir la ruta absoluta al archivo de preguntas JSON
    # Ahora usamos script_dir para construir la ruta al JSON
    questions_json_path = os.path.join(script_dir, 'prompts', 'stack_questions.json')

    # 2. Obtener configuración del proyecto a través de preguntas CLI
    # --- ¡Pasa la ruta absoluta al archivo JSON a get_project_config! ---
    answers = get_project_config(questions_json_path)
    if not answers:
        log_message("No se pudo obtener la configuración del proyecto. Saliendo.", level="ERROR")
        return

    # 3. Generar sugerencia de stack
    recommended_stack = recommend_stack(answers)
    if not recommended_stack:
        log_message("No se pudo generar una recomendación de stack. Saliendo.", level="ERROR")
        return

    # Definir nombre del proyecto basado en el tipo de proyecto
    # Si quieres que el usuario lo ingrese, deberás añadir una pregunta en stack_questions.json para ello
    project_name_prefix = answers.get("project_type", "my_new").replace(" ", "_")
    project_name = f"{project_name_prefix}_project"
    
    # Si quieres que el nombre del proyecto sea interactivo:
    # from PyInquirer import prompt
    # name_question = {
    #     'type': 'input',
    #     'name': 'project_name',
    #     'message': '¿Cómo se llamará tu nuevo proyecto?',
    #     'default': f"{project_name_prefix}_project"
    # }
    # name_answer = prompt([name_question])
    # if name_answer and 'project_name' in name_answer:
    #     project_name = name_answer['project_name']
    # else:
    #     log_message("Nombre de proyecto no especificado. Saliendo.", level="ERROR")
    #     return


    # 4. Instalar tecnologías recomendadas (simulación por ahora)
    log_message("🔧 Instalando tecnologías recomendadas...", level="INFO")
    installation_success = run_installations(answers, project_name) # Asegúrate que run_installations maneje bien el path
    if not installation_success:
        log_message("La instalación de algunas tecnologías falló. Revisa los logs.", level="WARNING")

    # 5. Generar estructura base del proyecto
    log_message("📂 Generando estructura base del proyecto...", level="INFO")
    # Asegúrate que generate_base_structure use la CWD para crear la carpeta del proyecto
    # o pasale una ruta base si quieres que genere fuera de CWD.
    generated_path = generate_base_structure(project_name, answers)
    if not generated_path:
        log_message("La generación de la estructura del proyecto falló. Saliendo.", level="ERROR")
        return

    # 6. Guardar resumen de configuración
    log_message("📄 Guardando resumen de configuración...", level="INFO")
    summary = {
        "project_name": project_name,
        "project_type": answers.get("project_type"),
        "frontend_framework": answers.get("frontend_framework"),
        "backend_framework": answers.get("backend_framework"),
        "database": answers.get("database"),
        "recommended_stack": recommended_stack,
        "generated_path": generated_path,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_config_summary(summary, project_name) # Asegúrate que save_config_summary use la ruta correcta para outputs

    log_message(f"✅ ¡Tu entorno para '{project_name}' está listo! ¡Mucho éxito!", level="SUCCESS")

if __name__ == "__main__":
    from datetime import datetime # Importar aquí para uso en main
    main()