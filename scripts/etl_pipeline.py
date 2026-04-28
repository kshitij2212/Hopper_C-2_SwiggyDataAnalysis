import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_project_root():
    """Returns the project root directory."""
    return Path(__file__).resolve().parent.parent

def load_data(raw_path):
    """Loads raw data from CSV."""
    logger.info(f"Loading raw data from {raw_path}")
    df = pd.read_csv(raw_path, parse_dates=['Order Date'])
    logger.info(f"Loaded {len(df):,} rows.")
    return df

def clean_data(df):
    """Performs data cleaning steps."""
    logger.info("Starting data cleaning...")
    
    before = len(df)
    df = df.dropna()
    logger.info(f"Dropped {before - len(df):,} null rows.")
    
    before = len(df)
    df = df.drop_duplicates()
    logger.info(f"Dropped {before - len(df):,} duplicate rows.")
    
    before = len(df)
    df = df[df['Rating Count'] != 0]
    logger.info(f"Filtered out {before - len(df):,} rows with 0 rating count.")
    
    column_map = {
        'State': 'state', 
        'City': 'city', 
        'Order Date': 'order_date', 
        'Restaurant Name': 'restaurant_name', 
        'Location': 'location', 
        'Category': 'category', 
        'Dish Name': 'dish_name', 
        'Price (INR)': 'price_inr', 
        'Rating': 'rating', 
        'Rating Count': 'rating_count'
    }
    df = df.rename(columns=column_map)
    logger.info("Renamed columns to snake_case.")
    
    return df

def flag_outliers(df):
    """Flags price outliers using the IQR method."""
    logger.info("Flagging price outliers...")
    Q1 = df['price_inr'].quantile(0.25)
    Q3 = df['price_inr'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df['is_price_outlier'] = ~df['price_inr'].between(lower_bound, upper_bound)
    logger.info(f"Flagged {df['is_price_outlier'].sum():,} price outliers.")
    return df

def feature_engineering(df):
    """Adds derived features."""
    logger.info("Performing feature engineering...")
    df['month'] = df['order_date'].dt.to_period('M').astype(str)
    df['day_of_week'] = df['order_date'].dt.day_name()
    
    def categorize_price(price):
        if price < 150: return 'Budget'
        elif price < 400: return 'Mid-range'
        else: return 'Premium'
    
    df['price_bucket'] = df['price_inr'].apply(categorize_price)
    df['rating_count'] = df['rating_count'].astype(int)
    logger.info("Feature engineering complete.")
    return df

def save_data(df, processed_path, final_path):
    """Saves the cleaned data to CSV (both intermediate and final versions)."""
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(processed_path, index=False)
    logger.info(f"Cleaned dataset (with outliers) saved to {processed_path}")
    
    df_final = df.drop(columns=['is_price_outlier'])
    df_final.to_csv(final_path, index=False)
    logger.info(f"Final cleaned dataset (outlier flag removed) saved to {final_path}")

def run_pipeline():
    """Main function to run the ETL pipeline."""
    PROJECT_ROOT = get_project_root()
    RAW_PATH = PROJECT_ROOT / 'data/raw/swiggy_data_raw.csv'
    PROCESSED_PATH = PROJECT_ROOT / 'data/processed/swiggy_cleaned.csv'
    FINAL_PATH = PROJECT_ROOT / 'data/processed/swiggy_final_cleaned.csv'
    
    try:
        df = load_data(RAW_PATH)
        df = clean_data(df)
        df = flag_outliers(df)
        df = feature_engineering(df)
        save_data(df, PROCESSED_PATH, FINAL_PATH)
        logger.info("ETL Pipeline completed successfully.")
    except Exception as e:
        logger.error(f"ETL Pipeline failed: {str(e)}")

if __name__ == "__main__":
    run_pipeline()
