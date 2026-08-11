# Import the functions from our custom scraper module
from src.scraper import fetch_html, extract_title

def main():
    # Example URL for educational purposes
    target_url = "https://automatetheboringstuff.com/"
    print(f"Starting scraper for: {target_url}\n")
    
    # 1. Fetch the HTML
    html_data = fetch_html(target_url)
    
    if html_data:
        # 2. Extract and print the data
        page_title = extract_title(html_data)
        print(f"Success! The title of the page is: '{page_title}'")
    else:
        print("Failed to retrieve HTML data.")

# This ensures the main function only runs if this script is executed directly
if __name__ == "__main__":
    main()
