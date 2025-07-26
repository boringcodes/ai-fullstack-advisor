
# AI Fullstack Advisor™

## AI Fullstack Advisor™ v1.0

🚀 Overview
AI Fullstack Advisor™ es una herramienta de línea de comandos (CLI) diseñada para simplificar y guiar la fase inicial de planificación técnica de tu próximo proyecto de desarrollo. Olvídate de la parálisis por análisis; este asistente te ayuda a definir tu stack tecnológico ideal y a generar una estructura de proyecto base, para que puedas saltar directamente a codificar.

Esta es la Versión 1.0 (MVP educativo), el resultado de un emocionante proceso de desarrollo iterativo, lleno de desafíos y aprendizajes valiosos.

✨ Features (v1.0 MVP)
Verificación de Requisitos: Comprueba automáticamente la presencia de Python (3.9+), pip, Node.js, npm y Git en tu sistema.

Asesor Interactivo: Realiza una serie de preguntas clave (tipo de proyecto, frameworks, base de datos) para entender tus necesidades.

Lógica Condicional Robusta: Adapta las preguntas basándose en tus respuestas previas, utilizando un sistema de preguntas personalizado en Python.

Recomendación de Stack: Sugiere una combinación optimizada de tecnologías frontend, backend y base de datos basada en tus elecciones.

Generación de Estructura Base: Crea directorios y archivos esenciales para tu proyecto, incluyendo estructuras para Frontend (React, Angular, Vue.js) y Backend (Node.js con Express, Django, Flask).

Simulación de Instalación de Dependencias: Por ahora, simula la ejecución de comandos de instalación (npm install, pip install) para los frameworks seleccionados.

Resumen de Configuración: Guarda un archivo JSON detallado con todos los detalles de tu proyecto y las decisiones tomadas.

Registro Detallado: Utiliza un sistema de logging (INFO, SUCCESS, WARNING, ERROR, DEBUG) para un seguimiento claro y granular del proceso.

🛠️ Tech Stack & Development Journey
El AI Fullstack Advisor™ está construido principalmente con Python, aprovechando su robustez para scripting y su extenso ecosistema de librerías.

Tecnologías Clave Utilizadas:
Python 3.9+: El lenguaje principal y el motor de la aplicación.

os y sys (Módulos de Python): Fundamentales para la gestión de rutas de archivos absolutas, asegurando que el script funcione correctamente sin importar desde dónde se ejecute.

PyInquirer: Utilizado para crear la interfaz de línea de comandos interactiva y estilizada, proporcionando una experiencia de usuario amigable.

json (Módulo de Python): Esencial para cargar y gestionar las definiciones de las preguntas del CLI y para guardar el resumen de la configuración final del proyecto.

subprocess (Módulo de Python): Empleado para la simulación de la ejecución de comandos externos del sistema (como npm para Node.js o pip para Python).

Desafíos Superados y Soluciones Implementadas:
El camino hacia la v1.0 estuvo marcado por varios retos cruciales, cada uno transformado en una solución robusta:

Manejo de Rutas Absolutas:

Desafío: Asegurar que el script pudiera encontrar sus módulos internos (utils, prompts, logic) y archivos JSON sin importar el directorio de trabajo actual desde el que se ejecutara.

Solución: Implementamos un bloque de código al inicio de fullstack_advisor.py que utiliza os.path.dirname(os.path.abspath(__file__)) y sys.path.insert(0, script_dir) para añadir la ruta del script a la ruta de búsqueda de módulos de Python, garantizando la portabilidad.

Lógica Condicional en Preguntas (PyInquirer's 'when'):

Desafío: PyInquirer se mostró extremadamente estricto y propenso a errores al interpretar las condiciones "when" definidas directamente en el archivo stack_questions.json, a pesar de seguir su sintaxis documentada. Esto generaba errores persistentes como 'when' needs to be function that accepts a dict argument.

Solución: Adoptamos un enfoque más robusto y controlado:

Eliminación de "when" del JSON: La clave "when" fue removida completamente de prompts/stack_questions.json.

custom_prompter.py: Creamos una herramienta de preguntas personalizada (utils/custom_prompter.py) que maneja la lógica condicional (_should_show_question) directamente en Python. Este módulo decide qué pregunta presentar basándose en las respuestas obtenidas hasta el momento, y luego pasa solo esa pregunta (ya sin la clave "when") a PyInquirer para su renderizado, dándonos control total sobre el flujo de preguntas.

Normalización de Entradas de Usuario:

Desafío: Las respuestas del usuario (ej., "Fullstack", "React") a menudo comenzaban con mayúsculas, lo que podía causar que la lógica de recomendación o generación de stack no las reconociera si esperaba todo en minúsculas.

Solución: Implementamos una normalización automática de todas las respuestas de texto a minúsculas dentro de utils/custom_prompter.py antes de almacenarlas en el diccionario answers. El nombre del proyecto es la única excepción para preservar su formato original.

Error de requirements.txt:

Desafío: Durante la fase de simulación de instalación, la función intentaba encontrar un requirements.txt en una ubicación incorrecta para los proyectos generados.

Solución: Identificamos la necesidad de ajustar la lógica en logic/installer.py para que, en una instalación real, busque el requirements.txt dentro del subdirectorio backend del proyecto recién generado (si es un backend Python), o para gestionar las dependencias de Node.js con npm de forma adecuada. Esto se ha marcado como una mejora prioritaria para futuras versiones con instalación real.

💡 Próximos Pasos (V2 Aspirations)
Aunque el AI Fullstack Advisor™ v1.0 es funcional y robusto, el camino hacia la Versión 2.0 es emocionante y lleno de potencial:

Instalación Real de Dependencias: Pasar de la simulación a la ejecución real de comandos como npm install, pip install -r, etc., para configurar el entorno de desarrollo automáticamente.

Generación de Contenido Avanzado: Crear no solo la estructura de carpetas, sino también archivos de configuración inicial, ejemplos de "Hello World" para los frameworks elegidos, y plantillas de código básicas.

Más Opciones de Stack: Ampliar la biblioteca de frameworks, bases de datos y herramientas DevOps soportadas por el Advisor.

Validación de Entrada Mejorada: Implementar validaciones más robustas y personalizadas para las respuestas del usuario, garantizando una configuración aún más precisa.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues, enviar pull requests o sugerir nuevas características para hacer crecer este Advisor.

📜 Licencia
Distribuido bajo licencia MIT. Consulta LICENSE para más detalles.

Made with AI, DevOps & Love 💜
by @Farükツ
