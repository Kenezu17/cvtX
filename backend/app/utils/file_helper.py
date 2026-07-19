import os
from pathlib import Path
from typing import Optional


def get_file_size(file_path: str | os.PathLike) -> int:
    """Return the size of a file in bytes."""
    return Path(file_path).stat().st_size


def get_file_extension(file_name: str) -> str:
    """Return the lowercase file extension without the dot."""
    return Path(file_name).suffix.lower().lstrip(".")


def build_output_path(output_dir: str | os.PathLike, file_name: str) -> Path:
    """Create a safe output path inside the given directory."""
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    return output_dir_path / Path(file_name).name


def read_text_file(file_path: str | os.PathLike) -> str:
    """Read the contents of a text file."""
    return Path(file_path).read_text(encoding="utf-8")


def remove_file_if_exists(file_path: str | os.PathLike) -> None:
    """Remove a file if it exists."""
    path = Path(file_path)
    if path.exists():
        path.unlink()
