"""
Logger simple para registrar resúmenes y mensajes.
"""

def log_summary(answers, recommendations):
    print("\n--- Resumen del proyecto ---")
    print("Respuestas del usuario:")
    for k, v in answers.items():
        print(f"  - {k}: {v}")

    print("\nRecomendaciones:")
    for k, v in recommendations.items():
        if isinstance(v, list):
            print(f"  - {k}: {', '.join(v)}")
        else:
            print(f"  - {k}: {v}")
    print("----------------------------\n")
