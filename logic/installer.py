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
