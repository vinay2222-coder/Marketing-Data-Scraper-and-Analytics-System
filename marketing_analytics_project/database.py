import mysql.connector

def save_to_mysql(tags):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vinay@2222", # Your specific password
            database="marketing_db"
        )
        cursor = db.cursor()
        
        # SQL query to insert data
        query = "INSERT INTO campaign_data (platform, campaign_name, impressions) VALUES (%s, %s, %s)"
        
        for tag in tags:
            # We assign a default of 100 impressions for each tag
            cursor.execute(query, ("Website_Scrape", tag, 100))
            
        db.commit()
        print(f"Database: {cursor.rowcount} rows inserted.")
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if 'db' in locals(): db.close()