```python
import os

def embed_file_path(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    return file_path

def get_reddit_scraper_path():
    return embed_file_path("../scraping/reddit_scraper.py")

def get_pagination_handler_path():
    return embed_file_path("../scraping/pagination_handler.py")

def get_dynamic_content_handler_path():
    return embed_file_path("../scraping/dynamic_content_handler.py")

def get_json_data_store_path():
    return embed_file_path("../data/json_data_store.py")

def get_shortGPT_data_train_path():
    return embed_file_path("../data/shortGPT_data_train.py")

def get_checkbox_handler_path():
    return embed_file_path("../ui/checkbox_handler.py")

def get_webscraper_integration_path():
    return embed_file_path("../backend/webscraper_integration.py")
```