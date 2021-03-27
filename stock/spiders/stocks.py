import scrapy
import time
from stock.items import StockItem 


rank_base_page = 'http://q.10jqka.com.cn/index/index/board/hs/field/zdf/order/desc/page/'
rank_base_ss = 'http://q.10jqka.com.cn/index/index/board/ss/field/zdf/order/desc/page/'

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ["q.10jqka.com.cn"
        ]
    start_urls = [
        rank_base_page + "1" ,
        rank_base_ss + "1"
        ]

    def parse(self, response):
        if "q.10jqka.com.cn/index/index/board/hs/field/zdf/order/desc/page" in response.url:
            max = int(response.xpath("//span[@class='page_info']/text()").extract()[0].split('/')[1])
            print('这是列表页面 一共', max, "页")
            yield from self.handlePage(response)
            for i in range(max):
                if i != 1:
                    yield scrapy.Request(rank_base_page + str(i), self.handlePage)
        if "q.10jqka.com.cn/index/index/board/ss/field/zdf/order/desc/page" in response.url:
            max = int(response.xpath("//span[@class='page_info']/text()").extract()[0].split('/')[1])
            print('这是列表页面 一共', max, "页")
            yield from self.handlePage(response)
            for i in range(max):
                if i != 1:
                    yield scrapy.Request(rank_base_ss + str(i), self.handlePage)            
        pass

    def handlePage(self, response):
        print("处理列表页面")
        trs = response.xpath("//tr")
        #open("test.html" , "wb+").writelines(trs).close()
        
        for tr in trs[1:]:
            # 股票代码 简称
            number = tr.xpath(".//a[@target='_blank']")[0].xpath('text()').extract()[0]
            name = tr.xpath(".//a[@target='_blank']")[1].xpath('text()').extract()[0]
            # 股票价格
            price = tr.xpath("./td[4]").xpath('text()').extract()[0]
            # 股票涨幅
            gains = tr.xpath("./td[5]").xpath('text()').extract()[0]
            # 股票换手率
            rate = tr.xpath("./td[8]").xpath('text()').extract()[0]
            # 股票量比
            thanCarrie = tr.xpath("./td[9]").xpath('text()').extract()[0]
            # 股票振幅
            amplitude = tr.xpath("./td[10]").xpath('text()').extract()[0]

            print(name)

            stock = StockItem()

            stock['stock_id'] = number
            stock['stock_name'] = name
            stock['stock_price'] = price
            stock['stock_gains'] = gains
            stock['stock_rate'] = rate
            stock['stock_thanCarrie'] = thanCarrie
            stock['stock_amplitude'] = amplitude
            stock['today'] = time.strftime("%Y-%m-%d", time.localtime())

            yield stock
            
            

#http://q.10jqka.com.cn/index/index/board/ss/field/zdf/order/desc/page/1/ajax/1/
#http://q.10jqka.com.cn/index/index/board/hs/field/zdf/order/desc/page/1/ajax/1/
#http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/
