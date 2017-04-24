# -*- coding: utf-8 -*-
import scrapy
from conespider.items import ConespiderItem
from bs4 import BeautifulSoup

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["bing.com"]
    start_urls = ['https://www.bing.com/images/search?q=traffic+cone&qs=n&form=QBILPG&sp=-1&pq=traffic+cone&sc=8-12&cvid=9D31384C3A0D47E4A62311383C32F3DE&first=1&cw=1680&ch=843']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title
        # let's only gather Time U.S. magazine covers
        # url = response.css("div.refineCol ul li").xpath("a[contains(., 'TIME U.S.')]")
        # yield scrapy.Request(url.xpath("@href").extract_first(), self.parse_page)
