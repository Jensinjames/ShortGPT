```python
import scrapy
from scrapy.http import Request

class PaginationHandler(scrapy.Spider):
    name = 'reddit_scraper'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        # Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
            # Create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }

            # Yield or give the scraped info to Scrapy
            yield scraped_info

        # Get the next page url and create a new request to it
        next_page_url = response.css("span.next-button a::attr(href)").extract_first()
        if next_page_url is not None:
            yield Request(url=next_page_url, callback=self.parse)
```