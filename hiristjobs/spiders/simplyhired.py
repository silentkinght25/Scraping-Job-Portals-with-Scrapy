import scrapy
import random


class SimplyhiredSpider(scrapy.Spider):
    name = "simplyhired"
    allowed_domains = ["www.simplyhired.co.in"]
    user_agents = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.3.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',


        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    ]

    user_agent_index = 0
    requests_per_user_agent = 4
    # use priority in each request 
    # use delay to avoid 429 status error code
    # use multiple user agent so as to reduce chances of getting blocked 429

    def start_requests(self):
        start_urls = [
            "https://www.simplyhired.co.in/search?l=mumbai%2C+maharashtra&job=z8yBECFneLPIYhPHy2tfGcT-GPcosH-ziAzXJODvuop_zEJD_GL4Xg",
            "https://www.simplyhired.co.in/search?l=bengaluru%2C+karnataka&job=hod8w-UxvPL2wjLVjtLG8B69hucBZb0dYW1nzGvdEBKXdv2nPc9JYg",
            "https://www.simplyhired.co.in/search?l=chennai%2C+tamil+nadu&job=XjREJDbgstoid9CPxMIsfMatBK9L0T_DxhGvlMfrW1geavK65Zt3VA",
            "https://www.simplyhired.co.in/search?l=pune%2C+maharashtra&job=u3foFDmKnfv7KigeyqIOVY8-ifqepPzydJHS3DZVqSK9yh16BvjlFA",
            "https://www.simplyhired.co.in/search?l=hyderabad%2C+telangana&job=--r9oEDEbleP1SfAIIHE9i_mMwMHHhlrUyEKTX5pzrGawRfguJj_8w",
            "https://www.simplyhired.co.in/search?l=delhi%2C+delhi&job=AVIN2yydE-ZFMBL400-f_dmfWBudQXTjsvxVESvaSCX6IpxJ9hKy-Q",
            "https://www.simplyhired.co.in/search?l=ahmedabad%2C+gujarat&job=19OOwvN-T8CM5ggFkMsjJmS47eOftIoktE0HMFVL6xvrwRacL8CvPQ",
            "https://www.simplyhired.co.in/search?l=gurgaon%2C+haryana&job=C_naagiCqER5Iz2FyC497h_IEOH3kGZo_phODnwRVeAvwUNObYQP7g",
            "https://www.simplyhired.co.in/search?l=noida%2C+uttar+pradesh&job=mKWnMVR49zxEVsopT_WGQ5PYp5GOFCpDkPJ43EZE0Xo_ESxnz32ycw",
            "https://www.simplyhired.co.in/search?l=kolkata%2C+west+bengal&job=1ATnp84Yd4629KIsuZpewXkpm2O7q1yEB_hud5VCQf8WLVxmkkJoOQ",
            "https://www.simplyhired.co.in/search?l=coimbatore%2C+tamil+nadu&job=YxfrZF7ni1IZCPCv2EgjPSVGQnhEoCspbdKu8G9KcuIPXrJ6zq-DcQ",
            "https://www.simplyhired.co.in/search?l=jaipur%2C+rajasthan&job=sbNgrlAVAcLXbwiJOnym_nB_ey6q7WxucSCZKI5iIIXLaBgndFlceg",
            "https://www.simplyhired.co.in/search?l=mohali%2C+punjab&job=Hm_F5S6C76QKWBayILMqt11027-ilqdtR8rRYKEMhtAWlRosXtF74w"
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, 
                                 callback=self.parse, 
                                 headers={'User-Agent': self.get_current_user_agent()},
                                 priority = 10)

    def parse(self, response):
        user_agent = response.request.headers.get('User-Agent')
        jobs = response.xpath("//ul[@id='job-list']/li/article/div")
        for job in jobs:
            job_details = job.xpath(".//div[@class='jobposting-title-container']/h3/a/@href").get()
            #print(job_details)
            for _ in range(self.requests_per_user_agent):
                yield response.follow(url=job_details, 
                                    callback = self.parse_jobs,
                                    headers={'User-Agent': self.get_current_user_agent()},
                                    priority = 5)

        next_page = response.xpath("//li[@class='next-pagination']/a/@href").get()
        if next_page:
            next_page = f'https://www.simplyhired.co.in{next_page}'
            yield scrapy.Request(url=next_page, 
                                 callback=self.parse,
                                 headers={'User-Agent': user_agent},
                                 priority=8)    

    def parse_jobs(self, response):

        user_agent = response.request.headers.get('User-Agent')
        # print(f'user_agent:: {user_agent}')

        qualification_list = response.xpath("//div[contains(@class,'viewjob-qualifications')]/ul[@class='Chips']/li/text()").getall()
        qualification = [skill.strip() for skill in qualification_list if skill.strip()]

        job_type = response.xpath("//span[@data-testid='VJ-jobDetails-jobType']/span/text()").get()
        if job_type:
            job_type = response.xpath("//span[@data-testid='VJ-jobDetails-jobType']/span/text()").get()
        else:
            job_type = 'NA'    
        
        yield{
            'Company Name': response.xpath("//div[@class='viewjob-container']/div/div[@class='viewjob-labelWithIcon'][1]/text()").get(),
            'Title': response.xpath("//h2[@class='viewjob-jobTitle h2']/text()").get(),
            'Location': response.xpath("//div[@class='viewjob-container']/div/div[@class='viewjob-labelWithIcon'][2]/text()").get(),
            'qualification': qualification,
            'Job Type': job_type,
            'user_agent': user_agent
        }        

    def get_current_user_agent(self):
        user_agent = self.user_agents[self.user_agent_index]
        self.user_agent_index = (self.user_agent_index + 1) % len(self.user_agents)
        return user_agent    