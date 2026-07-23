import importlib
import os
import sys

if __name__ == "__main__":
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)

    try:
        uvicorn = importlib.import_module("uvicorn")
    except ImportError as exc:
        raise RuntimeError(
            "uvicorn is required to run this script. Install it with 'pip install uvicorn'."
        ) from exc

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=5000,
        reload=True,
    )