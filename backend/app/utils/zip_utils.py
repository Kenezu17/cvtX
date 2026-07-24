from pathlib import Path
import zipfile

# BASEDIR = Path(__file__).resolve().parent.parent

# OUTPUT = BASEDIR / 'output'

def zip_folder(folder_path:str, zip_path:str):
    folder = Path(folder_path)
    zip_file = Path(zip_path)

    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in folder.iterdir():
            if file.is_file():
                zf.write(file,arcname=file.name)

    return str(zip_file)
