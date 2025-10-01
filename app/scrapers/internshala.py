import requests
from bs4 import BeautifulSoup
import urllib.parse

def fetch_jobs(keyword, location, pages=3):
    all_jobs = []
    keyword_enc = urllib.parse.quote(keyword)
    location_enc = urllib.parse.quote(location)
    
    for page in range(1, pages + 1):
        url = f"https://internshala.com/internships/{keyword_enc}-jobs-in-{location_enc}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_cards = soup.find_all("div", class_="individual_internship")
        
        for job_card in job_cards:
            title_tag = job_card.find("h3", class_="job-internship-name")
            title = title_tag.get_text(strip=True) if title_tag else ""
            link = title_tag.find("a")["href"] if title_tag else ""
            company_tag = job_card.find("p", class_="company-name")
            company = company_tag.get_text(strip=True) if company_tag else ""
            location_tag = job_card.find("a", class_="location_link")
            location = location_tag.get_text(strip=True) if location_tag else ""
            skills = [skill.get_text(strip=True) for skill in job_card.find_all("div", class_="job_skill")]
            
            all_jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link,
                "skills": ", ".join(skills),
                "source": "Internshala"
            })
    
    return all_jobs
