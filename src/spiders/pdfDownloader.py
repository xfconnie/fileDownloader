'''
Created on Aug 21, 2015

@author: v-shayi
'''
import scrapy
import logging
from src.items import pdfItem
from src import settings


class MyClass(scrapy.Spider):
    name = "pdfDownloader"
    allowed_domains = ["usda.mannlib.cornell.edu"]
    start_urls = ["http://usda.mannlib.cornell.edu/MannUsda/viewDocumentInfo.do?documentID=1002"]
    
    def parse(self, response):
        sel = scrapy.Selector(response)
        years = sel.xpath('//div[@id="archived-docs"]/div/div')
        items = []
        
        for year in years:
            itemYear = year.xpath('a/text()').extract()
            pdfList = year.xpath('div[contains(@id, "pdf")]')
            for pdf in pdfList:
                item = pdfItem()
                item['year'] = itemYear
                item['name'] = pdf.xpath('@id').extract()
                item['file_urls'] = pdf.xpath('a/@href').extract()
                items.append(item)
        return items