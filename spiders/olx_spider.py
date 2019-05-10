# -*- coding: utf-8 -*-
import scrapy
import numpy as np
from olx.items import OlxItem


class OlxSpiderSpider(scrapy.Spider):
	name = 'olx_spider'
	start_urls = ['https://www.olx.ua/transport/legkovye-avtomobili/?page={}'.format(page) for page in range(1, 501)]

	def parse(self, response):
		# Download all data from ads
		for link in response.css('a.marginright5::attr(href)').extract():
			yield response.follow(link, callback = self.grab)

		# Looking for the next page
		# next_page = response.css('a.pageNextPrev::attr(href)').extract_first()
		# Repeat parsing on next page
		# yield scrapy.Request(url = next_page, callback = self.parse)

	def grab(self, response):
		item = OlxItem()
		
		item['title'] = response.css('div.offer-titlebox h1::text').extract_first().strip()
		item['address'] = response.css('a.show-map-link > strong::text').extract_first().strip()
		item['pub_date'] = ''.join(response.css('em::text').extract()).strip().split(',')[-2].strip()
		item['mark'] = response.css('table.item > tr:contains("Марка") a::text').extract_first('NaN').strip()
		item['model'] = response.css('table.item > tr:contains("Модель") a::text').extract_first('NaN').strip()
		item['year'] = response.css('table.item > tr:contains("Год выпуска") strong::text').extract_first('NaN').strip()
		item['mileage'] = ''.join(response.css('table.item > tr:contains("Пробег") strong::text').extract_first('NaN').strip().split(' ')[:-1])
		item['body_type'] =  response.css('table.item > tr:contains("Тип кузова") strong > a::text').extract_first('NaN').strip()
		item['color'] = response.css('table.item > tr:contains("Цвет") strong > a::text').extract_first('NaN').strip()
		
		opt = [i.strip() for i in response.css('table.item > tr:contains("Доп. опции") strong > a::text').extract()]
		if opt:
			item['add_opt'] = opt
		else:
			item['add_opt'] = 'NaN'

		item['fuel'] = response.css('table.item > tr:contains("Вид топлива") strong > a::text').extract_first('NaN').strip()
		item['engine_vol'] = ''.join(response.css('table.item > tr:contains("Объем двигателя") strong::text').extract_first('NaN').strip().split()[:-1])
		item['gearbox'] = response.css('table.item > tr:contains("Коробка передач") strong > a::text').extract_first('NaN').strip()
		
		cond = [i.strip() for i in response.css('table.item > tr:contains("Состояние машины") strong > a::text').extract()]
		if cond:
			item['condition'] = cond
		else:
			item['condition'] = 'NaN'
		
		item['cleared'] = response.css('table.item > tr:contains("Растаможена") strong > a::text').extract_first('NaN').strip()
		
		mult = [i.strip() for i in response.css('table.item > tr:contains("Мультимедиа") strong > a::text').extract()]
		if mult:
			item['multimedia'] = mult
		else:
			item['multimedia'] = 'NaN'
		
		sec = [i.strip() for i in response.css('table.item > tr:contains("Безопасность") strong > a::text').extract()]
		if sec:
			item['security'] = sec
		else:
			item['security'] = 'NaN'

		oth = [i.strip() for i in response.css('table.item > tr:contains("Прочее") strong > a::text').extract()]
		if oth:
			item['other'] = oth
		else:
			item['other'] = 'NaN'

		item['owner_note'] = ' '.join([i.strip() for i in response.css('#textContent::text').extract()])
		item['views'] = response.css('div.pdingtop10 > strong::text').extract_first('NaN').strip()
		item['price'] = ''.join(response.css('strong.xxxx-large::text').extract_first().strip().split()[:-1])
		item['currency'] = response.css('strong.xxxx-large::text').extract_first().strip().split()[-1]

		yield item
