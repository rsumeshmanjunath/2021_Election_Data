# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from itemloaders.processors import Join, MapCompose, TakeFirst

def in_process_candidate_name(name):
    return name.upper()

def in_process_age(text):
    if text.isdigit():
        return text
    else:
        return -1

def in_process_gender(text):
    return text.capitalize()

class DocDownloaderItem(Item):
    file_url = Field()
    file_result = Field()
    file_name = Field()

class CandidateItem(Item):
    candidate_name = Field(input_processor=MapCompose(in_process_candidate_name), output_processor=TakeFirst())
    party = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    state = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    constituency = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    status = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    age = Field(input_processor=MapCompose(in_process_age), output_processor=TakeFirst())
    gender = Field(input_processor=MapCompose(in_process_gender), output_processor=TakeFirst())

    
class FullCandidateItem(Item):
    candidate_name = Field(input_processor=MapCompose(in_process_candidate_name), output_processor=TakeFirst())
    party = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    state = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    constituency = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    status = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    age = Field(input_processor=MapCompose(in_process_age), output_processor=TakeFirst())
    gender = Field(input_processor=MapCompose(in_process_gender), output_processor=TakeFirst())
    file_url = Field()
    file_result = Field()

