import os
import sys

# Importamos log_message de utils.logger para mantener consistencia en los logs
try:
    from utils.logger import log_message
except ImportError:
    # Fallback si se ejecuta generate_structure_doc.py de forma aislada
    def log_message(message, level="INFO"):
        print(f"[{level}] {message}")


def generate_tree_structure(startpath, exclude_dirs=None, exclude_files=None):
    """
    Genera una representación de árbol de directorios y archivos,
    excluyendo ciertos elementos y añadiendo comentarios.
    """
    if exclude_dirs is None:
        # Excluimos directorios internos que no son relevantes para la estructura principal
        # o que no queremos que se listen sus contenidos (ej. .git, outputs, docs internos)
        exclude_dirs = ['.git', '__pycache__', 'node_modules', 'venv', 'env']
    if exclude_files is None:
        # Excluimos archivos generados dinámicamente o que no aportan al entendimiento de la estructura del código
        exclude_files = ['.DS_Store', 'config_summary.json']

    tree_str_lines = []
    
    # Obtener el nombre de la carpeta raíz del proyecto para la primera línea
    project_root_name = os.path.basename(os.path.abspath(startpath))
    tree_str_lines.append(f"{project_root_name}/")

    # Almacenar elementos para ordenar: primero directorios, luego archivos, dentro de cada nivel
    # Y también para saber el camino completo para los comentarios
    items_at_level = {} # {relative_path: (dirs, files)}

    for root, dirs, files in os.walk(startpath, topdown=True):
        # Excluir directorios completos antes de procesar sus contenidos
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        relative_root = os.path.relpath(root, startpath)
        if relative_root == ".": # Es la raíz del proyecto
            current_level_path = ""
        else:
            current_level_path = relative_root

        # Filtrar archivos a excluir
        filtered_files = [f for f in files if f not in exclude_files]

        # Guardar para procesamiento ordenado
        items_at_level[current_level_path] = (sorted(dirs), sorted(filtered_files))

    # Ahora recorremos de forma estructurada para construir el árbol
    def build_branch(current_path, level):
        indent = '│   ' * level
        
        # Obtener los elementos para este nivel
        dirs_to_process, files_to_process = items_at_level.get(current_path, ([], []))

        # Añadir subdirectorios
        for d in dirs_to_process:
            full_sub_path = os.path.join(current_path, d)
            
            comment = ""
            if d == 'logic':
                comment = "\t\t# Lógica principal y backend inteligente"
            elif d == 'prompts':
                comment = "\t\t# Preguntas y lógica del sistema"
            elif d == 'utils':
                comment = "\t\t# Utilidades auxiliares"
            elif d == 'outputs':
                comment = "\t\t# Archivos generados automáticamente"
            elif d == '.github':
                comment = "\t\t# Configuración de GitHub (workflows, plantillas)"
            elif d == 'workflows': # Dentro de .github
                comment = "" # No es necesario un comentario para este subdirectorio específico
            elif d == 'docs':
                comment = "\t\t# Documentación extendida"

            tree_str_lines.append(f"{indent}├── {d}/{comment}")
            build_branch(full_sub_path, level + 1) # Llamada recursiva para subcarpetas

        # Añadir archivos en el nivel actual
        for f in files_to_process:
            comment = ""
            file_full_path = os.path.join(current_path, f)

            # Comentarios específicos para archivos
            if f == 'fullstack_advisor.py':
                comment = "\t\t# Módulo principal CLI (flujo general de ejecución)"
            elif f == 'requirements.txt':
                comment = "\t\t# Lista de dependencias del sistema"
            elif f == 'setup_structure.py':
                comment = "\t\t# Script que genera la estructura base inicial"
            elif f == 'README.md':
                comment = "\t\t# Documentación general del proyecto"
            elif f == 'LICENSE':
                comment = "\t\t# Licencia del proyecto"
            elif f == '.gitignore':
                comment = "\t\t# Archivos a ignorar por Git"
            elif f == '.pre-commit-config.yaml':
                comment = "\t\t# Configuración para automatizar tareas antes de cada commit"
            elif f == 'recommender.py':
                comment = "\t\t# Motor de recomendaciones según respuestas"
            elif f == 'installer.py':
                comment = "\t\t# Instalación automática de dependencias"
            elif f == 'structure_generator.py':
                comment = "\t\t# Generador de carpetas y archivos del proyecto"
            elif f == 'stack_questions.json':
                comment = "\t\t# Base de preguntas clave con opciones"
            elif f == 'stack_questions.py':
                comment = "\t\t# Lógica para lanzar preguntas en CLI"
            elif f == 'checker.py':
                comment = "\t\t# Verifica herramientas locales (npm, pip, etc.)"
            elif f == 'generate_structure_doc.py':
                comment = "\t\t# Script para actualizar dinámicamente docs/structure.graphql"
            elif f == 'logger.py':
                comment = "\t\t# Logging del proceso y resumen generado"
            elif f == 'config_summary.json': # aunque esté en exclude_files, si por alguna razón aparece
                comment = "\t\t# Resultado personalizado del usuario"
            elif f == 'project-board.md':
                comment = "" # Ya está claro por la carpeta docs
            elif f == 'roadmap.md':
                comment = "" # Ya está claro por la carpeta docs
            elif f == 'structure.graphql':
                comment = "" # Ya está claro por la carpeta docs
            elif f == 'project-template.md':
                comment = "" # Dentro de .github
            elif f == 'validate_config.yml':
                comment = "" # Dentro de .github/workflows


            tree_str_lines.append(f"{indent}├── {f}{comment}")

    # Iniciar la construcción del árbol desde la raíz
    build_branch("", 0) # La raíz del proyecto es nivel 0

    # Reemplazar el último '├──' con '└──' en cada nivel para un mejor aspecto de árbol
    final_lines = []
    for i, line in enumerate(tree_str_lines):
        if i + 1 < len(tree_str_lines):
            # Obtener la indentación actual y la siguiente
            current_indent_level = line.count('│   ')
            next_indent_level = tree_str_lines[i+1].count('│   ')

            # Si la siguiente línea está en un nivel inferior o igual, es el último elemento del nivel actual
            if next_indent_level <= current_indent_level:
                 # Encontrar el último '├──' o '└──' en la línea
                last_branch_symbol_index = line.rfind('├──')
                if last_branch_symbol_index != -1:
                    # Sustituir el último '├──' por '└──'
                    modified_line = line[:last_branch_symbol_index] + '└──' + line[last_branch_symbol_index+3:]
                    final_lines.append(modified_line)
                else:
                    final_lines.append(line)
            else:
                final_lines.append(line)
        else: # Última línea del archivo, siempre es '└──'
             last_branch_symbol_index = line.rfind('├──')
             if last_branch_symbol_index != -1:
                 modified_line = line[:last_branch_symbol_index] + '└──' + line[last_branch_symbol_index+3:]
                 final_lines.append(modified_line)
             else:
                 final_lines.append(line)
    
    return "\n".join(final_lines)


