```python
import sys
sys.path.append('../scraping')
sys.path.append('../data')
sys.path.append('../ui')

from reddit_scraper import scrape_reddit
from pagination_handler import handle_pagination
from dynamic_content_handler import handle_dynamic_content
from json_data_store import store_data
from checkbox_handler import handle_checkbox

class WebscraperIntegration:
    def __init__(self):
        self.webscraper = False

    def integrate_webscraper(self):
        checkbox_state = handle_checkbox()
        if checkbox_state:
            print("Scraping Started")
            reddit_data = scrape_reddit()
            print("Scraping Completed")

            print("Handling Pagination")
            paginated_data = handle_pagination(reddit_data)
            print("Pagination Handled")

            print("Handling Dynamic Content")
            dynamic_content_data = handle_dynamic_content(paginated_data)
            print("Dynamic Content Handled")

            print("Storing Data")
            store_data(dynamic_content_data)
            print("Data Stored")

            self.webscraper = True
            print("Webscraper Integrated")
        else:
            print("Webscraper Not Integrated")

    def is_webscraper_enabled(self):
        return self.webscraper

if __name__ == "__main__":
    webscraper_integration = WebscraperIntegration()
    webscraper_integration.integrate_webscraper()
```