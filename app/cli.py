import argparse
from app.services import aggregator
from app.utils.excel_export import save_to_excel

parser = argparse.ArgumentParser(description="Job Integrator CLI")
parser.add_argument("--keyword", required=True, help="Job keyword")
parser.add_argument("--location", default="", help="Job location")

args = parser.parse_args()
jobs = aggregator.get_all_jobs(args.keyword, args.location)

if jobs:
    save_to_excel(jobs)
    print(f"{len(jobs)} jobs saved to data/jobs.xlsx")
else:
    print("No jobs found!")
