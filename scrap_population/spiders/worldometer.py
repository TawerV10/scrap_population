import scrapy
import json

class WorldometerSpider(scrapy.Spider):
    name = 'worldometer'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        data = []

        rows = response.xpath('//tbody/tr')
        for row in rows:
            country = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

            print(country, population)

            data.append({
                'country': country,
                'population': population
            })

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)