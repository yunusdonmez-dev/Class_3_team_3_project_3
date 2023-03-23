import scrapy


class NewHollandSpider(scrapy.Spider):
    name = "new_holland"
   # allowed_domains = ["tr.wikipedia.org"]
    start_urls = ['https://tr.wikipedia.org/wiki/Hollanda%27daki_%C5%9Fehirler_listesi']

    def parse(self, response):
        rows = response.xpath("//table[@class='wikitable sortable']/tbody/tr") 
       
        for row in rows:
            
            region = row.xpath(".//td[7]/a/text()").get()
            city = row.xpath(".//td[2]/a/text()").get()
            population = row.xpath(".//td[6]/text()").get()
            if region == None:
                region= row.xpath(".//td[7]/text()").get()
                
            
            
           
           
            yield{
                "country" : "Holland",
                
                "city" : city,
                "population" : population,
                "region" :region
            }
