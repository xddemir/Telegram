import scrapy
class QuotesSpider(scrapy.Spider):

    def __init__(self,name):
        self.name=name

        self.start_urls='https://www.youtube.com/'
        self.url=f'{self.start_urls}results?search_query={self.name}'

    def parse(self, response):
        elemen=response.xpath("//*[@id='thumbnail'] href::text").extract()