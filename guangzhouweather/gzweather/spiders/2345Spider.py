# coding: utf-8

import scrapy
from gzweather.items import GzweatherItem


class TtffSpider(scrapy.Spider):
	# name定义spider名字的字符串，唯一的，必须的
	# 可以生成多个spider实例
	name = 'tianqi'
	# allowed_domains包含了允许爬取的域名列表
	allowed_domains = ['lishi.tianqi.com']
	# start_urls是URL列表
	# 当没有指定特定的URL时，spider将从该列表开始进行爬取
	start_urls = ['http://lishi.tianqi.com/guangzhou/201101.html']
	# custom_setting是一个dict，当启动spider时，该设置将会覆盖项目级的设置
	custom_settings = {}
	# crawler在初始化class后，由类方法from_crawler()设置
	# 并且链接了本spider实例对应的Crawler对象
	# Crawler包含了很多项目中的组件,作为单一的入口点 (例如插件,中间件,信号管理器等)

	# settings是一个setting实例

	# logger与spider的名字一起创建，可以用来发送日志信息

	# from_crawler()设置crawler和setting属性

	# start_requests()返回一个iterable，包含了spider用于爬取的第一个Request
	# 只被scrapy调用一次，可以实现为生成器

	# make_requests_from_url()返回用于爬去的Request对象

	# parse()默认的回调函数
	# parse负责处理response并返回处理的数据以及(/或)跟进的URL
	# Spider对其他的Request的回调函数也有相同的要求
	def parse(self, response):
		# 回调函数必须返回一个包含Request, dict或Item的可迭代的对象
		self.logger.info('A response from %s just arrived!', response.url)
		# 在此项目中一直response是html_reponse
		# 实例化Selector
		sel = scrapy.Selector(response)
		title = sel.xpath('//title/text()').extract_first()
		# gzitem['title'] = title
		print u'打印输出**************'
		print 'title:', title
		uls = sel.xpath('//div[@class="tqtongji2"]/ul')
		# print 'uls:', uls.extract()
		for index, ul in enumerate(uls):
			gzitem = GzweatherItem()
			if index == 0:
				continue
			args = ul.xpath('li/text()').extract()
			if len(args) == 5:
				gzitem['date'] = ul.xpath('li/a/text()').extract()[0]
				gzitem['maxtemp'] = args[0]
				gzitem['mintemp'] = args[1]
				gzitem['weather'] = args[2]
				gzitem['wind'] = args[3]
				gzitem['power'] = args[4]
				yield gzitem
			elif len(args) == 6:
				gzitem['date'] = args[0]
				gzitem['maxtemp'] = args[1]
				gzitem['mintemp'] = args[2]
				gzitem['weather'] = args[3]
				gzitem['wind'] = args[4]
				gzitem['power'] = args[5]
				yield gzitem
		# for h3 in response.xpath('//h3').extract():
		# 	yield GzweatherItem(date=h3)
		print '#####'
		print '#####'
		# print sel.xpath('//div[contains(@id, "tool_site")]/div[1]/span[1]/a[last()]/@href').extract()
		for url in sel.xpath('//div[contains(@id, "tool_site")]/div[1]/span[1]/a[last()]/@href').extract():
			print 'url: ', url
			# //span[@class="tqxiangqing"/a[2]]
			# '//a/@href'
			yield scrapy.Request(url, self.parse)
		pass

	# log(message[, level, component])
	# 使用scrapy.log.msg()方法记录(log)message
	# 自动带上该spider的name属性，封装了通过logger来发送log消息的方法，向后兼容

	# closed(reason)spider关闭时调用
	# 替代调用signals.connect()来监听spider_closed信号的快捷方式
