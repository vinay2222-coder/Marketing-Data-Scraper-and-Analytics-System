import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
from datetime import datetime

def generate_marketing_report():
    try:
        # Encode password to handle the '@' symbol
        password = urllib.parse.quote_plus("Vinay@2222")
        engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/marketing_db")
        
        # 1. Pull Data
        df = pd.read_sql("SELECT * FROM campaign_data", engine)
        
        if df.empty:
            print("Analytics: No data found in database.")
            return

        # 2. Perform Analytics (Calculating Share of Voice)
        total_impressions = df['impressions'].sum()
        df['Share_of_Voice'] = (df['impressions'] / total_impressions) * 100
        
        # 3. Export to Excel
        filename = f"Marketing_Analytics_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(filename, index=False, engine='openpyxl')
        
        print(f"Analytics: Report generated as {filename}")
        
    except Exception as e:
        print(f"Analytics Error: {e}")