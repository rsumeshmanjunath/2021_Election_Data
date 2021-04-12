 # -*- coding: utf-8 -*-
import scrapy

class QoutesSpider(scrapy.Spider):
    name = "candidates"

    start_urls = ['https://affidavit.eci.gov.in/']

    def parse(self, response):
        self.logger.info('Hello this is my first spider')
        candidates = response.xpath('//div[@class="details-name"]')
        for candidate in candidates:
            temp = candidate.xpath('./div/div/p/text()').getall()
            yield {
                'name': candidate.xpath('./h4/text()').get(),
                'party' : temp[0],
                'status' : candidate.xpath('./div/div/p/strong/font/text()').get(),
                'state' : temp[2],
                'constituency' : temp[3],
            }

#        yield from response.follow_all(css='li.page-item a', callback=self.parse)
