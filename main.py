from src.data_ingestion import load_data, generate_ingestion_summary

if __name__ == "__main__":
    file_path = "data/XAUUSD_1m.csv"
    load_df = load_data(file_path)
    generate_ingestion_summary(load_df)

