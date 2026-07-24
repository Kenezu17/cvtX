import time
from pathlib import Path
import shutil
import asyncio

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT =  BASE_DIR / 'output'
UPLOAD  = BASE_DIR / 'uploads'

expiration  = 10*60

def clean_up():
    print('Running cleanup....')

    now = time.time()

    for folder in [OUTPUT, UPLOAD]:
        if not folder.exists():
            continue
        
        for file in folder.iterdir():

            try:
                age =  now - file.stat().st_mtime

                if age > expiration:
                    if file.is_file():
                        file.unlink()

                    elif file.is_dir():
                        shutil.rmtree(file)

            except Exception as e:
                print(f'Failed to delete after the expiration {str(e)}')

async def clean_worker():
    while True:
        clean_up()
        await asyncio.sleep(60)
           