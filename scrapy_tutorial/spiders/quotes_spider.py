 # -*- coding: utf-8 -*-
import scrapy

class QoutesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        self.logger.info('Hello this is my first spider')
        quotes = response.css('div.details-name')
        for quote in quotes:
            yield {
                'quotetext': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }

            author_url = quote.css('.author + a::attr(href)').get()
            self.logger.info('get author page url')

            # go to author next_page
            yield response.follow(author_url, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if(next_page is not None):
            yield response.follow(next_page, callback=self.parse)


    def parse_author(self, response):
        yield {
            'author_name': response.css('.author-title::text').get(),
            'author_birthday': response.css('.author-born-date::text').get(),
            'author_bornlocation': response.css('.author-born-location::text').get(),
        }
