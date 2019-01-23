# -*- coding: utf-8 -*-
import json

import scrapy

from visafree.items import Countrypair

class HenleySpider(scrapy.Spider):
    name = 'henley'
    allowed_domains = ['www.henleypassportindex.com']
    start_urls = ['https://www.henleypassportindex.com/country/list']

    def parse(self, response):
        countrylist = json.loads(response.body_as_unicode())
        for country in countrylist:
            yield scrapy.Request("https://www.henleypassportindex.com/fetch?url=passports%2F{}%2Fcountries".format(country['code']), callback = self.parse_country, meta = {'passport': country['code']})

    def parse_country(self, response):
        countrypermissions = json.loads(response.body_as_unicode())
        for country in countrypermissions:
            item = Countrypair()
            item['passport'] = response.meta['passport']
            item['to'] = country['code']
            item['visafree'] = country['pivot']['is_visa_free']
            yield item
