import scrapy, re, datetime
from watch_item import WatchItem


class CwSpider(scrapy.Spider):
    name = 'cw'
    allowed_domains = ['creationwatches.com']
    # start_urls = ['http://creationwatches.com/']
    # start_urls = ['https://www.creationwatches.com/products/seiko-automatic-sports-89/seiko-automatic-snk795-snk795k1-snk795k-mens-watch-1709.html?currency=USD']
    start_urls = ['file:///home/vital/work/scrapit/cw01.html']

    def parse(self, response):
        # pass
        item = WatchItem()
        item['url'] = response.url
        # detail_css = response.css('.detail-boxppara.div').getall()
        # for detail in detail_css:
        for detail in response.css('.detail-boxppara'):
            col1 = detail.css(".col1::text").get()
            col2 = detail.css(".col2::text").get()
            if col1 == "Brand:":
                item['brand'] = col2
            elif col1 == "Model:":
                item['model'] = col2
            elif col1 == "Gender:":
                if col2 == "Men's":
                    item['gender'] = "m"
                if col2 == "Women's":
                    item['gender'] = "w"
            # elif col1 == "---caliber---":
            #     item['caliber'] = col2
            elif col1 == "Case Size:":
                item['size'] = col2
            elif col1 == "Case Thickness:":
                item['height'] = col2
        item['usd'] = 0
        usd_re = re.compile(">Price:</span>.*US \$([0-9\.]*)</span>")
        usd_css = response.css('.product-price1').getall()
        for usd_str in usd_css:
            usd_s = usd_re.search(usd_str)
            if usd_s is not None:
                usd_value = usd_s.group(1)
                item['usd'] = float(usd_value)
                break
        # item['rub'] = response.url
        item['last_seen'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if item['brand'] is not None and item['model'] is not None:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(">>> Yields: " + item['brand'] + " " + item['model'] + " price: $" + str(item['usd']))
            yield item


# ">Price:</span>.*US \$([0-9\.]*)</span>"

# SOLD OUT:
# response.xpath('/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/span').get()
