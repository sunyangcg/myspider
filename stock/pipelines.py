# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class StockPipeline:
    def process_item(self, item, spider):

        item.get('stock_id')

        self.file = codecs.open(item.get('stock_id') + '.cvs' ,"a+" ,encoding='utf-8')
        self.file.write(item.get('today') + '\t')
        self.file.write(item.get('stock_id') + '\t')
        self.file.write(item.get('stock_name') + '\t')
        self.file.write(item.get('stock_price') + '\t')
        self.file.write(item.get('stock_gains') + '\t')
        self.file.write(item.get('stock_rate') + '\t')
        self.file.write(item.get('stock_thanCarrie') + '\t')
        self.file.write(item.get('stock_amplitude') + '\n')

        return item 
    def spider_closed(self, spider):
        self.file.close()
        
