import os
import shutil
from pathlib import Path

IGNORED_DIRS = [".venv"]


def delete_pycache_folder(root_dir: Path) -> None:
    for dirpath, dirnames, _ in os.walk(root_dir):
        if any(ignored_dir in dirpath for ignored_dir in IGNORED_DIRS):
            continue

        if "__pycache__" in dirnames:
            pycache_dir = os.path.join(dirpath, "__pycache__")
            print(f"cleaning: {pycache_dir}")
            try:
                shutil.rmtree(pycache_dir)
                print(f"delete: {pycache_dir}")
            except Exception as e:
                print(f"cant find {pycache_dir}: {e}")


def main() -> None:
    root_dir = Path(__file__).parent.parent.parent
    print(f"Root directory: {root_dir}")
    delete_pycache_folder(root_dir)
    delete_pycache_folder(root_dir=root_dir)


if __name__ == "__main__":
    main()
