# -*- coding: utf-8 -*-
  
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import *
 
class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
#         return FilesPipeline.file_path(self, request, response=response, info=info)
        fileName = request.url.split('/')[-1]
        return 'full/%s' % (fileName)