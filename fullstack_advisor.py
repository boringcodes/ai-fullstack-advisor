"""
AI-Fullstack-Advisor: CLI para guiar la configuración técnica de proyectos dev.
Made with AI, DevOps & Love 💜 by Farükツ
Versión: 1.0 - MVP educativo
"""

<<<<<<< HEAD
import os
from utils.logger import log_message, save_config_summary
from utils.checker import check_all_requirements
from prompts.stack_questions import get_project_config
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

    # 2. Obtener configuración del proyecto a través de preguntas CLI
    answers = get_project_config()
    if not answers:
        log_message("No se pudo obtener la configuración del proyecto. Saliendo.", level="ERROR")
        return

    # 3. Generar sugerencia de stack
    recommended_stack = recommend_stack(answers)
    if not recommended_stack:
        log_message("No se pudo generar una recomendación de stack. Saliendo.", level="ERROR")
        return

    # Definir nombre del proyecto basado en el tipo de proyecto
    project_name_prefix = answers.get("project_type", "my_new").replace(" ", "_")
    project_name = f"{project_name_prefix}_project"

    # 4. Instalar tecnologías recomendadas (simulación por ahora)
    log_message("🔧 Instalando tecnologías recomendadas...", level="INFO")
    installation_success = run_installations(answers, project_name)
    if not installation_success:
        log_message("La instalación de algunas tecnologías falló. Revisa los logs.", level="WARNING")

    # 5. Generar estructura base del proyecto
    log_message("📂 Generando estructura base del proyecto...", level="INFO")
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
    save_config_summary(summary, project_name)

    log_message(f"✅ ¡Tu entorno para '{project_name}' está listo! ¡Mucho éxito!", level="SUCCESS")

if __name__ == "__main__":
    from datetime import datetime # Importar aquí para uso en main
=======
from prompts.stack_questions import load_questions, ask_questions
from logic.recommender import generate_recommendations
from logic.installer import install_recommendations
from logic.structure_generator import generate_structure
from utils.logger import log_summary

def main():
    print("\n🧠 Bienvenido a AI Fullstack Advisor")
    print("Una herramienta para guiar la planificación técnica de tu proyecto.\n")

    # 1. Cargar preguntas clave
    questions = load_questions()

    # 2. Lanzar preguntas y recolectar respuestas del usuario
    answers = ask_questions(questions)

    # 3. Generar recomendaciones de stack con base en las respuestas
    stack = generate_recommendations(answers)

    # 4. Verificar herramientas e instalar lo necesario
    install_recommendations(stack)

    # 5. Generar estructura base del proyecto
    generate_structure(stack)

    # 6. Registrar resumen en logs
    log_summary(answers, stack)

    print("\n✅ Tu entorno está listo para comenzar. ¡Mucho éxito!")

if __name__ == "__main__":
>>>>>>> 386c08e7392360a7fad41d9ed71668350cf41424
    main()