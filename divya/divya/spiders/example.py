# IMPORTING ALL THE DEPENDENCIES
import scrapy
from scrapy_splash import SplashRequest
from ..items import DivyaItem




class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls =['https://www.e.leclerc/cat/sport-loisirs']

    # SPLASH REQUEST : All the request made via splash server and javascript also get rendered.
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5}, endpoint='render.html')

    # EXTRACTING ELEMENTS
    def parse(self, response):


        elements=response.css('a.child-title::attr(href)').extract()

        # loop over 'href' in the sports category
        for i in elements:
            url = response.urljoin(i)
            yield scrapy.Request(url, callback=self.parse_contentzz)

        yield scrapy.Request('https://www.e.leclerc/cat/vetements',self.parse)
        for i in elements:
            url = response.urljoin(i)
            yield scrapy.Request(url, callback=self.parse_contentzz)




    # extracting all the data inside each link
    def parse_contentzz(self,response):
        item = DivyaItem()

        # product tag where all other desired constraint reside
        products = response.css('div.product')
        for items in products:
            nam = items.css('.product-label::text').get()
            brand = items.css('.product-brand::text').get()
            ori_price = items.css('.price-strike::text').get()
            dis_price = items.css('.price-unit::text').get()
            img_url = items.css('.img-fluid::attr(src)').get()
            product_url = items.css('.product-visual::attr(href)').get()
            product_category = items.css('.seller-link::text').get()


            item['nam'] = nam
            item['brand'] = brand
            item['ori_price'] = ori_price
            item['dis_price'] = dis_price
            item['img_url'] = img_url
            item['product_url'] = product_url
            item['product_category'] = product_category

            yield item













