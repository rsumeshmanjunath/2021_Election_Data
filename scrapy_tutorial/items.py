# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from itemloaders.processors import Join, MapCompose, TakeFirst, Identity, Compose
from datetime import datetime

def remove_quotes(text):
    text = text.strip(u'\u201c'u'\u201d')
    return text

def convert_date(text):
    return datetime.strptime(text,'%B %d, %Y')

def parse_location(text):
    return text[3:]

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


class QuoteItem(Item):
    quote_content = Field(input_processor=MapCompose(remove_quotes), output_processor=TakeFirst())
    tags = Field()
    author_name = Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    author_birthday = Field(input_processor=MapCompose(convert_date), output_processor=TakeFirst())
    author_bornlocation = Field(input_processor=MapCompose(parse_location), output_processor=TakeFirst())

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
#    file_url = Field()
#    file_result = Field()
