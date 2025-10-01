import streamlit as st
from services import aggregator
from utils.excel_export import save_to_excel

st.title("Job Integrator System - Internshala + Indeed")

keyword = st.text_input("Enter Job Keyword", "Data Analyst")
location = st.text_input("Enter Location", "Bangalore")

if st.button("Search Jobs"):
    with st.spinner("Fetching jobs..."):
        jobs = aggregator.get_all_jobs(keyword, location)
    
    st.success(f"Found {len(jobs)} jobs!")
    
    for job in jobs:
        st.markdown(f"**{job['title']}** - {job['company']} ({job['source']})")
        st.markdown(f"Location: {job['location']}")
        st.markdown(f"Skills: {job['skills']}")
        st.markdown(f"[Link]({job['link']})")
        st.markdown("---")
    
    if st.button("Export to Excel"):
        save_to_excel(jobs)
        st.success("Jobs exported to jobs.xlsx")
