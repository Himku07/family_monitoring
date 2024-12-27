# Install required libraries
!pip install streamlit

# Save the script to a Python file
code = """
import streamlit as st
import pandas as pd
import datetime

# Title and Description
st.title("Child Development and Activity Tracker")
st.write("Monitor and promote a child's school progress, extracurricular activities, and developmental milestones.")

# Sidebar Navigation
menu = ["Home", "Track Progress", "Add Activity", "Milestone Tracker", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)

# Sample Data Storage
if "data" not in st.session_state:
    st.session_state["data"] = []

if "milestones" not in st.session_state:
    st.session_state["milestones"] = []

# Home Section
if choice == "Home":
    st.subheader("Welcome!")
    st.write("""
        Use this dashboard to:
        - Track academic progress
        - Monitor extracurricular activities
        - Set and achieve developmental milestones
    """)

# Add Activity Section
elif choice == "Add Activity":
    st.subheader("Add an Activity or Progress Update")
    
    # Input fields
    activity_name = st.text_input("Activity Name")
    category = st.selectbox("Category", ["Academic", "Extracurricular", "Developmental"])
    progress = st.slider("Progress (%)", 0, 100, 0)
    date = st.date_input("Date", datetime.date.today())
    notes = st.text_area("Additional Notes")
    
    # Save data
    if st.button("Save"):
        st.session_state["data"].append({
            "Activity": activity_name,
            "Category": category,
            "Progress": progress,
            "Date": date,
            "Notes": notes
        })
        st.success("Activity added successfully!")

# Track Progress Section
elif choice == "Track Progress":
    st.subheader("Track Progress")
    if st.session_state["data"]:
        df = pd.DataFrame(st.session_state["data"])
        st.dataframe(df)
    else:
        st.warning("No activities recorded yet.")

# Milestone Tracker Section
elif choice == "Milestone Tracker":
    st.subheader("Set or Track Milestones")
    milestone_name = st.text_input("Milestone Name")
    milestone_date = st.date_input("Target Date", datetime.date.today())
    
    if st.button("Add Milestone"):
        st.session_state["milestones"].append({
            "Milestone": milestone_name,
            "Target Date": milestone_date
        })
        st.success("Milestone added successfully!")
    
    if st.session_state["milestones"]:
        st.write("Milestones:")
        st.table(st.session_state["milestones"])
    else:
        st.warning("No milestones set yet.")

# Analytics Section
elif choice == "Analytics":
    st.subheader("Analytics")
    if st.session_state["data"]:
        df = pd.DataFrame(st.session_state["data"])
        
        # Progress by category
        progress_by_category = df.groupby("Category")["Progress"].mean()
        st.bar_chart(progress_by_category)
    else:
        st.warning("No data available for analytics.")
"""

with open("child_tracker.py", "w") as f:
    f.write(code)

# Streamlit Launch Instructions
print("""
Your Python script has been saved as 'child_tracker.py'.

To run this Streamlit app:
1. Open a terminal or local environment with Streamlit installed.
2. Run the command: streamlit run child_tracker.py.
3. Access the app in your browser using the displayed local URL.
""")
