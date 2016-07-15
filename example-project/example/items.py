# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class SearchItem(Item):
    '''
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()
    '''
    crawled = Field()
    spider = Field()
    url = Field()
    #title = Field()
    abstract = Field()
    query = Field()
    relatedQuery = Field()


class ExampleLoader(ItemLoader):
    default_item_class = SearchItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
