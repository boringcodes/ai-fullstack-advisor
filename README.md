# 🤖 AI Fullstack Advisor™

**AI Fullstack Advisor™** es una herramienta CLI inteligente y modular que guía a desarrolladores en la elección, configuración, instalación y estructuración del stack tecnológico ideal para sus proyectos (frontend, backend o fullstack) en segundos.

> Made with AI, DevOps & Love 💜 by [Farükツ](https://github.com/boringcodes)  
> Versión 1.0 · MVP educativo · Proyecto modular & escalable

---

## 🧠 ¿Qué resuelve?

Muchos desarrolladores pierden tiempo y energía en configurar manualmente sus entornos técnicos o eligen mal su stack por falta de guía. Este sistema:

- 🔍 Hace **preguntas clave** para entender el proyecto y sus necesidades  
- 💡 Ofrece **recomendaciones inteligentes** de stack, frameworks y librerías  
- ⚙️ Instala automáticamente dependencias sugeridas (`npm`, `pip`)  
- 🏗️ Genera una **estructura profesional, escalable y modular**  
- 🚦 Aplica buenas prácticas de arquitectura desde el día 1 (Scrum + DevOps)

---

## 🚀 ¿Para quién es?

- 🧑‍🎓 Estudiantes o tesistas que quieren lanzar un proyecto funcional desde cero  
- 🧑‍💻 Freelancers o devs independientes que buscan acelerar su setup técnico  
- 🧑‍🏫 Profesores o mentores que necesitan estandarizar entornos educativos  
- 🧑‍🚀 Devs expertos que quieren ahorrar tiempo o experimentar nuevos stacks

---

## 📦 Requisitos Técnicos

| Herramienta        | Versión mínima |
|--------------------|----------------|
| Python             | 3.10+          |
| pip                | 22.x           |
| Node.js (opcional) | 18.x           |
| Git                | Última         |
| Visual Studio C++  | (para compilar en Windows) |

> ⚠️ Recomendado usar en ambientes Unix (Linux/macOS/WSL).  
> En Windows, asegúrate de tener instalados los **Build Tools**.

---

## ⚡ Instalación Rápida

```bash
# Clona el repositorio
git clone https://github.com/boringcodes/ai-fullstack-advisor.git
cd ai-fullstack-advisor

# Crea y activa el entorno virtual (si no lo tienes)
python -m venv venv
source venv/bin/activate # Para Linux/macOS/Git Bash
# O .\venv\Scripts\activate para CMD/PowerShell

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el sistema CLI
python fullstack_advisor.py
```

---

## 💡 Ejemplo de uso (CLI)

```bash
$ python fullstack_advisor.py

🧠 Bienvenido a AI Fullstack Advisor
Una herramienta para guiar la planificación técnica de tu proyecto.

👉 ¿Qué tipo de proyecto vas a iniciar?
[1] Frontend
[2] Backend
[3] Fullstack
> 3

✅ Sugerencia: React + FastAPI + PostgreSQL

🔧 Instalando tecnologías recomendadas...
📂 Generando estructura base del proyecto...
📄 Guardando resumen de configuración...

✅ ¡Tu entorno está listo! ¡Mucho éxito!
```

---

## 📁 Estructura del Proyecto (v1.0)

```plaintext
ai-fullstack-advisor/
│
├── fullstack_advisor.py            # Módulo principal CLI (flujo general de ejecución)
├── requirements.txt                # Lista de dependencias del sistema
├── setup_structure.py              # Script que genera la estructura base inicial
├── README.md                       # Documentación general (este archivo)
│
├── logic/                          # Lógica principal y backend inteligente
│   ├── recommender.py              # Motor de recomendaciones según respuestas
│   ├── installer.py                # Instalación automática de dependencias
│   └── structure_generator.py      # Generador de carpetas y archivos del proyecto
│
├── prompts/                        # Preguntas y lógica del sistema
│   ├── stack_questions.json        # Base de preguntas clave con opciones
│   └── stack_questions.py          # Lógica para lanzar preguntas en CLI
│
├── utils/                          # Utilidades auxiliares
│   ├── checker.py                  # Verifica herramientas locales (npm, pip, etc.)
│   └── logger.py                   # Logging del proceso y resumen generado
│   └── generate_structure_doc.py   # Script para actualizar dinámicamente docs/structure.graphql
│
├── outputs/                        # Archivos generados automáticamente
│   └── config_summary.json         # Resultado personalizado del usuario
│
├── .gitignore                      # Ignora archivos temporales y entornos virtuales
│
├── .pre-commit-config.yaml         # Configuración para automatizar tareas antes de cada commit
│
├── .github/
│   ├── project-template.md         # Plantilla Scrum-DevOps para gestión de proyecto
│   └── workflows/
│       └── validate_config.yml     # CI: Validación del JSON de configuración
│
└── docs/                           # Documentación extendida
    ├── project-board.md            # Scrum board: backlog, tareas, sprints
    ├── roadmap.md                  # Roadmap a futuro (v2, v3, plugins)
    └── structure.graphql           # Esquema visual en formato GraphQL del sistema
```

---

## 🛠️ Actualización Automática de la Estructura

La documentación de la estructura del proyecto (`docs/structure.graphql`) se mantiene siempre al día. Gracias a **pre-commit**, este archivo se **actualiza automáticamente** cada vez que realizas un `git commit`.

**Es fundamental que tu entorno virtual esté activado antes de hacer un commit** para que este proceso se ejecute correctamente.

---

## 🧩 Modularidad

Cada archivo está desacoplado. Puedes extender funcionalidades fácilmente:

- 🔧 Agrega nuevos stacks en `prompts/stack_questions.json`
- 🔧 Crea lógica de instalación en `installer.py`
- 🔧 Añade nuevas estructuras en `structure_generator.py`
- 🔧 Mejora las sugerencias en `recommender.py`

---

## 📈 Roadmap

| Versión | Características previstas                                                         |
| ------- | --------------------------------------------------------------------------------- |
| v1.0    | CLI inteligente, instalación, estructura, logs básicos ✅                          |
| v1.5    | Dockerfile, flags de terminal (modo experto), validaciones más estrictas          |
| v2.0    | UI web, historial de configuraciones, integración GPT para generación de README   |
| v3.0    | Plugin system, analizador de proyectos existentes, sugerencias basadas en IA real |

---

## 🧪 Test & QA

Para ejecutar pruebas de validación o futuras suites:

```bash
# Validar archivo de preguntas
python -m json.tool prompts/stack_questions.json

# Validar estructura generada
python setup_structure.py && tree
```

---

## 🤝 Cómo Contribuir

1. Haz fork del proyecto
2. Crea una branch: `git checkout -b feature/nueva-funcionalidad`
3. Haz commit de tus cambios: `git commit -m "feat: nueva funcionalidad"`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request 🧵

---

## 📖 Documentación Extendida

Revisa estos archivos en `docs/` para profundizar:

- 📌 `roadmap.md`: visión de futuro (Docker, plugins, Web UI)
- 🛠️ `project-board.md`: tareas pendientes, ideas, bugs
- 🧬 `structure.graphql`: visualización de carpetas como schema

---

## 📜 Licencia

Distribuido bajo licencia MIT.
Consulta `LICENSE` para más detalles.

---

## ✨ Créditos

- 👨‍💻 Autor: [Farükツ](https://github.com/boringcodes)
- 🧠 Inspiración: `cookiecutter`, `create-react-app`, `fig`, `DevStack Boosters`
- 🤖 AI Support: ChatGPT (OpenAI), Gemini (Google DeepMind)
- 🌍 Comunidad: Python, FastAPI, Devs de GitHub, StackOverflow & beyond

---

## 🧠 Filosofía de Diseño

> **"Automatiza lo repetitivo. Estandariza lo importante. Hazlo con inteligencia."**
> Este proyecto nace para empoderar a developers a lanzar ideas técnicas con rapidez, enfoque y buenas prácticas desde el día 1.

---

## 💜 Made with Code, AI & Love

**boringcodes™**
Querétaro, 🇲🇽 · 2025
[https://github.com/boringcodes](https://github.com/boringcodes)
