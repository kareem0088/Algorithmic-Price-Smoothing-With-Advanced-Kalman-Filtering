import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[!] error to find: {file_path}")
    df = pd.read_csv(file_path)
    df['Gmt time'] = pd.to_datetime(df['Gmt time'])
    df.set_index('Gmt time', inplace=True)
    df.sort_index(inplace=True)
    return df


def generate_ingestion_summary(df: pd.DataFrame) -> None:
    print("---:: Data Ingestion ::---")
    print(f"[-] Total Data Points (1m Candel Count): {len(df)}")
    print(f"[-] Start Date: {df.index.min()}")
    print(f"[-] End Date: {df.index.max()}")
    print("\n[-] Data Columns & Types:")
    print(df.dtypes)
    print("\n[-] First 10 Rows:")
    print(df.head(10))
