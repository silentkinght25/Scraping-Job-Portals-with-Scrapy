import scrapy
from scrapy.http import Headers
from scrapy.utils.project import get_project_settings
import os

# Get the project settings
settings = get_project_settings()

# Specify the full path to the proxy list file
proxy_list_path = r'C:\Users\Ashwani Singh\projects\hiristjobs\proxy\proxy_list.txt'
print(proxy_list_path)
# Update the PROXY_LIST setting with the full path
settings.set('PROXY_LIST', proxy_list_path)

class FounditSpider(scrapy.Spider):
    name = "foundit"
    allowed_domains = ["www.foundit.in"]
    start_urls = [
        "https://www.foundit.in/search/freshers-jobs-1?searchId=45a2d8ae-3de9-4219-aa1f-e8f39b57752d",
        "https://www.foundit.in/search/it-jobs-1?searchId=4cd9def3-8306-48f3-8c88-21ec08e83a80",
        "https://www.foundit.in/search/java-jobs-1?searchId=6678f976-8970-4bd7-b933-72f6a0969e24",
        "https://www.foundit.in/search/hr-executive-jobs-1?searchId=0ca21b8e-c8ce-4e80-9620-492f7909e182",
        "https://www.foundit.in/search/manual-testing-jobs-1?searchId=f8083d4e-c9a3-4595-a2e2-0cd47f88e269",
        "https://www.foundit.in/search/work-from-home-jobs-1?searchId=60917068-eb55-4b2a-a92e-cd6f5c8081a6",
        "https://www.foundit.in/search/software-engineer-jobs-1?searchId=e35ba34b-e03d-4862-a62d-81ccae0494da",
        "https://www.foundit.in/search/business-analyst-jobs-1?searchId=524a902e-4bbc-43cd-993a-a81c1fd62e04"
        ]

    def parse(self, response):
        header_s = Headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
        })
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_jobs, 
                                 headers=header_s, 
                                 meta={'proxy': self.proxy})

    def parse_jobs(self, response):
        header_s = Headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
        })
        for job in response.xpath("//div[contains(@class, 'cardContainer')]"):
            
            skill_labels = job.xpath(".//div[@class='skillDetails']//label/a/text()").getall()
            skills = [label.strip() for label in skill_labels if label.strip()]

            salary_desc = job.xpath(".//div[@class='bodyRow']/div[@class='addEllipsis']/span[@class='details']")
            if salary_desc:
                salary = salary_desc.xpath("normalize-space(.)").get()
            else:
                salary = 'NA'    
            yield{
                'company_name': job.xpath("./div/div/div[@class='companyName']/a/text()").get(),
                'title': job.xpath("./div[@class='cardHead']/div/div/h3/a/text()").get(),
                'years_of_exp': job.xpath("./div[@class='cardBody']/div[3]/div[2]/text()").get(),
                'Job_type': job.xpath("./div[@class='cardBody']/div/div[@class='addEllipsis']/a/text()").get(),
                #/div[@class="cardBody"]/div)[1]/div[2]/a/text()   ---job type
                'Location': job.xpath("./div[@class='cardBody']/div[2]/div[2]/div/a/text()").get(),
                'skills': skills,
                'salary': salary
            }
        next_page = response.xpath("(//div[@class='number']/following-sibling::a)[last()]/@href").get()
                                    #(//div[@class='pagination']//div[@class='number']/a)[last()]/@href
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_jobs, 
                                 headers=header_s, 
                                 meta={'proxy': self.proxy})

            #yield response.follow(url=country_link, callback = self.parse_country)



       
       