import json
import scrapy

class MobileApplicationsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["hirist.com"]
    start_urls = [
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/5?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/2?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/1?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/7?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/8?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/3?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/4?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/6?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/9?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/10?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/11?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/12?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false",
        "https://jobseeker-api.hirist.com/v2/jobfeed/-1/v3/catJobs/13?pageNo=0&loc=&minexp=0&maxexp=30&boostJobs=false"
    ]

    def parse(self, response):
        # Iterate through the start URLs
        for url in self.start_urls:
            ## Initialize the meta data for each request
            #The meta attribute is used to keep track of the total count of jobs and the number of jobs already crawled.
            yield scrapy.Request(url, callback=self.parse_jobs, meta={'total_count': None, 'crawled_count': 0})
    
    def parse_jobs(self, response):
        # Parse the API response
        resp = json.loads(response.body)
        count = resp.get('count')

        # Check if jobs are present in the response
        if count != 0:
            jobs = resp.get('jobs')
            for job in jobs:
                # Extract the location information
                locations = job.get('location')
                location_names = [loc.get('name') for loc in locations]
                yield {
                    'companyName': job.get('companyData').get('companyName'),
                    'title': job.get('title'),
                    'min_years': job.get('min'),
                    'max_years': job.get('max'),
                    'location' : location_names,
                    'work_from_home': job.get('workFromHome'),
                    'femaleCandidate': job.get('femaleCandidate'),
                    'differentlyAbled': job.get('differentlyAbled'),
                    'exDefence': job.get('exDefence'),
                }
                # The meta attribute is initialized in the parse method and passed along with the requests.
                response.meta['crawled_count'] += 1

            has_next = resp.get('hasMore')
            if has_next:
                next_page_num = response.meta.get('page_no', 0) + 1
                base_url = response.url.split('?')[0]
                next_url = f'{base_url}?pageNo={next_page_num}&loc=&minexp=0&maxexp=30&boostJobs=false'
                print(f'\n\n\n\n page_no: {next_page_num}  Next Page: {next_url}\n\n\n')

                # The total_count is obtained from the API response and stored in the meta attribute if it is not already present.
                total_count = response.meta.get('total_count')
                crawled_count = response.meta.get('crawled_count')

                # Before making the next request, the code checks if the total count is known and 
                # if the number of crawled jobs has reached the total count. 
                # If so, the function returns to stop further crawling.
                if total_count is not None and crawled_count >= total_count:
                    return

                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse_jobs,
                    meta={'page_no': next_page_num, 'total_count': total_count, 'crawled_count': crawled_count}
                )

            # Check if the total count is not yet known
            if response.meta['total_count'] is None:
                total_count = resp.get('total', 0)
                response.meta['total_count'] = total_count

