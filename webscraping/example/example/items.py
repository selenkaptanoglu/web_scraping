# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kitapAdi = scrapy.Field()
    kitapFiyati = scrapy.Field()
    kategori = scrapy.Field()
    yildizSayisi = scrapy.Field()
    durum = scrapy.Field()
    aciklama = scrapy.Field()

