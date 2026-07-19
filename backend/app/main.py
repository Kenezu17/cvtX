from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.convert import router as convert_router
from .routers.download import router as download_router

app = FastAPI(
    title='ConvertX',
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

 

BASE_DIR = Path(__file__).resolve().parent
(BASE_DIR / 'uploads').mkdir(parents=True, exist_ok=True)
(BASE_DIR / 'output').mkdir(parents=True, exist_ok=True)

app.include_router(convert_router)
app.include_router(download_router)


