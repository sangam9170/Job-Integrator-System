import requests
from bs4 import BeautifulSoup

def fetch_jobs(keyword, location, pages=3):
    all_jobs = []
    keyword_enc = "+".join(keyword.split())
    location_enc = "+".join(location.split())
    
    for page in range(pages):
        start = page * 10
        url = f"https://www.indeed.com/jobs?q={keyword_enc}&l={location_enc}&start={start}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_cards = soup.find_all("div", class_="job_seen_beacon")
        
        for job_card in job_cards:
            title_tag = job_card.find("h2", class_="jobTitle")
            title = title_tag.get_text(strip=True) if title_tag else ""
            link = "https://www.indeed.com" + title_tag.find("a")["href"] if title_tag else ""
            company_tag = job_card.find("span", class_="companyName")
            company = company_tag.get_text(strip=True) if company_tag else ""
            location_tag = job_card.find("div", class_="companyLocation")
            location = location_tag.get_text(strip=True) if location_tag else ""
            skills = []  # Indeed typically does not list skills explicitly
            
            all_jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link,
                "skills": ", ".join(skills),
                "source": "Indeed"
            })
    
    return all_jobs
