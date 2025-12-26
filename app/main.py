import streamlit as st
import pandas as pd
from app.services.aggregator import get_all_jobs

st.set_page_config(page_title="Job Integrator", layout="wide")

st.title("💼 Job Integrator System")
st.subheader("Internshala Jobs")

keyword = st.text_input("Job Keyword", "Data Analyst")
pages = st.slider("Pages to scrape", 1, 5, 2)

if st.button("🔍 Search Jobs"):
    with st.spinner("Fetching jobs..."):
        jobs = get_all_jobs(keyword, location="", pages=pages)

    if not jobs:
        st.warning("No jobs found")
    else:
        st.success(f"Found {len(jobs)} jobs")

        df = pd.DataFrame(jobs)

        # show jobs
        st.dataframe(df)

        # 🔥 CREATE EXCEL IN MEMORY
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Jobs")

        output.seek(0)

        # ⬇️ DOWNLOAD BUTTON
        st.download_button(
            label="⬇️ Download Excel",
            data=output,
            file_name="internshala_jobs.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
