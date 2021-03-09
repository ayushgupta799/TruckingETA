# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TruckingtimeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    location = scrapy.Field()
    state = scrapy.Field()
    averageSpeed = scrapy.Field()
    peakAvgSpeed = scrapy.Field()
    nonPeakAvgSpeed = scrapy.Field()
    deltaChange = scrapy.Field()