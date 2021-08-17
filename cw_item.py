import scrapy
 
class CwItem(scrapy.Item):
    url = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    gender = scrapy.Field()
    caliber = scrapy.Field()
    size = scrapy.Field()
    height = scrapy.Field()
    usd = scrapy.Field()
    rub = scrapy.Field()
    last_seen = scrapy.Field()