def update_structure_graphql(project_root_dir, output_file):
    """
    Genera la estructura del proyecto y la guarda en el archivo .graphql,
    sobrescribiendo el contenido existente.
    """
    log_message("Generando estructura del proyecto para documentación...", level="INFO")

    # Incluimos explícitamente las carpetas 'outputs', '.github', 'docs' aquí
    # ya que os.walk las ignoraría si estuvieran en exclude_dirs al procesar la raíz.
    # Pero las queremos en el árbol, aunque no sus contenidos.
    # El script las manejará como directorios sin explorar en profundidad si no están en la raíz de la exclusión.
    
    # Define las carpetas y archivos a excluir de la lista recursiva,
    # pero asegurándote de que las carpetas de alto nivel como 'outputs' sí aparezcan.
    # Las subcarpetas y archivos de .github y docs se manejan de forma simplificada en el árbol.
    exclude_dirs_for_walk = ['.git', '__pycache__', 'node_modules', 'venv', 'env']
    exclude_files_for_walk = ['.DS_Store', 'config_summary.json'] # config_summary.json es generado

    structure_content = generate_tree_structure(project_root_dir, exclude_dirs_for_walk, exclude_files_for_walk)
    
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True) # Asegura que la carpeta docs exista
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Esquema Visual de la Estructura del Sistema AI Fullstack Advisor™\n\n")
            f.write("> **Nota:** Este archivo se genera automáticamente. No editar manualmente.\n\n")
            f.write("```plaintext\n")
            f.write(structure_content)
            f.write("\n```\n") # Añade una línea en blanco antes del cierre del bloque de código
        log_message(f"Archivo de estructura actualizado: {output_file}", level="SUCCESS")
    except IOError as e:
        log_message(f"Error al escribir en {output_file}: {e}", level="ERROR")

if __name__ == "__main__":
    # La ruta de la raíz de tu proyecto 'ai-fullstack-advisor'.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    output_path = os.path.join(project_root, 'docs', 'structure.graphql')
    
    update_structure_graphql(project_root, output_path)