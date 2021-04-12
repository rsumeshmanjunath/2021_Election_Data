# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy_tutorial.items import QuoteItem

class QoutesSpider(scrapy.Spider):
    name = "quotes_item"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))
        quotes = response.css('div.quote')

        for quote in quotes:
            loader = ItemLoader(item = QuoteItem(), selector=quote)
            loader.add_css('quote_content', '.text::text')
            loader.add_css('tags', '.tag::text')
            quote_item = loader.load_item()

            author_url = quote.css('.author + a::attr(href)').get()

            # go to author next_page
            yield response.follow(author_url, self.parse_author, meta={'quote_item':quote_item})

        # go to Next page
        for a in response.css('li.next a'):
            yield response.follow(a, self.parse)


    def parse_author(self, response):
        quote_item = response.meta['quote_item']
        loader = ItemLoader(item=quote_item, response=response)
        loader.add_css('author_name', '.author-title::text')
        loader.add_css('author_birthday', '.author-born-date::text')
        loader.add_css('author_bornlocation', '.author-born-location::text')
        yield loader.load_item()
