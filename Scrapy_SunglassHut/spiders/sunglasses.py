import scrapy
import json


class SunglassesSpider(scrapy.Spider):
    name = 'sunglasses'
    allowed_domains = ['sunglasshut.com']
    start_urls = ['https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837?isProductNeeded=true&orderBy=default&pageSize=18&responseFormat=json&isChanelCategory=false&currency=USD&pageView=image&viewTaskName=CategoryDisplayView&orderBy=default&beginIndex=0&categoryId=3074457345626651837&catalogId=20602&langId=-1&currentPage=1&storeId=10152&top=Y&orderBy=default&currentPage=1']

    def parse(self, response):
        data = json.loads(response.body)
        yield from data['plpView']['products']['products']['product']

        next_page = data['plpView']['nextPageURL']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)