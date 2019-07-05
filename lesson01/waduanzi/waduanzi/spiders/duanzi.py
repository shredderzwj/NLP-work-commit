# -*- coding: utf-8 -*-
import scrapy
from waduanzi.items import WaduanziItem
from urllib.parse import urlparse


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['www.waduanzi.com']
    start_urls = [
        'http://www.waduanzi.com/joke/page/1',
        'http://www.waduanzi.com/joke/page/300',
        'http://www.waduanzi.com/joke/page/600',
        'http://www.waduanzi.com/joke/page/900',
        'http://www.waduanzi.com/joke/page/1200',
        'http://www.waduanzi.com/joke/page/1500',
        'http://www.waduanzi.com/joke/page/1800',
        'http://www.waduanzi.com/joke/page/2100',
    ]

    def parse(self, response):
        item = WaduanziItem()
        divs = response.xpath('//div[@class="panel panel20 post-item post-box"]')
        for div in divs:
            try:
                title = div.xpath('.//a[@class="cd-title-link"]/@title').extract_first()
                url = div.xpath('.//a[@class="cd-title-link"]/@href').extract_first()
                id = url.split('/')[-1]
                content = div.xpath('.//div[@class="item-content"]/text()').extract_first()
                content = content.replace('\n', '').replace('\t', '').replace(' ', '')
                likes = int(div.xpath('.//a[@data-score="1"]/text()').extract_first().strip())
                unlikes = int(div.xpath('.//a[@data-score="-1"]/text()').extract_first().strip())
                item['id'] = id
                item['url'] = url
                item['title'] = title
                item['content'] = content
                item['likes'] = likes
                item['unlikes'] = unlikes
                yield item
            except:
                pass

        # 翻页
        root_url = "%s://%s" % (urlparse(response.url)[0], urlparse(response.url)[1])
        next_url_path = response.xpath('//ul[@id="yw1"]//li[@class="next"]//a/@href').extract_first()
        if next_url_path is not None:
            next_num = next_url_path.split('/')[-1]
            if next_num not in ['300', '600', '900', '1200', '1500', '1800', '2100']:
                next_url = root_url + next_url_path
                yield scrapy.Request(next_url, callback=self.parse)
                print(next_num)

