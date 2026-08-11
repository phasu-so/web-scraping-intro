import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Downloads the HTML content from the provided URL.
    Returns the HTML text if successful, or None if it fails.
    """
    try:
        # User-Agent headers help prevent the scraper from being blocked
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (Status Code 200)
        response.raise_for_status() 
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_title(html_content):
    """
    Parses the HTML and extracts the main title of the page.
    """
    if not html_content:
        return None
        
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the <title> tag in the HTML
    title_tag = soup.find('title')
    
    if title_tag:
        return title_tag.text.strip()
    else:
        return "No title found."
