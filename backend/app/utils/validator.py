import os
from pathlib import Path
from typing import Tuple

ALLOWED_EXTENSIONS = {
    "pdf": {"pdf"},
    "document": {"doc", "docx", "txt", "rtf"},
    "image": {"png", "jpg", "jpeg", "webp"},
    "spreadsheet": {"xls", "xlsx", "csv"},
}


def validate_file(file_name: str, allowed_types: Tuple[str, ...] | None = None) -> Tuple[bool, str]:
    """Validate an uploaded file name and extension."""
    if not file_name:
        return False, "No file name provided."

    extension = Path(file_name).suffix.lower().lstrip(".")
    if not extension:
        return False, "File has no extension."

    if allowed_types is None:
        allowed_types = tuple(ALLOWED_EXTENSIONS.keys())

    allowed_exts = set()
    for file_type in allowed_types:
        allowed_exts.update(ALLOWED_EXTENSIONS.get(file_type, set()))

    if extension not in allowed_exts:
        supported = ", ".join(sorted(allowed_exts))
        return False, f"Unsupported file type. Supported types: {supported}"

    return True, ""


def sanitize_filename(file_name: str) -> str:
    """Keep a filename safe for filesystem usage."""
    path = Path(file_name)
    stem = path.stem
    suffix = path.suffix

    safe_stem = "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in stem)
    safe_stem = safe_stem.strip("._") or "file"

    return f"{safe_stem}{suffix.lower()}"


def ensure_upload_dir(directory: str | os.PathLike) -> Path:
    """Create a directory if it does not exist and return it."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path
