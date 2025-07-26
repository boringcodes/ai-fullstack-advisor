import subprocess
import shutil
import os # Aunque no se usa directamente en esta revisión, es bueno tenerlo si se necesita en el futuro

try:
    from utils.logger import log_message
except ImportError:
    # Fallback si utils.logger no está disponible (ej. durante testing o ejecución aislada)
    def log_message(message, level="INFO"):
        print(f"[{level}] {message}")

def check_command_exists(command):
    """Verifica si un comando ejecutable existe en el PATH del sistema."""
    return shutil.which(command) is not None

def check_python_version():
    """
    Verifica si Python está instalado y si su versión es 3.9 o superior (compatible con PyInquirer).
    Prioriza 'python' en Windows y 'python3' en Linux/macOS.
    """
    python_command = None
    python_version_output = None

    # Primero intenta con 'python' (común en Windows y si se añade al PATH)
    try:
        result = subprocess.run(['python', '--version'], check=True, capture_output=True, text=True)
        python_version_output = result.stdout.strip()
        python_command = 'python'
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Si 'python' falla, intenta con 'python3' (común en Linux/macOS)
        try:
            result = subprocess.run(['python3', '--version'], check=True, capture_output=True, text=True)
            python_version_output = result.stdout.strip()
            python_command = 'python3'
        except (subprocess.CalledProcessError, FileNotFoundError):
            log_message("Python no se encontró en el PATH. Asegúrate de que Python 3.9 o superior esté instalado y accesible.", level="ERROR")
            return False

    if python_version_output:
        # Extraer la versión (ej. "Python 3.9.13" -> "3.9.13")
        version_string = python_version_output.split(" ")[1]
        try:
            version_parts = list(map(int, version_string.split(".")))
            major, minor = version_parts[0], version_parts[1]

            # Requisito para PyInquirer es ~3.9.x, pero tu Advisor puede necesitar 3.10+
            # Mantenemos el requisito de 3.9+ para compatibilidad con PyInquirer,
            # pero puedes ajustar esto si tu Advisor realmente requiere 3.10+ para otras cosas.
            if major >= 3 and minor >= 9:
                log_message(f"Python 3.9+ detectado: {python_command} ({version_string})", level="SUCCESS")
                return True
            else:
                log_message(f"Versión de Python ({version_string}) inferior a la recomendada (3.9+). Algunas funcionalidades podrían no operar correctamente.", level="WARNING")
                return False
        except ValueError:
            log_message(f"No se pudo parsear la versión de Python: '{version_string}'.", level="ERROR")
            return False
    
    return False # En caso de que se llegue aquí sin determinar la versión

def check_pip_installed():
    """Verifica si pip está instalado."""
    if check_command_exists("pip"):
        log_message("pip está instalado.", level="SUCCESS")
        return True
    else:
        log_message("pip no está instalado o no está en el PATH. Es esencial para instalar dependencias.", level="ERROR")
        return False

def check_npm_installed():
    """Verifica si Node.js y npm están instalados."""
    if check_command_exists("node") and check_command_exists("npm"):
        log_message("Node.js y npm están instalados.", level="SUCCESS")
        return True
    else:
        log_message("Node.js o npm no están instalados. Esto puede afectar la generación de proyectos frontend.", level="WARNING")
        return False

def check_git_installed():
    """Verifica si Git está instalado."""
    if check_command_exists("git"):
        log_message("Git está instalado.", level="SUCCESS")
        return True
    else:
        log_message("Git no está instalado. No se podrá inicializar el control de versiones ni clonar repositorios.", level="WARNING")
        return False

def check_all_requirements():
    """Verifica todos los requisitos técnicos."""
    log_message("Verificando requisitos técnicos...", level="INFO")
    all_main_requirements_met = True # Cambiado el nombre para mayor claridad

    # Verificación de Python (requerido)
    if not check_python_version():
        all_main_requirements_met = False
        log_message("Se requiere Python 3.9+ para la ejecución principal del Advisor.", level="ERROR")
        
    # Verificación de pip (requerido)
    if not check_pip_installed():
        all_main_requirements_met = False
        log_message("Se requiere pip para instalar dependencias y asegurar el funcionamiento del Advisor.", level="ERROR")

    # Verificaciones opcionales con advertencia
    check_npm_installed()
    check_git_installed()

    if not all_main_requirements_met:
        log_message("Algunos requisitos técnicos CRÍTICOS no se cumplen. Por favor, instálalos antes de continuar.", level="ERROR")
        return False # Devolvemos False para indicar que no puede continuar
    else:
        log_message("Todos los requisitos técnicos principales están cubiertos.", level="INFO")
        return True # Devolvemos True si todo está OK