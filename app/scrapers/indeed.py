import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch_jobs(keyword, location="", pages=2):
    jobs_data = []

    keyword = keyword.replace(" ", "+")
    location = location.replace(" ", "+")

    for page in range(pages):
        start = page * 10
        url = f"https://in.indeed.com/jobs?q={keyword}&l={location}&start={start}"

        response = requests.get(url, headers=HEADERS, timeout=10)
        html = response.text.lower()

        # 🛑 Bot / captcha detection
        if "captcha" in html or "verify you are human" in html:
            print("⚠️ Indeed blocked request (captcha)")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("a", class_="tapItem")

        for job in jobs:
            title = job.select_one("h2 span")
            company = job.select_one(".companyName")
            loc = job.select_one(".companyLocation")
            posted = job.select_one(".date")

            link = job.get("href")
            if link and link.startswith("/"):
                link = "https://in.indeed.com" + link

            jobs_data.append({
                "title": title.get_text(strip=True) if title else "",
                "company": company.get_text(strip=True) if company else "",
                "location": loc.get_text(strip=True) if loc else "",
                "posted": posted.get_text(strip=True) if posted else "",
                "link": link,
                "source": "Indeed"
            })

    return jobs_data
