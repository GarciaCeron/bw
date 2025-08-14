import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Error Analysis Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    # Read Excel file (in production you would use a file uploader)
    # df = pd.read_excel("RCA.xlsx", sheet_name="Sheet1")
    df = pd.read_csv("RCA.csv")
    
    # Basic data cleaning
    df['Time Delayed'] = df['Time Delayed'].replace({'No Delay': '0 hr', '1:20 hr': '1.33 hr'})
    df['Hours Delayed'] = df['Time Delayed'].str.extract('(\d+\.?\d*)').astype(float)
    
    return df

df = load_data()

# Sidebar - Filters
st.sidebar.header("Filters")
environments = df['Environment'].unique()
selected_env = st.sidebar.radio("Select Environment:", environments)

# Filter data
filtered_df = df[df['Environment'] == selected_env]

# Main layout
col1, col2 = st.columns([1, 3])

# Column 1: Summary metrics
with col1:
    st.subheader(f"Summary for {selected_env}")
    
    total_incidents = len(filtered_df)
    delayed_incidents = len(filtered_df[filtered_df['Delay Y/N'] == 'Y'])
    
    st.metric("Total Incidents", total_incidents)
    st.metric("Delayed Incidents", delayed_incidents)
    
    avg_delay = filtered_df['Hours Delayed'].mean()
    st.metric("Average Delay (hrs)", f"{avg_delay:.2f}")

# Column 2: Data and visualizations
with col2:
    st.subheader("Detailed Data")
    st.dataframe(filtered_df, height=300, use_container_width=True)
    
    # Chart 1: Top 3 Jobs with most errors
    st.subheader("Top 3 Jobs with Most Errors")
    job_counts = filtered_df['Job'].value_counts().head(3)
    
    fig1, ax1 = plt.subplots()
    sns.barplot(x=job_counts.values, y=job_counts.index, palette="Blues_d", ax=ax1)
    ax1.set_xlabel('Number of Errors')
    ax1.set_ylabel('Job')
    st.pyplot(fig1)
    
    # Chart 2: Delay distribution
    st.subheader("Delay Distribution")
    
    delay_counts = filtered_df['Delay Y/N'].value_counts()
    time_delayed = filtered_df[filtered_df['Delay Y/N'] == 'Y']['Hours Delayed']
    
    fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Pie chart of delays yes/no
    ax2.pie(delay_counts, labels=delay_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
    ax2.set_title('Delay Proportion')
    
    # Delay time histogram
    if not time_delayed.empty:
        sns.histplot(time_delayed, bins=5, kde=True, ax=ax3, color='skyblue')
        ax3.set_xlabel('Delay Hours')
        ax3.set_ylabel('Frequency')
        ax3.set_title('Delay Time Distribution')
    else:
        ax3.text(0.5, 0.5, 'No delay data available', ha='center', va='center')
    
    st.pyplot(fig2)

# Additional notes
st.sidebar.markdown("---")
st.sidebar.info("""
**Notes:**
- Data shows recorded incidents with their root cause analysis.
- 'Time Delayed' has been converted to numeric hours for analysis.
""")