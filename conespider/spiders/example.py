# -*- coding: utf-8 -*-
import scrapy
from conespider.items import ConespiderItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["bing.com"]
    start_urls = ['https://www.bing.com/images/search?q=traffic+cone&qs=n&form=QBILPG&sp=-1&pq=traffic+cone&sc=8-12&cvid=9D31384C3A0D47E4A62311383C32F3DE&first=1&cw=1680&ch=843']

    def parse(self, response):
        pass
