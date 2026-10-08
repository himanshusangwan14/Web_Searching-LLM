import requests
from bs4 import BeautifulSoup


def scrape_webpage(text: str) -> str:
    try:
        url = "https://google.com/search?q=" + text
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.get_text()
    except Exception as e:
        print(f"Error scraping webpage: {e}")
        return ""
