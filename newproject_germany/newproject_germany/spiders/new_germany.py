import scrapy


class NewGermanySpider(scrapy.Spider):
    name = "new_germany"
    #allowed_domains = ["de.wikipedia.org"]
    start_urls = ["https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9F-_und_Mittelst%C3%A4dte_in_Deutschland"]

    def parse(self, response):
        rows = response.xpath("//table[@class='wikitable sortable zebra'][2]/tbody/tr") 
       
        for row in rows:
             
            city = row.xpath(".//td[2]/a/text()").get()
            region = row.xpath(".//td[9]/text()").get()
            population = row.xpath(".//td[8]/text()").get()                       
                            
          
            yield{
                "country" : 'Germany',
                "region" :region, 
                "city" : city,
                "population":population
                }
            