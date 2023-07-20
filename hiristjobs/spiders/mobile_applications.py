import scrapy
import json
# --mobile app
# --frontend dev
# --backend dev
# --data analyst
# --dev ops
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/2?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/1?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/7?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/8?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false

# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/3?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/4?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/6?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/9?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/10?pageNo=1&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/11?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/12?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false
# https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/13?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false




class MobileApplicationsSpider(scrapy.Spider):
    name = "mobile_applications"
    allowed_domains = ["hirist.com"]
    start_urls = ["https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false"]

    next_page_num = 0
    def parse(self, response):
         
         resp = json.loads(response.body)
         count = resp.get('count')
         jobs = resp.get('jobs')
         for job in jobs:
              yield{
                  'companyName' : job.get('companyData').get('companyName'),
                  'page_no': self.next_page_num,
                #  'location' : job.get('location').get('name'),
                  'title' : job.get('title'),
                  'min_years' : job.get('min'),
                 'max_years' : job.get('max'),
                 'work_from_home' : job.get('workFromHome'),
                 'has more':resp.get('hasMore')
             }
            
         has_next = resp.get('hasMore')
         if has_next:
             self.next_page_num += 1
             absolute_url =  f'https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo={self.next_page_num}&loc=&minexp=0&maxexp=30&boostJobs=false'
             print(f'Next Page: {absolute_url}')
             yield scrapy.Request(
                 url = absolute_url,
                 callback= self.parse
             )

###################################################################################################
# import json
# import scrapy

# class MobileApplicationsSpider(scrapy.Spider):
#     name = "mobile_applications"
#     allowed_domains = ["www.hirist.com"]
#     start_urls = ["https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false"]

#     def parse(self, response):
#         resp = json.loads(response.body)
#         jobs = resp.get('jobs')

#         for job in jobs:
#             link = job.get('url')
#             yield scrapy.Request(link, callback=self.parse_job_tags)

#         has_next = resp.get('hasMore')
#         if has_next:
#             self.next_page_num += 1
#             next_url = f'https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo={self.next_page_num}&loc=&minexp=0&maxexp=30&boostJobs=false'
#             yield scrapy.Request(next_url, callback=self.parse)

#     def parse_job_tags(self, response):
#         # Parse the tags associated with each job
#         resp = json.loads(response.body)
#         tags = resp.get('tags')

#         yield {
#             'url': response.url,
#             'tags': tags
#         }
