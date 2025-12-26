import argparse
from app.services.aggregator import get_all_jobs
from app.utils.excel_export import save_to_excel

def main():
    parser = argparse.ArgumentParser(description="Job Integrator CLI")
    parser.add_argument("--keyword", required=True, help="Job keyword")
    parser.add_argument("--location", default="", help="Job location (Indeed)")
    parser.add_argument("--pages", type=int, default=3, help="Pages to scrape")

    args = parser.parse_args()

    print("🔍 Fetching jobs...")
    jobs = get_all_jobs(args.keyword, args.location, args.pages)

    if jobs:
        save_to_excel(jobs)
        print(f"✅ {len(jobs)} jobs saved to data/jobs.xlsx")
    else:
        print("❌ No jobs found")

if __name__ == "__main__":
    main()
