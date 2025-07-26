"""
Generador de recomendaciones basado en respuestas del usuario.
"""

def generate_recommendations(answers):
    recommendations = {}

    # Recomendación basada en tipo de proyecto
    if answers.get("project_type") == "Backend":
        subtype = answers.get("backend_subtype")
        if subtype == "API REST":
            recommendations["stack"] = ["FastAPI", "PostgreSQL", "Docker"]
        elif subtype == "Microservicios":
            recommendations["stack"] = ["Django", "RabbitMQ", "Kubernetes"]
        else:
            recommendations["stack"] = ["Python scripts", "Cron jobs"]
    elif answers.get("project_type") == "Frontend":
        subtype = answers.get("frontend_subtype")
        if subtype == "SPA (React/Vue)":
            recommendations["stack"] = ["React", "Vite", "Tailwind CSS"]
        elif subtype == "Landing Page":
            recommendations["stack"] = ["HTML", "CSS", "JavaScript"]
        else:
            recommendations["stack"] = ["PWA tools", "Service Workers"]
    else:
        subtype = answers.get("fullstack_subtype")
        if subtype == "API + SPA":
            recommendations["stack"] = ["FastAPI", "React", "PostgreSQL"]
        elif subtype == "SSR (Next.js, Nuxt)":
            recommendations["stack"] = ["Next.js", "Node.js", "MongoDB"]
        else:
            recommendations["stack"] = ["Microservices", "Vue", "Docker"]

    # Recomendación de herramientas según nivel del dev
    level = answers.get("experience_level")
    if level == "Principiante":
        recommendations["tools"] = ["VSCode", "Git", "Postman"]
    elif level == "Intermedio":
        recommendations["tools"] = ["VSCode", "Git", "Docker", "Postman"]
    else:
        recommendations["tools"] = ["VSCode", "Git", "Docker", "Kubernetes", "Postman"]

    return recommendations
