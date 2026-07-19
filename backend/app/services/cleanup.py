import os
import shutil
import time
from pathlib import Path
from typing import Iterable


class CleanupService:
    def __init__(self, root_dir: str | os.PathLike | None = None, ttl_seconds: int = 600):
        self.root_dir = Path(root_dir or Path(__file__).resolve().parent.parent)
        self.ttl_seconds = ttl_seconds
        self.upload_dir = self.root_dir / "uploads"
        self.output_dir = self.root_dir / "output"

        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def cleanup_old_files(self, directories: Iterable[str | os.PathLike] | None = None) -> list[Path]:
        """Delete files older than the configured TTL from the given directories."""
        targets = [Path(d) for d in (directories or [self.upload_dir, self.output_dir])]
        removed_files: list[Path] = []
        now = time.time()

        for directory in targets:
            if not directory.exists():
                continue
            for path in directory.iterdir():
                if path.is_file() and (now - path.stat().st_mtime) > self.ttl_seconds:
                    path.unlink()
                    removed_files.append(path)
                elif path.is_dir() and (now - path.stat().st_mtime) > self.ttl_seconds:
                    shutil.rmtree(path, ignore_errors=True)
                    removed_files.append(path)

        return removed_files

    def cleanup_file(self, path: str | os.PathLike) -> None:
        """Delete a single file or directory if it exists."""
        target = Path(path)
        if target.is_dir():
            shutil.rmtree(target, ignore_errors=True)
        elif target.exists():
            target.unlink()

    def cleanup_after_download(self, paths: Iterable[str | os.PathLike]) -> list[Path]:
        """Remove files after a download has been served."""
        removed_files: list[Path] = []
        for path in paths:
            target = Path(path)
            if target.exists():
                self.cleanup_file(target)
                removed_files.append(target)
        return removed_files
