# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy_tutorial.items import FullCandidateItem

class FullCandidateSpider(scrapy.Spider):
   name = "full_candidate_item"

   start_urls = ['https://affidavit.eci.gov.in/']

   def parse(self, response):
       self.logger.info('Parse function called on {}'.format(response.url))
       candidates = response.xpath('//div[@class="details-name"]')
       for candidate in candidates:
           temp = candidate.xpath('./div/div/p/text()').getall()
           status = candidate.xpath('./div/div/p/strong/font/text()').get()

           # select only candidates from TN and selected
           if((temp[2].strip() == 'Tamil Nadu') and (status.strip() == 'Accepted')):

               loader = ItemLoader(item = FullCandidateItem(), selector=candidate)

               loader.add_xpath('candidate_name', './h4/text()')
               loader.add_xpath('status','./div/div/p/strong/font/text()')
               loader.add_value('party', temp[0])
               loader.add_value('state', temp[2])
               loader.add_value('constituency', temp[3])

               candidate_item = loader.load_item()

               # go to the candiate page and extract their age and gender.
               candidate_url = candidate.css('a::attr(href)').get()
               yield response.follow(candidate_url, self.parse_candidate, meta={'candidate_item':candidate_item})

       #extract candidate details from remaining pages
       yield from response.follow_all(css='li.page-item a', callback=self.parse)

   def parse_candidate(self, response):

       candidate_item = response.meta['candidate_item']
       details =  response.xpath('//form[@class="form-horizontal"]/div/div/div[@class="form-group"]')

       pdf = response.xpath('//div[@class="aside-af"]/input/@value').get()
       doc_url = 'https://affidavit.eci.gov.in/affidavit-pdf-download/' + pdf
       loader = ItemLoader(item=candidate_item, response=response)
       loader.add_value('file_url', doc_url)
       candidate_item = loader.load_item()

       for detail in details:
           label_name = detail.xpath('./label/p/text()').get()
           if(label_name is not None):
               label_name = label_name.strip()
               if(label_name == "Gender:"):
                    loader = ItemLoader(item=candidate_item, selector=detail)
                    loader.add_xpath('gender', './div/p/text()')
                    candidate_item = loader.load_item()
               elif(label_name == "Age:"):
                    loader = ItemLoader(item=candidate_item, selector=detail)
                    loader.add_xpath('age', './div/p/text()')
                    candidate_item = loader.load_item()

       yield candidate_item
