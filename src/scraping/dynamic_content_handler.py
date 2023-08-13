```python
import scrapy

class DynamicContentHandler(scrapy.Spider):
    name = 'dynamic_content_handler'
    reddit_data_schema = {}

    def start_requests(self):
        urls = [
            'http://www.reddit.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('Scraping Started')
        self.reddit_data_schema = {
            'title': response.css('h1::text').get(),
            'link': response.url,
            'comments': self.handle_dynamic_content(response)
        }
        self.log('Scraping Completed')

    def handle_dynamic_content(self, response):
        self.log('Handling Dynamic Content')
        comments = response.css('div.comment').extract()
        self.log('Dynamic Content Handled')
        return comments

    def log(self, message):
        print(message)
```