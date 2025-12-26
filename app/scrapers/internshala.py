import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_jobs(keyword, pages=3):
    jobs = []
    keyword_words = keyword.lower().split()

    for page in range(1, pages + 1):
        url = f"https://internshala.com/internships/page-{page}/"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.find_all("div", class_="individual_internship")

        for card in cards:
            title_tag = card.find("h3", class_="job-internship-name")
            title = title_tag.get_text(strip=True) if title_tag else ""

            if not any(word in title.lower() for word in keyword_words):
                continue

            company = card.find("p", class_="company-name")
            loc = card.find("a", class_="location_link")
            link = title_tag.find("a")["href"]

            jobs.append({
                "title": title,
                "company": company.get_text(strip=True) if company else "",
                "location": loc.get_text(strip=True) if loc else "",
                "skills": "",
                "link": "https://internshala.com" + link,
                "source": "Internshala"
            })

    return jobs
