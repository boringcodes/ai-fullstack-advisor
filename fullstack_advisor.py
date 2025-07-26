"""
AI-Fullstack-Advisor: CLI para guiar la configuración técnica de proyectos dev.
Made with AI, DevOps & Love 💜 by Farükツ
Versión: 1.0 - MVP educativo
"""

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
    main()