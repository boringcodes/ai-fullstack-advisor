from utils.logger import log_message

def recommend_stack(answers):
    """
    Recomienda un stack tecnológico basado en las respuestas del usuario.
    """
    if not answers:
        log_message("No se recibieron respuestas para generar la recomendación.", level="WARNING")
        return None

    project_type = answers.get("project_type")
    frontend_framework = answers.get("frontend_framework")
    backend_framework = answers.get("backend_framework")
    database = answers.get("database")

    recommendation_parts = []

    if project_type == "frontend":
        if frontend_framework:
            recommendation_parts.append(frontend_framework.capitalize())
        else:
            recommendation_parts.append("React (por defecto)") # Recomendación por defecto
    elif project_type == "backend":
        if backend_framework:
            recommendation_parts.append(backend_framework.capitalize())
        if database:
            recommendation_parts.append(database.capitalize())
        else:
            recommendation_parts.extend(["FastAPI (por defecto)", "PostgreSQL (por defecto)"])
    elif project_type == "fullstack":
        if frontend_framework:
            recommendation_parts.append(frontend_framework.capitalize())
        else:
            recommendation_parts.append("React (por defecto)")
        if backend_framework:
            recommendation_parts.append(backend_framework.capitalize())
        else:
            recommendation_parts.append("FastAPI (por defecto)")
        if database:
            recommendation_parts.append(database.capitalize())
        else:
            recommendation_parts.append("PostgreSQL (por defecto)")
    else:
        log_message("Tipo de proyecto no reconocido.", level="WARNING")
        return None

    if recommendation_parts:
        recommendation = " + ".join(recommendation_parts)
        log_message(f"Sugerencia: {recommendation}", level="SUCCESS")
        return recommendation
    else:
        log_message("No se pudo generar una sugerencia de stack con las respuestas dadas.", level="WARNING")
        return None