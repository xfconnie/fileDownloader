'''
Created on Aug 24, 2015

@author: v-shayi
'''
import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', '-o', 'output.xml', '-t', 'xml', 'pdfDownloader'])

if __name__ == '__main__':
    main()