"""
Generador básico de estructura de carpetas para proyectos.
"""

import os

def generate_structure(recommendations):
    project_root = "my_project"  # Podrías parametrizar o preguntar nombre
    print(f"\n📁 Generando estructura base en carpeta '{project_root}'...")

    try:
        os.makedirs(project_root, exist_ok=True)

        # Carpeta backend
        if any(framework.lower() in ["fastapi", "django", "python scripts"] for framework in recommendations.get("stack", [])):
            os.makedirs(os.path.join(project_root, "backend"), exist_ok=True)
            with open(os.path.join(project_root, "backend", "README.md"), "w") as f:
                f.write("# Backend\nEstructura inicial del backend.\n")

        # Carpeta frontend
        if any(framework.lower() in ["react", "vite", "tailwind css", "next.js", "node.js", "vue"] for framework in recommendations.get("stack", [])):
            os.makedirs(os.path.join(project_root, "frontend"), exist_ok=True)
            with open(os.path.join(project_root, "frontend", "README.md"), "w") as f:
                f.write("# Frontend\nEstructura inicial del frontend.\n")

        # Carpeta docs
        os.makedirs(os.path.join(project_root, "docs"), exist_ok=True)
        with open(os.path.join(project_root, "docs", "README.md"), "w") as f:
            f.write("# Documentación\nArchivos de documentación.\n")

        print("📁 Estructura creada con éxito.")
    except Exception as e:
        print(f"Error creando estructura: {e}")