# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 股票代码
    stock_id = scrapy.Field()
    # 公司全称
    stock_name = scrapy.Field()
    # 价格
    stock_price = scrapy.Field()
    # 涨幅
    stock_gains = scrapy.Field()
    # 换手率
    stock_rate = scrapy.Field()
    # 量比
    stock_thanCarrie = scrapy.Field()
    # 振幅
    stock_amplitude = scrapy.Field()

    today = scrapy.Field()
    pass
