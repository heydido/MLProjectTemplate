import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "project_name"

list_of_files = [
    ".dvc/config",
    ".github/workflows/.gitkeep",
    "artifacts/.gitkeep",
    "config/.gitkeep",
    "dags/.gitkeep",
    "docs/.gitkeep",
    "flowcharts/.gitkeep",
    "logs/.gitkeep",
    "mlruns/.gitkeep",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "references/.gitkeep",
    "scripts/test.sh",
    "reports/figures/.gitkeep",
    "reports/.gitkeep",
    "scripts/test.sh",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/exception.py",
    f"src/{project_name}/utils/logger.py",
    "static/assets/img/.gitkeep",
    "static/css/.gitkeep",
    "static/css2/.gitkeep",
    "static/js/.gitkeep",
    "templates/index.html",
    "templates/results.html",
    "tests/unit/.gitkeep",
    "tests/integration/.gitkeep",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "dvc.yaml",
    "main.py",
    "README.md",
    "requirements.txt",
    "setup.py",
]

for a_file in list_of_files:
    a_file = Path(a_file)
    file_dir, file_name = os.path.split(a_file)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")

    if (not os.path.exists(a_file)) or (os.path.getsize(a_file) == 0):
        with open(a_file, "w") as f:
            pass
            logging.info(f"Creating empty file: {a_file}")
    else:
        logging.info(f"{file_name} already exists. Skipping creating the file.")
