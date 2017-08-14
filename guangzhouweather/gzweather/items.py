# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GzweatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    date = scrapy.Field()
    maxtemp = scrapy.Field()
    mintemp = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
    power = scrapy.Field()
    pass
