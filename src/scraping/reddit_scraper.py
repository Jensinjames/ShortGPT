```python
import scrapy
from scrapy.crawler import CrawlerProcess
from src.data.json_data_store import store_data

class RedditScraper(scrapy.Spider):
    name = "reddit_scraper"
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        reddit_data_schema = {
            'title': response.css('h1::text').get(),
            'url': response.url,
            'content': response.css('div.content').get(),
        }
        store_data(reddit_data_schema)
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(RedditScraper)
    process.start()
```