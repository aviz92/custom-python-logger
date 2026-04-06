import os
from pathlib import Path

IGNORED_DIRS = [".venv"]
IGNORED_FILES = ["__init__.py"]


def clean_migrations_folder(root_dir: Path) -> None:
    for dirpath, dirnames, _ in os.walk(root_dir):
        if any(ignored_dir in dirpath for ignored_dir in IGNORED_DIRS):
            continue

        if "migrations" in dirnames:
            migrations_dir = os.path.join(dirpath, "migrations")
            print(f"cleaning: {migrations_dir}")

            for filename in os.listdir(migrations_dir):
                file_path = os.path.join(migrations_dir, filename)
                if filename in IGNORED_FILES and os.path.isfile(file_path):
                    continue
                try:
                    os.remove(file_path)
                    print(f"delete: {file_path}")
                except Exception as e:
                    print(f"cant find {file_path}: {e}")


def main() -> None:
    root_dir = Path(__file__).parent.parent.parent
    print(f"Root directory: {root_dir}")
    clean_migrations_folder(root_dir=root_dir)


if __name__ == "__main__":
    main()
