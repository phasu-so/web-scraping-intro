# Week 7: Introduction to Web Scraping

This project introduces the fundamentals of web scraping using Python's `requests` and `BeautifulSoup4` libraries. It demonstrates how to download HTML content from a website and extract specific information based on HTML structure.

**Important Note on Ethics and Legality:**
Always be mindful of the website's `robots.txt` file (e.g., `https://example.com/robots.txt`) and their Terms of Service. Respect rate limits and avoid overwhelming servers. This project is for educational purposes only and should not be used for malicious or unauthorized data collection.

## Implemented Features
* **HTML Download**: Uses the `requests` library to fetch web page content.
* **HTML Parsing**: Leverages `BeautifulSoup4` to parse the downloaded HTML.
* **Data Extraction**: Extracts the main book title and a list of chapter titles from the "Automate the Boring Stuff with Python" website.
* **Error Handling**: Basic error handling for network issues and HTTP responses.

## How to Run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/web-scraping-intro.git
    cd web-scraping-intro
    ```
2.  **Install Dependencies:**
    You'll need `requests` and `beautifulsoup4`. It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install requests beautifulsoup4
    ```
3.  **Run the scraper:**
    ```bash
    python main.py
    ```
    The script will print the scraped book title and chapter titles to the console.
