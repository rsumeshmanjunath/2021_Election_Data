# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mimetypes
import os
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class TestPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None, *, item=None):
        self.logger.info("=========================================================")
        return 'files/' + 'test.pdf'
