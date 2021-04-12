# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy_tutorial.items import DocDownloaderItem



def process_value(value) :
  m = re.search("*", value)
  if m :
    return m.group(1)


class DocSpider(scrapy.Spider):
   name = "doc_download_spider"

   start_urls = ['https://affidavit.eci.gov.in/']

   def parse(self, response):
       relative_url = 'affidavit-pdf-download/aHR0cHM6Ly9zdXZpZGhhLmVjaS5nb3YuaW4vdXBsb2FkczEvYWNhZmZpZGF2aXQvRTEwLzIwMjEvQUMvUzI1LzE2MC9TMjVfMTY5MDZfMTEzMzlfMjAyMTA0MDcwODEyMTYxNjE3ODA2NTM2LnBkZg=='
       absolute_url = response.urljoin(relative_url)
       loader = ItemLoader(item = DocDownloaderItem(), response=response)
       loader.add_value('file_url', absolute_url)
       loader.add_value('file_name',"test.pdf")
       yield loader.load_item()
