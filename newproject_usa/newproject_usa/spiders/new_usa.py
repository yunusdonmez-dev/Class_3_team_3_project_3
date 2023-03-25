import scrapy


class NewUsaSpider(scrapy.Spider):
    name = "new_usa"
   # allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"]
   

    def parse(self, response):
      
        
        usa_row=response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody').css("tr")
      
        for row in usa_row[1:]:
            # print(row)
            usa_list=row.css("td ::text").getall()
            
            
            if usa_list:
            
                city=usa_list[0].strip()
                
               
                if "[" in usa_list[1]:
                    population=usa_list[5].strip().split(',')
                    population="".join(population)
                    population=int(population)
                    
                    region=usa_list[3].strip()
                    
                else:
                    population=usa_list[4].strip().split(',')
                    population="".join(population)
                    population=int(population)
                   
                    region=usa_list[2].strip()
                
                
                
            yield {"country":"USA","city":city,"population":population,"region":region}
