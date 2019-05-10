# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
	title = scrapy.Field()
	address = scrapy.Field()
	pub_date = scrapy.Field()
	mark = scrapy.Field()
	model = scrapy.Field()
	year = scrapy.Field()
	mileage = scrapy.Field()
	body_type = scrapy.Field()
	color = scrapy.Field()
	add_opt = scrapy.Field()
	fuel = scrapy.Field()
	engine_vol = scrapy.Field()
	gearbox = scrapy.Field()
	condition = scrapy.Field()
	cleared = scrapy.Field()
	multimedia = scrapy.Field()
	security = scrapy.Field()
	other = scrapy.Field()
	owner_note = scrapy.Field()
	views = scrapy.Field()
	price = scrapy.Field()
	currency = scrapy.Field()