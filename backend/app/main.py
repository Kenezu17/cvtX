from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from .routers.convert import router as convert_router
from .routers.download import router as download_router

from app.services.cleanup import clean_worker

@asynccontextmanager
async def lifespan(app: FastAPI):
    task =  asyncio.create_task(clean_worker())
    yield
    task.cancel()

app = FastAPI(
    title='ConvertX',
    version='1.0.0',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5173',
        'https://cvt-x.vercel.app',
        'https://cvt-nc2msir2y-kenezu17s-projects.vercel.app'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

 

BASE_DIR = Path(__file__).resolve().parent
(BASE_DIR / 'uploads').mkdir(parents=True, exist_ok=True)
(BASE_DIR / 'output').mkdir(parents=True, exist_ok=True)

app.include_router(convert_router)
app.include_router(download_router)


