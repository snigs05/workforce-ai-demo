import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

st.set_page_config(page_title="Consultant Intelligence Platform", layout="wide")

# Sample data
data = [
    ["Snigdha Singh", "Startup Sourcing", "NetApp, Panasonic, NASSCOM Report", "Management Consulting", "Delivery OKRs", "Market Sizing, Financial Projections", "Tech Certification", "5 months", "None", "Available"],
    ["Aditya Gopalakrishnan", "Reports, Automotive", "MBRDI, NASSCOM Report, Flexera", "Management Consulting, Basic Tech", "Upskilling in Tech", "Automotive Sector Analysis", "Excel Automation", "2 months", "Next project mapped", "Not Available"],
    ["Chirag Batra", "Japanese Clients, Emerging Tech", "Sumitomo, Marubeni, Sony", "Tech + Client Mgt", "Productivity OKRs", "Emerging Tech Research", "Data Viz Workshops", "4 months", "None", "Available"],
    ["Gautham Savio", "Data Analysis", "Internal Tools, BD Decks", "Tech, Reports", "Delivery OKRs", "Internal Automation, Dashboards", "Python Basics", "1 month", "Next project mapped", "Not Available"],
    ["John Doe", "Market Analysis", "Confidential", "Basic Tech", "Upskilling OKRs", "Market Sizing", "SQL Bootcamp", "2 months", "None", "Available"],
    ["Jane Smith", "Delivery Excellence", "Process Revamp", "Mgmt Consulting", "Productivity OKRs", "Workflow Design", "AI Overview", "3 months", "Next project mapped", "Not Available"]
]

columns = ["Name", "Expertise", "Projects", "Skills", "OKRs", "Suggested Projects", "L&D Plan", "Current Project Duration", "Next Project", "Availability"]
df = pd.DataFrame(data, columns=columns)

# --- Header ---
st.title("🚀 Consultant Intelligence Dashboard")
st.markdown("A smart, AI-ready platform to match the **right talent** with the **right projects** at the **right time**.")
st.markdown("---")

# --- Filters ---
st.sidebar.header("🔍 Filter Consultants")
availability = st.sidebar.selectbox("Availability", options=["All"] + df["Availability"].unique().tolist())
skill = st.sidebar.multiselect("Skills", options=sorted(df["Skills"].unique().tolist()))

filtered_df = df.copy()
if availability != "All":
    filtered_df = filtered_df[filtered_df["Availability"] == availability]
if skill:
    filtered_df = filtered_df[filtered_df["Skills"].isin(skill)]

# --- Consultant Table ---
st.subheader("👥 Consultant Profiles")
st.dataframe(filtered_df, use_container_width=True)

# --- Visualisation 1: Availability Status ---
st.subheader("📊 Availability Overview")
avail_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Availability", title="Status"),
        y=alt.Y("count()", title="Consultant Count"),
        color="Availability",
        tooltip=["Availability", "count()"]
    )
    .properties(width=300, height=300)
)
st.altair_chart(avail_chart, use_container_width=True)

# --- Visualisation 2: Consultant Count by Expertise ---
st.subheader("💼 Consultant Count by Expertise")
expertise_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Expertise", sort="-y", title="Area of Expertise"),
        y=alt.Y("count()", title="Consultant Count"),
        color="Expertise",
        tooltip=["Expertise", "count()"]
    )
    .properties(width=600, height=400)
)
st.altair_chart(expertise_chart, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("Crafted with ❤️ by PersonaX")


