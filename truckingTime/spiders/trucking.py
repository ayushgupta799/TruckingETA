import scrapy
from ..items import TruckingtimeItem


class TruckingSpider(scrapy.Spider):
    name = 'trucking'
    allowed_domains = ['www.truckingresearch.org']
    start_urls = ['https://truckingresearch.org/2021/02/23/2021-top-truck-bottlenecks/amp/']

    def parse(self, response):
        items = TruckingtimeItem()

        alldata = response.css('tr:nth-child(n)')
        for data in alldata:
            rank = data.css('.column-1').css('::text').extract()
            location = data.css('.column-2').css('::text').extract()
            state = data.css('.column-3').css('::text').extract()
            averageSpeed = data.css('.column-4').css('::text').extract()
            peakAvgSpeed = data.css('.column-5').css('::text').extract()
            nonPeakAvgSpeed = data.css('.column-6').css('::text').extract()
            deltaChange = data.css('.column-7').css('::text').extract()

            items['rank'] = rank
            items['location'] = location
            items['state'] = state
            items['averageSpeed'] = averageSpeed
            items['peakAvgSpeed'] = peakAvgSpeed
            items['nonPeakAvgSpeed'] = nonPeakAvgSpeed
            items['deltaChange'] = deltaChange

            yield items