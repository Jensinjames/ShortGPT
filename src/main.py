```python
import sys
sys.path.append('src/scraping')
sys.path.append('src/data')
sys.path.append('src/ui')
sys.path.append('src/routes')
sys.path.append('src/backend')

from reddit_scraper import scrape_reddit
from pagination_handler import handle_pagination
from dynamic_content_handler import handle_dynamic_content
from json_data_store import store_data
from shortGPT_data_train import train_shortGPT
from checkbox_handler import handle_checkbox
from directory_routes import embed_file_path
from webscraper_integration import integrate_webscraper

def main():
    # Check if webscraper is enabled
    if handle_checkbox('checkbox'):
        print("Scraping Started")
        reddit_data = scrape_reddit()
        print("Scraping Completed")

        print("Handling Pagination")
        paginated_data = handle_pagination(reddit_data)
        print("Pagination Handled")

        print("Handling Dynamic Content")
        dynamic_content_handled_data = handle_dynamic_content(paginated_data)
        print("Dynamic Content Handled")

        print("Storing Data")
        store_data(dynamic_content_handled_data)
        print("Data Stored")

        print("Embedding File Path")
        file_path = embed_file_path()
        print("File Path Embedded")

        print("Training Started")
        train_shortGPT(file_path)
        print("Training Completed")

        print("Integrating Webscraper")
        integrate_webscraper()
        print("Webscraper Integrated")

if __name__ == "__main__":
    main()
```