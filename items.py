# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ticket(scrapy.Item):
    price = scrapy.Field()
    departure_time = scrapy.Field()
    arrival_time = scrapy.Field()
    is_nonstop = scrapy.Field()
    airline = scrappy.Field()
    
