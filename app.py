# workforce-ai-demo
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="AI Workforce Portal", layout="wide")

# Load Icons (optional - can skip if deploying without local assets)
icon_url = "https://img.icons8.com/ios-filled/50/000000/briefcase.png"

# Sample Consultant Data
consultant_data = {
    "Name": ["Snigdha Singh", "Aditya Gopalakrishnan", "Chirag Batra", "Gautham Savio"],
    "Skills": [
        "Strategy, Program Mgmt, Basic Python",
        "Delivery Mgmt, Financial Modelling, SQL",
        "Research, Market Sizing, Power BI",
        "Client Comms, Project Mgmt, Excel"
    ],
    "Current OKRs": [
        "Improve productivity on delivery tasks, Upskill in data analysis tools",
        "Build financial projection models, Learn automation with Python",
        "Speed up research turnaround, Learn basic data scraping",
        "Enhance stakeholder communication, Master Excel dashboards"
    ],
    "Suggested Projects": [
        "Productivity tracker for internal teams, Market entry strategy for healthcare",
        "Industry benchmarking analysis, Internal finance automation",
        "Competitor deep-dive in mobility, Investor landscape mapping",
        "Internal insights dashboard, Regulatory trends report"
    ],
    "L&D Plan": [
        "Intro to Python for Consulting, Dashboarding in Excel",
        "Finance Automation with Python, Time-to-Insight Training",
        "Power BI Advanced, Fast Research Techniques",
        "Storytelling with Data, Excel Tips for Client Delivery"
    ]
}
df = pd.DataFrame(consultant_data)

# Sidebar
st.sidebar.markdown("## 🔎 Navigation")
section = st.sidebar.radio("Choose a section", ["🏢 Manager View", "👤 Consultant View", "💬 Chat Assistant (Mock)"])

st.markdown(
    """
    <style>
    .big-font {
        font-size: 24px;
        font-weight: bold;
    }
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# MANAGER VIEW
if section == "🏢 Manager View":
    st.markdown("<div class='big-font'>📊 Manager Dashboard</div>", unsafe_allow_html=True)
    st.markdown("#### Overview of Consultant Pipeline and Opportunities")
    st.dataframe(df)

    st.markdown("### 🔍 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Consultants Tracked", len(df))
    with col2:
        st.success("High priority: Upskilling + Delivery Optimization")

# CONSULTANT VIEW
elif section == "👤 Consultant View":
    st.markdown("<div class='big-font'>🙋 Consultant Portal</div>", unsafe_allow_html=True)
    selected_name = st.selectbox("Select your name", df["Name"])
    data = df[df["Name"] == selected_name].iloc[0]

    st.markdown("#### 🔍 Profile Details")
    st.markdown(f"<div class='card'><b>Skills:</b><br>{data['Skills']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'><b>Current OKRs:</b><br>{data['Current OKRs']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'><b>Suggested Projects:</b><br>{data['Suggested Projects']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'><b>L&D Plan:</b><br>{data['L&D Plan']}</div>", unsafe_allow_html=True)

# CHAT VIEW
elif section == "💬 Chat Assistant (Mock)":
    st.markdown("<div class='big-font'>💬 AI Assistant (Demo)</div>", unsafe_allow_html=True)
    st.markdown("Ask questions like:")
    st.markdown("- _Who is fit for a market sizing task?_\n- _Recommend L&D for Gautham_")

    query = st.text_input("Ask something:")
    if query:
        st.markdown("#### 🤖 Response")
        if "market sizing" in query.lower():
            st.success("Chirag Batra or Snigdha Singh would be strong choices.")
        elif "Gautham" in query and "L&D" in query:
            st.success("Gautham’s plan: Storytelling with Data and Excel Tips for Client Delivery.")
        else:
            st.info("This is a mock NLP. Real AI assistant coming soon.")

