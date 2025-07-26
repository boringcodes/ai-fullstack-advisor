<<<<<<< HEAD
import subprocess
import shutil
from utils.logger import log_message

def check_command_exists(command):
    """Verifica si un comando está disponible en el PATH."""
    return shutil.which(command) is not None

def check_python_version():
    """Verifica si la versión de Python es 3.10 o superior."""
    try:
        version_output = subprocess.check_output(["python3", "--version"]).decode("utf-8")
        version_parts = version_output.split(" ")[1].split(".")
        major = int(version_parts[0])
        minor = int(version_parts[1])
        if major >= 3 and minor >= 10:
            log_message(f"Python 3.10+ encontrado: {version_output.strip()}", level="SUCCESS")
            return True
        else:
            log_message(f"Python 3.10+ no encontrado. Versión actual: {version_output.strip()}. "
                        "Algunas funcionalidades podrían no operar correctamente.", level="WARNING")
            return False
    except Exception as e:
        log_message(f"No se pudo verificar la versión de Python: {e}", level="ERROR")
        return False

def check_npm_installed():
    """Verifica si Node.js y npm están instalados."""
    if check_command_exists("node") and check_command_exists("npm"):
        log_message("Node.js y npm están instalados.", level="SUCCESS")
        return True
    else:
        log_message("Node.js o npm no están instalados. Es posible que los proyectos frontend no se inicialicen correctamente.", level="WARNING")
        return False

def check_git_installed():
    """Verifica si Git está instalado."""
    if check_command_exists("git"):
        log_message("Git está instalado.", level="SUCCESS")
        return True
    else:
        log_message("Git no está instalado. No se podrá clonar repositorios o inicializar el control de versiones.", level="WARNING")
        return False

def check_all_requirements():
    """Verifica todos los requisitos técnicos."""
    log_message("Verificando requisitos técnicos...", level="INFO")
    all_present = True
    if not check_python_version():
        all_present = False
    if not check_command_exists("pip"):
        log_message("pip no está instalado o no está en el PATH.", level="ERROR")
        all_present = False
    else:
        log_message("pip está instalado.", level="SUCCESS")

    check_npm_installed() # Opcional, solo advierte si no está.
    check_git_installed() # Opcional, solo advierte si no está.

    if not all_present:
        log_message("Algunos requisitos técnicos no se cumplen. Revisa la documentación.", level="WARNING")
    else:
        log_message("Todos los requisitos técnicos principales están cubiertos.", level="INFO")
    return all_present
=======
"""
Funciones para verificar si herramientas están instaladas localmente.
"""

import shutil

def is_tool_installed(tool_name):
    """
    Verifica si una herramienta está disponible en PATH.
    """
    return shutil.which(tool_name) is not None
>>>>>>> 386c08e7392360a7fad41d9ed71668350cf41424
