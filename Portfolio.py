import streamlit as st
import pandas as pd
import random
import time
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="My Portfolio", page_icon="🎨", layout="wide")
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .animated {
        animation: fadeIn 1.5s;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #0078ff;
        color: white;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "page" not in st.session_state:
    st.session_state["page"] = "Home"
st.sidebar.title("Navigation")
page_options = ["Home", "Expertise", "Skills", "Language", "Achievements", "Projects", "Experience", "Contact"]
page = st.sidebar.selectbox("Take a look at my", page_options, index=page_options.index(st.session_state["page"]))

if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("**Name:** Hariprasath A")
    st.image("WhatsApp Image 2025-01-26 at 1.45.22 PM.jpeg",width=500)
    st.write("As a forward looking individual i posses a strong enthusiasm about teamwork and leadership. I'm eager to eager to explore the advanced fileds of machine learning, cyber security. I look forward to utilize my skills to explore the boundaries of the position I get. I assure you that I'll put my fullest effort to my work and ")
    if st.button("Explore My Work", key="explore"):
        st.session_state["page"] = "Projects"
        st.rerun()

elif page == "Projects":
    st.title("My Projects")
    st.write("Explore my work below.")
    projects = pd.DataFrame({
        "Name": ["AI-based water-footprint calculator", "Automatic file backup app", "Power prediction website", "Portfolio Website"],
        "Year": [2023, 2023, 2024, 2025]
    })
    year_filter = st.slider("Filter by Year", min_value=2022, max_value=2025, value=(2022, 2025))
    filtered_projects = projects[(projects["Year"] >= year_filter[0]) & (projects["Year"] <= year_filter[1])]
    st.dataframe(filtered_projects, use_container_width=True)
    
elif page == "Experience":
    st.title("My Experience")
    st.write("A brief overview of my work and accomplishments.")
    
    experiences = [
        "Quiz Master for multiple intercollegiate fests since 2022",
        "Internship at EMglitz Technologies"
    ]
    
    for exp in experiences:
        with st.container():
            st.markdown(f"✔ {exp}")
            time.sleep(0.2)  

elif page == "Contact":
    st.title("Contact Me")
    
    st.write("Feel free to reach out to me through the details below:")
    st.markdown("**Email:** hariprasathasaithambi@gmail.com")
    st.markdown("**Phone:** +91-9345930934")
    st.markdown("**LinkedIn:** [linkedin.com/in/imayavan](https://linkedin.com/in/imayavan)")
    st.markdown("**GitHub:** [github.com/imayavan](https://github.com/imayavan)")
st.markdown("---")
st.markdown("© 2025 My Portfolio. All rights reserved.")

