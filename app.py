import streamlit as st
import pandas as pd
import random
import plotly.express as px

# Core dataset
consultants_data = [
    {"Name": "Snigdha Singh", "Designation": "Project Lead I", "Expertise": "Startup Sourcing",
     "Skills": ["Consulting", "Startup Scouting", "Research"], "Projects": ["NetApp", "Panasonic", "NASSCOM Report"],
     "OKRs": "Drive delivery efficiency, mentor team, build tech knowledge",
     "L&D Plan": "Coursera: AI for Everyone, McKinsey Problem Solving",
     "Availability": "May 2025", "Current Project": "Panasonic", "Next Project": "TBD"},

    {"Name": "Aditya Gopalakrishnan", "Designation": "Project Lead I", "Expertise": "Reports, Automotive",
     "Skills": ["Consulting", "Automotive", "Report Writing"], "Projects": ["MBRDI", "NASSCOM Report", "Flexera"],
     "OKRs": "Delivery on Flexera, automotive insights, upskill in ML",
     "L&D Plan": "ML for Business Leaders, Financial Forecasting (LinkedIn)",
     "Availability": "June 2025", "Current Project": "MBRDI", "Next Project": "TBD"},

    {"Name": "Chirag Batra", "Designation": "Consultant II", "Expertise": "Japanese Clients, Emerging Tech",
     "Skills": ["Consulting", "Emerging Tech", "Client Handling"], "Projects": ["Sumitomo", "Marubeni", "Sony"],
     "OKRs": "Improve delivery metrics, learn data storytelling",
     "L&D Plan": "Emerging Tech Webinar Series, Communication for Impact",
     "Availability": "April 2025", "Current Project": "Sony", "Next Project": "Marubeni"},

    {"Name": "Gautham Savio", "Designation": "Senior Associate - Marketing", "Expertise": "Marketing Strategy",
     "Skills": ["Campaigns", "Content Strategy", "Design"], "Projects": ["Internal GTM", "Employer Branding"],
     "OKRs": "Improve internal reach, launch 2 GTM campaigns",
     "L&D Plan": "Hubspot Certification, Canva Pro Workshop",
     "Availability": "July 2025", "Current Project": "Employer Branding", "Next Project": "TBD"}
]

# Add dummy consultants
names = ["John Doe", "Jane Smith", "Priya Raj", "Aarav Mehta", "Emily Chen", "Carlos Diaz"]
designations = ["Project Lead II", "Consultant I"]
skills_list = ["Consulting", "Strategy", "Market Sizing", "Data Cleaning", "Storyboarding", "PowerPoint", "Python"]

for name in names:
    consultants_data.append({
        "Name": name,
        "Designation": random.choice(designations),
        "Expertise": random.choice(["Finance", "Retail", "Healthcare", "Edtech"]),
        "Skills": random.sample(skills_list, 3),
        "Projects": random.sample(["XYZ", "ABC", "DEF", "GHI", "JKL"], 3),
        "OKRs": "Improve output, upskill in AI, enhance communication",
        "L&D Plan": "Skillshare, GPT-4 Tutorials",
        "Availability": random.choice(["April 2025", "May 2025", "June 2025"]),
        "Current Project": random.choice(["XYZ", "ABC", "GHI"]),
        "Next Project": "TBD"
    })

df = pd.DataFrame(consultants_data)

# Streamlit config
st.set_page_config(page_title="AI-Powered Staffing | Internal Demo", layout="wide")
st.title("🧠 AI-Powered Internal Talent Dashboard")

tabs = st.tabs(["📈 Manager View", "👤 Consultant View", "🤖 Chatbot", "🧩 HR View"])

# Manager View
with tabs[0]:
    st.subheader("Overview: Consultants vs Projects")
    st.dataframe(df[["Name", "Designation", "Skills", "Current Project", "Availability", "Next Project"]])

    st.subheader("Skill Distribution")
    skill_df = df.explode("Skills")
    skill_counts = skill_df["Skills"].value_counts().reset_index()
    skill_counts.columns = ["Skill", "Count"]
    fig = px.bar(skill_counts, x="Skill", y="Count", color="Skill", title="Consultant Skill Heatmap")
    st.plotly_chart(fig, use_container_width=True)

# Consultant View
with tabs[1]:
    st.subheader("Personalized Consultant Snapshot")
    consultant_choice = st.selectbox("Choose your name", df["Name"].unique())
    selected = df[df["Name"] == consultant_choice].iloc[0]

    st.markdown(f"""
    **🪪 Designation:** {selected['Designation']}  
    **🎯 Expertise:** {selected['Expertise']}  
    **🛠️ Skills:** {', '.join(selected['Skills'])}  
    **📁 Projects:** {', '.join(selected['Projects'])}  
    **📍 Availability:** {selected['Availability']}  
    **🚧 Current Project:** {selected['Current Project']}  
    **🔜 Next Project:** {selected['Next Project']}  
    """)

    st.markdown("**🎯 OKRs**")
    st.success(selected["OKRs"])

    st.markdown("**📚 Learning Plan**")
    st.info(selected["L&D Plan"])

# Chatbot View
with tabs[2]:
    st.subheader("Ask AI about your Role")
    st.markdown("Example prompts:")
    st.markdown("- *What’s my next project?*")
    st.markdown("- *What are my current OKRs?*")
    st.markdown("- *Suggest a learning plan*")

    query = st.text_input("Ask a question")
    if query and consultant_choice:
        q = query.lower()
        response = ""
        if "next project" in q:
            response = f"Your next mapped project is **{selected['Next Project']}**."
        elif "okr" in q:
            response = f"Your current OKRs are: **{selected['OKRs']}**."
        elif "learning" in q or "training" in q:
            response = f"Recommended L&D: **{selected['L&D Plan']}**."
        elif "availability" in q:
            response = f"You're available from **{selected['Availability']}**."
        elif "skills" in q:
            response = f"Your key skills are: **{', '.join(selected['Skills'])}**."
        elif "designation" in q:
            response = f"You're currently a **{selected['Designation']}**."
        elif "project" in q:
            response = f"You're on **{selected['Current Project']}**, mapped to **{selected['Next Project']}** next."
        else:
            response = "I'm learning! Try asking about your skills, project, or OKRs."

        st.markdown(f"**💬 AI says:** {response}")

# HR View
with tabs[3]:
    st.subheader("Hiring & Upskilling Tracker")
    upcoming_projects = {
        "Digital Health GTM": ["Healthcare", "Data Cleaning", "PowerPoint"],
        "Retail Trend Analysis": ["Retail", "Market Sizing", "Consulting"],
        "AI Startup Scouting": ["Startup Sourcing", "Storyboarding", "Python"],
        "Japanese CX Strategy": ["Japanese Clients", "Emerging Tech", "Report Writing"]
    }

    proj = st.selectbox("Select upcoming project", list(upcoming_projects.keys()))
    needed = upcoming_projects[proj]

    st.markdown(f"**Required Skills:** {', '.join(needed)}")
    match = df[df["Skills"].apply(lambda x: any(skill in x for skill in needed))]

    st.markdown("**🧑‍💼 Matching Consultants Available:**")
    st.dataframe(match[["Name", "Designation", "Skills", "Availability", "Current Project", "Next Project"]])

# --- Footer ---
st.markdown("---")
st.markdown("Crafted with ❤️ by PersonaX")


