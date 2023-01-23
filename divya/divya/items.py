# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DivyaItem(scrapy.Item):
    # define the fields for  item scraped  here:
    nam = scrapy.Field()
    brand = scrapy.Field()
    ori_price = scrapy.Field()
    dis_price = scrapy.Field()
    img_url = scrapy.Field()
    product_url = scrapy.Field()
    product_category = scrapy.Field()
    pass
