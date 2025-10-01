import pandas as pd

def save_to_excel(jobs, filename="jobs.xlsx"):
    df = pd.DataFrame(jobs)
    df.to_excel(filename, index=False)
    print(f"Jobs exported to {filename}")
