import streamlit as st
import pandas as pd
import random
import time
import base64
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
st.set_page_config(page_title="My Portfolio", page_icon="🎨")


if "page" not in st.session_state:
    st.session_state["page"] = "Profile"
from streamlit_option_menu import option_menu

with st.sidebar:
    page = option_menu(
        "Navigation",
        ["Profile", "Education", "Expertise", "Skills", "Achievements", 
         "Projects", "Certifications", "Co-curricular", "Contact"],
        icons=["person", "book", "lightbulb", "star", "award", "briefcase", "bookmark-check", "activity", "phone"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#6c6c6c", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#d3f2f3"},
            "nav-link-selected": {"background-color": "#1abc9c", "color": "white"},
        }
    )

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
    .box {
        padding: 15px;
        margin: 10px 0px;
        background-color: #f0f0f5;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        font-weight: bold;
        font-size: 18px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


bg_images = {
    "Profile": "/home/imayavan/Desktop/Portfolio/Portfolio/images/5651981.jpg",
}

default_bg = "/home/imayavan/Desktop/Portfolio/Portfolio/images/5651992.png"


def get_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None 

selected_bg = bg_images.get(page, default_bg)
encoded_bg = get_base64(selected_bg)

if encoded_bg:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/png;base64,{encoded_bg}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"⚠ Background image not found: {selected_bg}")

    
if page == "Profile":
    st.title("Welcome to My Portfolio")
    st.write("## **Name:** Hariprasath A")
    st.image("/home/imayavan/Desktop/Portfolio/Portfolio/images/profile.jpeg",width=500)
    st.write("As a forward looking individual i posses a strong enthusiasm about teamwork and leadership. I'm eager to eager to explore the advanced fileds of machine learning, cyber security. I look forward to utilize my skills to explore the boundaries of the position I get. I assure you that I'll put myfullest effort to honor my position and work hard for it.")
    st.write("I am a OS explorer and a kernel engineer and a hard working person on Operating Systems. I can speak upto four languages and has distinguished the stages of the four languages below")
    
    st.markdown("# Click on the languages listed below")
    if st.button("English", key="english"):
        data= [
            ["✔", "✔", "✔", "✔"]
        ]
        df = pd.DataFrame(data,columns=["Read", "Write", "Understand", "Speak"])
        st.table(df)
        
    if st.button("Tamil", key="tamil"):
        data= [
            ["✔", "✔", "✔", "✔"]
        ]
        df = pd.DataFrame(data,columns=["Read", "Write", "Understand", "Speak"])
        st.table(df)
        
    if st.button("Hindi", key="hindi"):
        data= [
            ["✔", "✔", "✔", "✔"]
        ]
        df = pd.DataFrame(data,columns=["Read", "Write", "Understand", "Speak"])
        st.table(df)
        
    if st.button("Telugu", key="telugu"):
        data= [
            [" ", " ", "✔", "✔"]
        ]
        df = pd.DataFrame(data,columns=["Read", "Write", "Understand", "Speak"])
        st.table(df)
    
    st.markdown("# Click the below button to view my projects") 
    if st.button("Explore My Work", key="explore"):
        st.session_state["page"] = "Projects"
        st.rerun()

elif page == "Education":
    st.markdown("""
        <style>
            .education-container {
                font-family: Arial, sans-serif;
            }
            .education-header {
                font-size: 24px;
                font-weight: bold;
                border-bottom: 3px solid #333;
                display: inline-block;
                margin-bottom: 10px;
            }
            .timeline {
                position: relative;
                padding-left: 20px;
                margin-top: 10px;
            }
            .timeline::before {
                content: '';
                position: absolute;
                left: 5px;
                top: 0;
                width: 2px;
                height: 100%;
                background: #555;
            }
            .timeline-item {
                position: relative;
                margin-bottom: 20px;
                padding-left: 20px;
            }
            .timeline-item::before {
                content: '•';
                position: absolute;
                left: -5px;
                top: 5px;
                font-size: 18px;
                color: #555;
            }
            .education-title {
                font-size: 18px;
                font-weight: bold;
            }
            .education-subtitle {
                font-size: 14px;
                color: #666;
            }
        </style>
        
        <div class="education-container">
            <div class="education-header">EDUCATION</div>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="education-title">SSLC</div>
                    <div class="education-subtitle">Jayam Vidhyalaya Matric Higher Secondary School (2019)</div>
                </div>
                <div class="timeline-item">
                    <div class="education-title">HSC</div>
                    <div class="education-subtitle">Jayam Vidhyalaya Matric Higher Secondary School (2021)</div>
                </div>
                <div class="timeline-item">
                    <div class="education-title">B.E - Computer Science and Engineering</div>
                    <div class="education-subtitle">Sri Ramakrishna Engineering College (2022 - 2026)</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
        
elif page == "Expertise":
    st.title("Expertise in")
    image_paths = [
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/web developement.jpeg",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/pngwing.png",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/AdobeStock_752175894_Preview.jpeg",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/github.png",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/python.jpg",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/C logo.png",
        "/home/imayavan/Desktop/Portfolio/Portfolio/images/shell scripting.png"
    ]

    text_items = [
        "Web Development",
        "MongoDB",
        "Prompt Engineering",
        "Git & GitHub",
        "Pyhton",
        "C",
        "Shell Scripting"
    ]

    for img, text in zip(image_paths, text_items):
        col1, col2 = st.columns([1, 3],gap="large")
        with col1:
            st.image(img, width=300)
        with col2:
            st.markdown(f"<p style='font-size:35px; font-weight:normal; line-height:7.0; padding-left:200px'>{text}</p>", unsafe_allow_html=True)

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
    
elif page == "Education":
    st.title("My Education")
    st.write("A brief overview of my work and accomplishments.")
    
    Education = [
        "Quiz Master for multiple intercollegiate fests since 2022",
        "Internship at EMglitz Technologies"
    ]
    
    for edu in Education:
        with st.container():
            st.markdown(f"✔ {edu}")
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

