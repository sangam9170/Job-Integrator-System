import pandas as pd
import os

def save_to_excel(jobs):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(jobs)
    df.to_excel("data/jobs.xlsx", index=False)
