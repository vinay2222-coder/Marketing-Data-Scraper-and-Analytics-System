# 📊 Marketing Data Scraper & Analytics System

An automated **End-to-End ETL (Extract, Transform, Load) Pipeline** built to monitor marketing trends and competitor data. This system scrapes real-time data, stores it in a relational MySQL database, and generates automated business intelligence reports in Excel.

## 🚀 Features
* **Automated Extraction:** Scrapes product categories and data using **BeautifulSoup4** with custom headers to bypass basic bot detection.
* **Persistent Storage:** Integrated with **MySQL** via **SQLAlchemy** to maintain a historical record of all scraped campaigns.
* **Data Transformation:** Uses **Pandas** to process raw SQL data into meaningful KPIs.
* **Business Intelligence:** Automatically generates timestamped Excel reports with calculated metrics like **Share of Voice**.
* **Modular Architecture:** Separated logic into Scraper, Database, and Analytics modules for professional-grade maintainability.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** BeautifulSoup4, Pandas, SQLAlchemy, Requests, Openpyxl
* **Database:** MySQL
* **Editor:** VS Code

## 🏗️ System Architecture
The project follows a modular design to ensure scalability:
1.  **`scraper.py`**: Fetches raw data from target marketing/e-commerce sites.
2.  **`database.py`**: Manages the MySQL connection and handles data insertion.
3.  **`analytics.py`**: Pulls data back from SQL to calculate metrics and export to Excel.
4.  **`main.py`**: The orchestration script that runs the entire pipeline from start to finish.

## 📂 Project Structure
```text
marketing_analytics_p/
├── main.py          # The entry point (Orchestrator)
├── scraper.py       # Web scraping logic using BeautifulSoup
├── database.py      # MySQL connection and data insertion
├── analytics.py     # Data processing and Excel generation
├── requirements.txt # List of dependencies
└── README.md        # Project documentation
