from scrapers import internshala, indeed


def get_all_jobs(keyword, location, pages=3):
    jobs = []
    jobs.extend(indeed.fetch_jobs(keyword, location, pages))
    jobs.extend(internshala.fetch_jobs(keyword, pages))
    return jobs
