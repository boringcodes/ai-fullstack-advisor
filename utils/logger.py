import json
from datetime import datetime
import os

def log_message(message, level="INFO"):
    """Imprime un mensaje formateado en la consola."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def save_config_summary(config_data, project_name="my_project"):
    """Guarda el resumen de la configuración en un archivo JSON."""
    outputs_dir = "outputs"
    os.makedirs(outputs_dir, exist_ok=True)
    filename = os.path.join(outputs_dir, f"config_summary_{project_name}.json")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=2)
        log_message(f"Resumen de configuración guardado en: {filename}", level="SUCCESS")
    except Exception as e:
        log_message(f"Error al guardar el resumen de configuración: {e}", level="ERROR")
