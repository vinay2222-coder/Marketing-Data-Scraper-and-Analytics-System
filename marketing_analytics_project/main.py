import scraper
import database
import analytics

def main():
    print("--- Starting Marketing Pipeline ---")
    
    # Step 1: Scrape
    data = scraper.get_marketing_tags()
    
    if data:
        # Step 2: Save to DB
        database.save_to_mysql(data)
        
        # Step 3: Run Analytics & Create Excel
        analytics.generate_marketing_report()
        
        print("--- Pipeline Execution Complete ---")
    else:
        print("--- Pipeline Failed at Scraping Stage ---")

if __name__ == "__main__":
    main()