from scrapers import internshala, indeed

def get_all_jobs(keyword, location):
    jobs = []
    jobs.extend(internshala.fetch_jobs(keyword, location))
    jobs.extend(indeed.fetch_jobs(keyword, location))
    return jobs
