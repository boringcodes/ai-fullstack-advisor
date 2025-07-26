<<<<<<< HEAD
import subprocess
import sys
from utils.logger import log_message
from utils.checker import check_command_exists, check_npm_installed

def install_python_dependencies():
    """Instala las dependencias de Python listadas en requirements.txt."""
    log_message("Instalando dependencias de Python...", level="INFO")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        log_message("Dependencias de Python instaladas exitosamente.", level="SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Error al instalar dependencias de Python: {e}", level="ERROR")
        return False

def install_frontend_dependencies(project_name, framework):
    """Instala dependencias de frontend usando npm."""
    if not check_npm_installed():
        log_message("npm no está instalado. No se pueden instalar dependencias frontend.", level="WARNING")
        return False

    log_message(f"Instalando dependencias frontend para {framework} en {project_name}...", level="INFO")
    try:
        # Esto es un placeholder. En un proyecto real, aquí crearías el proyecto
        # y luego instalarías las dependencias dentro de esa carpeta.
        # Por ejemplo:
        # if framework == "react":
        #    subprocess.run(["npx", "create-react-app", project_name], check=True)
        #    subprocess.run(["npm", "install"], cwd=project_name, check=True)
        log_message(f"Simulando instalación de dependencias para {framework}.", level="INFO")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Error al instalar dependencias frontend para {framework}: {e}", level="ERROR")
        return False

def install_backend_dependencies(project_name, framework):
    """Instala dependencias de backend."""
    log_message(f"Instalando dependencias backend para {framework} en {project_name}...", level="INFO")
    try:
        # Similar al frontend, aquí iría la lógica para crear el proyecto
        # y luego instalar las dependencias específicas del backend.
        # Por ejemplo:
        # if framework == "fastapi":
        #    subprocess.run([sys.executable, "-m", "venv", os.path.join(project_name, "venv")], check=True)
        #    subprocess.run([os.path.join(project_name, "venv", "bin", "pip"), "install", "fastapi", "uvicorn"], check=True)
        log_message(f"Simulando instalación de dependencias para {framework}.", level="INFO")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Error al instalar dependencias backend para {framework}: {e}", level="ERROR")
        return False

def run_installations(answers, project_name):
    """Gestiona las instalaciones según el stack recomendado."""
    log_message("Iniciando instalación de tecnologías recomendadas...", level="INFO")

    project_type = answers.get("project_type")
    frontend_framework = answers.get("frontend_framework")
    backend_framework = answers.get("backend_framework")

    success = True

    # Instalación de dependencias del propio Advisor (Python)
    if not install_python_dependencies():
        success = False

    if project_type in ["frontend", "fullstack"]:
        if not install_frontend_dependencies(project_name, frontend_framework):
            success = False

    if project_type in ["backend", "fullstack"]:
        if not install_backend_dependencies(project_name, backend_framework):
            success = False
    
    return success
=======
"""
Instalador automático para las dependencias recomendadas.
"""

import subprocess
import sys

def install_recommendations(recommendations):
    stack = recommendations.get("stack", [])
    tools = recommendations.get("tools", [])

    print("\n🔧 Verificando e instalando dependencias necesarias...\n")

    # Instalación simplificada: solo ejemplos para Python y npm
    for item in stack + tools:
        if item.lower() in ["fastapi", "django", "python scripts"]:
            # Ejemplo: usar pip para librerías Python
            print(f"Instalando paquete Python: {item}")
            subprocess.run([sys.executable, "-m", "pip", "install", item.lower()], check=False)
        elif item.lower() in ["react", "vite", "tailwind css", "next.js", "node.js", "vue"]:
            # Ejemplo: usar npm para librerías JS (solo mostramos)
            print(f"Recomienda instalar paquete npm: {item}")
            # Para simplificar no instalamos automáticamente npm aquí
        elif item.lower() in ["docker", "kubernetes", "postman", "git", "vscode"]:
            print(f"Por favor asegúrate de tener instalado: {item}")
        else:
            print(f"Elemento no manejado para instalación automática: {item}")

    print("\n🔧 Instalación/verificación finalizada.\n")
>>>>>>> 386c08e7392360a7fad41d9ed71668350cf41424
