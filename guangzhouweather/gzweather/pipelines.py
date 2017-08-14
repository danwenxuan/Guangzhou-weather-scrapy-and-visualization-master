# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class GzweatherPipeline(object):
	# def __init__(self):
	# 	self.file = '??'

	def process_item(self, item, spider):
		if True:
			return item
		else:
			raise DropItem('reason')


# class CsvWriterPipeline(object):
# 	def __init__(self):
# 		self.file = open('items.csv', 'wb')
#
# 	def process_item(self, item, spider):
# 		pass
