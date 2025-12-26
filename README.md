# Job Integrator System 🚀

A web-based job aggregation application built using **Python** and **Streamlit** that scrapes internship listings from **Internshala and Indeed**, displays them in an interactive UI, and allows users to **download results as an Excel file**.  
The app is fully deployed on **Streamlit Community Cloud**.

---

## 🔗 Live Demo

👉 https://job-integrator-system-bhiappmfhfbwhwdydhfrypc.streamlit.app/

---

## 📌 Features

- 🔍 Search internships by keyword (e.g., Data Analyst, Python, Web Development)
- 📄 Scrapes real-time internship data 
- 📊 Displays results in a clean, interactive table
- ⬇️ Download all job listings as an **Excel (.xlsx)** file
- ☁️ Deployed and accessible online via Streamlit Cloud
- 🧩 Modular and clean project structure

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – Web UI
- **Requests** – HTTP requests
- **BeautifulSoup** – Web scraping
- **Pandas** – Data processing
- **OpenPyXL** – Excel export
- **Git & GitHub** – Version control
- **Streamlit Community Cloud** – Deployment

---
```
## 📂 Project Structure

Job-Integrator-System/
│
├── app/
│ ├── main.py 
│ ├── cli.py
│ │
│ ├── scrapers/
│ │ ├── internshala.py
│ │ └── indeed.py 
│ │
│ ├── services/
│ │ └── aggregator.py 
│ │
│ └── utils/
│ └── excel_export.py 
│
├── data/
├── requirements.txt 
├── .gitignore
└── README.md


---
```

## ⚙️ How It Works

1. User enters a **job keyword** in the Streamlit interface  
2. The application scrapes internship 
3. Results are processed using Pandas and shown in the UI  
4. Users can download the results as an Excel file  
5. The app runs smoothly both **locally** and **on the cloud**

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sangam9170/Job-Integrator-System.git
cd Job-Integrator-System
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Streamlit app
bash
Copy code
python -m streamlit run app/main.py
Open browser at:

arduino
Copy code
http://localhost:8501
☁️ Deployment
The application is deployed using Streamlit Community Cloud with GitHub integration.

Deployment highlights:

Cloud-compatible imports

Excel export using openpyxl

Automatic redeploy on updates to the main branch

🚀 Future Enhancements
Resume-based internship matching

Filters (location, duration, stipend)

Email alerts for new internships

👨‍💻 Author
Sangam Singh
GitHub: https://github.com/sangam9170
