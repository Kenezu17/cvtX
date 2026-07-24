import pandas as pd

def csv_to_xl(inputFile: str, filename: str):
    df = pd.read_csv(inputFile)

    if not filename.lower().endswith((".xlsx", ".xls")):
        filename = f"{filename}.xlsx"

    df.to_excel(filename, index=False)

    return filename


