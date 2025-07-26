"""
Funciones para verificar si herramientas están instaladas localmente.
"""

import shutil

def is_tool_installed(tool_name):
    """
    Verifica si una herramienta está disponible en PATH.
    """
    return shutil.which(tool_name) is not None
