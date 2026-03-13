import requests
from bs4 import BeautifulSoup

def get_marketing_tags():
    url = "https://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape the 'Top Ten' tags from the sidebar
        tag_elements = soup.find_all('span', class_='tag-item')
        
        tags = []
        for tag in tag_elements[:10]:
            name = tag.find('a').get_text()
            tags.append(name)
            
        print(f"Scraper: Found {len(tags)} trending tags.")
        return tags
        
    except Exception as e:
        print(f"Scraper Error: {e}")
        return []