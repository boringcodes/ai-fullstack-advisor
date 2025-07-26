import json

def load_questions():
    """
    Carga las preguntas clave desde un JSON estructurado.
    """
    with open("prompts/stack_questions.json", "r", encoding="utf-8") as file:
        return json.load(file)

def ask_questions(questions):
    """
    Interactúa con el usuario para hacer preguntas y capturar respuestas.
    Retorna un dict con respuestas.
    """
    answers = {}
    for q in questions["questions"]:
        print(f"\n{q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"  {i}. {option}")
        while True:
            choice = input("Selecciona opción número: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(q['options']):
                answers[q['id']] = q['options'][int(choice)-1]
                break
            else:
                print("Por favor selecciona una opción válida.")
    return answers
