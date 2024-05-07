import scrapy

class LinkedJobsSpider(scrapy.Spider):
    name= "linkedin_jobs"
    api_url= 'https://de.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=junior%2BMarketing%2BManager&location=Metropolregion%2BM%C3%BCnchen&geoId=90009735&trk=public_jobs_jobs-search-bar_search-submit&start=150'
    
    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback= self.parse_job, meta={'first_job_on_page':first_job_on_page})
    
    def parse_job(self, response):
        first_job_on_page= response.meta['first_job_on_page']
        
        jobs = response.css("li")
        
        num_jobs_returned = len(jobs)
        print("******** Num Jobs Returned********")
        print(num_jobs_returned)
        
        
        for jobs in jobs:
            job_item['job_title']= job.csss("h3::text").get(default='not-found').strip()
            job_item['job_detail_url']= job.csss(".base-card_full_link::attr(href)").get(default='not-found').strip()
            job_item['job_LISTED']= job.csss("time::text").get(default='not-found').strip()
            
            job_item['company_name']= job.csss("h4 a::text").get(default='not-found').strip()
            job_item['company_link']= job.csss("h4 a::attr(href)").get(default='not-found').strip()
            job_item['company_location']= job.csss(".job-search-card_location::text").get(default='not-found').strip()
            yield job_item
            
        if num_jobs_returned>0:
            first_job_on_page= int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page'})
            