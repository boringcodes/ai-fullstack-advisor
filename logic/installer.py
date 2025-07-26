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
