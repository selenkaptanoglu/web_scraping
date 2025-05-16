import scrapy
from ..items import ExampleItem


class DenemeSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for href in response.xpath("//article[@class='product_pod']/h3/a/@href").getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_page(self, response):
        item = ExampleItem()

        kitapAdi = response.xpath("//div[contains(@class, 'product_main')]/h1/text()").get()
        kitapFiyati = response.xpath("//p[@class='price_color']/text()").get()
        kategori = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        yildiz_str = response.xpath("//p[contains(@class, 'star-rating')]/@class").get()
        yildizSayisi = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}.get(
            yildiz_str.replace("star-rating ", ""), 0)

        durum = response.xpath("normalize-space(//p[contains(@class, 'instock')])").get()

        aciklama = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        if aciklama:
            aciklama = aciklama.strip()
        else:
            aciklama = ''

        item['kitapAdi'] = kitapAdi
        item['kitapFiyati'] = kitapFiyati
        item['kategori'] = kategori
        item['yildizSayisi'] = yildizSayisi
        item['durum'] = durum
        item['aciklama'] = aciklama

        yield item
