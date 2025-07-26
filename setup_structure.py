import os

folders = [
    "logic", "prompts", "utils", "outputs", ".github/workflows"
]
files = {
    "README.md": "",
    "project-board.md": "",
    "requirements.txt": "",
    "fullstack_advisor.py": "",
    "logic/recommender.py": "",
    "logic/installer.py": "",
    "logic/structure_generator.py": "",
    "prompts/stack_questions.json": "",
    "utils/checker.py": "",
    "utils/logger.py": "",
    "outputs/config_summary.json": "",
    ".github/project-template.md": "",
    ".github/workflows/validate_config.yml": ""
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Estructura base creada correctamente.")
