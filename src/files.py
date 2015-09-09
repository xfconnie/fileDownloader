'''
Created on Aug 24, 2015

@author: v-shayi
'''
import warnings
from scrapy.exceptions import ScrapyDeprecationWarning
warnings.warn("Module `scrapy.contrib.pipeline.files` is deprecated, "
              "use `scrapy.pipelines.files` instead",
              ScrapyDeprecationWarning, stacklevel=2)

from scrapy.pipelines.files import *