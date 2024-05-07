import scrapy

class LinkedJobsSpider(scrapy.Spider):
    name= "linkedin_jobs"
    api_url= 'https://www.linkedin.com/jobs/search/?currentJobId=3918380402&distance=25&geoId=100506914&keywords=junior%20marketing%20manager&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true&start=25'
    
    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback= self.parse_job, meta{'first_job_on_page':first_job_on_page})