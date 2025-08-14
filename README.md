Root Cause Analysis (RCA) Dashboard
🚀 A Streamlit-powered dashboard for analyzing job failures, delays, and incident trends.

<img width="1900" height="794" alt="image" src="https://github.com/user-attachments/assets/a6932d7d-17a2-4b88-8b22-5adcf92777fc" />

📌 Overview
This interactive dashboard provides insights into:
✔ Job failure analysis (Top 3 error-prone jobs)
✔ Delay tracking (Frequency and duration)
✔ Environment-specific trends (Filter by Environment)

⚡ Features
Dynamic filtering by Environment

Key metrics: Total incidents, delays, and average delay time

Visualizations:

Top 3 jobs with most errors (bar chart)
Delay distribution (pie chart + histogram)
Responsive design (works on desktop/tablet)

🚀 Quick Start
Prerequisites
pip install streamlit pandas matplotlib seaborn openpyxl

Run Locally
Clone the repo:
git clone https://github.com/GarciaCeron/bw.git

Place your RCA.csv file in the root directory.

Launch the app:
streamlit run dashboard_rca.py

📂 Data Format
Excel/JSON Structure
Column	Description	Example
Physical Date	Timestamp of the incident	2025-01-05 00:00:00
Environment	Deployment environment	Env1, Env5
Job	Job name that failed	CORE_PAY_ORFSP
INC	Incident ID	INC218800
Reason	Root cause description	L0015 failed
Delay Y/N	Whether the incident caused a delay	Y/N
Time Delayed	Duration of delay (if any)	1 hr, No Delay

🛠 Customization
Add more filters: Modify the sidebar to filter by date range or job type.

New charts: Extend the visualizations section with Plotly for interactivity.

Deploy: Share via Streamlit Cloud or Docker.

📜 License
MIT © Gerardo Valentín García Ceron

💡 Pro Tip: Add a requirements.txt for easy dependency management!

streamlit
pandas
openpyxl
matplotlib
seaborn




