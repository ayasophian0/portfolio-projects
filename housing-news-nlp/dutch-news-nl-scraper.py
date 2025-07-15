import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to extract article links from category page
def get_article_links(page_url, headers):
    links = []
    response = requests.get(page_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        for a_tag in soup.find_all("a", href=True):
            div = a_tag.find("div", class_="ratio ratio-16x9")
            if div:
                links.append(a_tag['href'])
    else:
        print(f"Failed to fetch {page_url}, status code {response.status_code}")
    
    return links

# Function to extract data from article page
def get_article_data(article_url, headers):
    response = requests.get(article_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Timestamp
        time_tag = soup.find("time", class_="text-secondary updated me-2")
        timestamp = time_tag["datetime"] if time_tag else None
        
        # Headline
        headline_tag = soup.select_one("h1.text-serif.lh-1")
        headline = headline_tag.get_text(strip=True) if headline_tag else None
        
        # Article text
        main_tag = soup.find("main", class_="px-4")
        article_text = main_tag.get_text(separator="\n", strip=True) if main_tag else None
        
        return {
            "url": article_url,
            "timestamp": timestamp,
            "headline": headline,
            "article_text": article_text
        }
    else:
        print(f"Failed to fetch article {article_url}, status code {response.status_code}")
        return None

# Main scraper
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

all_articles = []

# Iterate over 110 pages
for page_num in range(1, 111):  # 1 to 110 inclusive
    if page_num == 1:
        page_url = "https://www.dutchnews.nl/category/housing/"
    else:
        page_url = f"https://www.dutchnews.nl/category/housing/page/{page_num}/"
    
    print(f"\nFetching page {page_num}: {page_url}")
    
    # Get article links from the page
    article_links = get_article_links(page_url, headers)
    print(f"Found {len(article_links)} article links on page {page_num}.")
    
    # For each article link, fetch article data
    for article_url in article_links:
        print(f"  Fetching article: {article_url}")
        article_data = get_article_data(article_url, headers)
        if article_data:
            all_articles.append(article_data)
        
        # Sleep a bit between article requests
        time.sleep(1)
    
    # Sleep a bit between page requests
    time.sleep(2)
    
    # Save progress every 10 pages
    if page_num % 10 == 0:
        checkpoint_df = pd.DataFrame(all_articles)
        checkpoint_filename = f"dutchnews_housing_articles_checkpoint_page_{page_num}.csv"
        checkpoint_df.to_csv(checkpoint_filename, index=False, encoding="utf-8")
        print(f"Checkpoint saved: {checkpoint_filename}")

# Final save
df = pd.DataFrame(all_articles)
df.to_csv("dutchnews_housing_articles.csv", index=False, encoding="utf-8")

print("\nScraping completed. Articles saved to dutchnews_housing_articles.csv")
