import scrapy

class LinkedJobsSpider(scrapy.Spider):
    name= "linkedin_jobs"
    api_url= 'https://www.linkedin.com/jobs/search/?currentJobId=3918380402&distance=25&geoId=100506914&keywords=junior%20marketing%20manager&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true&start=25'
    
    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback= self.parse_job, meta={'first_job_on_page':first_job_on_page})
    
    def parse_job(self, response):
        first_job_on_page= response.meta['first_job_on_page']
        
        jobs = response.css("li")
        
        for jobs in jobs:
            job_item['job_title']= job.csss("h3::text").get(default='not-found').strip()
            job_item['job_detail_url']= job.csss(".base-card_full_link::attr(href)").get(default='not-found').strip()
            job_item['job_LISTED']= job.csss("time::text").get(default='not-found').strip()
            
            job_item['company_name']= job.csss("h4 a::text").get(default='not-found').strip()
            job_item['company_link']= job.csss("h4 a::attr(href)").get(default='not-found').strip()
            job_item['company_location']= job.csss(".job-search-card_location::text").get(default='not-found').strip()
            yield job_item