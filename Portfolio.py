import streamlit as st
import pandas as pd
import base64
import time
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
import json
import time
import emoji

st.set_page_config(page_title="Hariprasath A | Portfolio", page_icon="🎨", layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = "Profile"

with st.sidebar:
    st.markdown("<h2 style='color:#e6e6e6;'>Navigation</h2>", unsafe_allow_html=True)
    page = option_menu(
        menu_title=None,
        options=["Profile", "Education", "Expertise", "Skills", "Achievements", "Projects", "Certifications", "Co-curricular", "Contact"],
        icons=["person", "book", "lightbulb", "star", "award", "briefcase", "bookmark-check", "activity", "phone"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#6c6c6c", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color":"#1b1818", "--hover-color": "#d3f2f3"},
            "nav-link-selected": {"background-color": "#1abc9c", "color": "blue"},
        }
    )

st.markdown("""
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .fadein {
        animation: fadeIn 1.5s;
    }
    .stButton>button {
        background-color: #0078ff;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .card {
        padding: 20px;
        margin: 15px 0;
        background-color: #f1f2f6;
        border-radius: 12px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
    }
    .box {
        padding: 20px;
        margin: 15px 0;
        background-color: #005ce6;
        border-radius: 12px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

bg_images = {
    "Profile": "/home/imayavan/Downloads/Portfolio/images/5651981.jpg"
}
default_bg = "/home/imayavan/Downloads/Portfolio/images/5651992.png"

def get_base64(image_path):
    try:
        with open(image_path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except FileNotFoundError:
        return None

selected_bg = bg_images.get(page, default_bg)
encoded_bg = get_base64(selected_bg)
if encoded_bg:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_bg}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# === PAGES ===

if page == "Profile":
    st.title("👋 Welcome to My Portfolio")
    st.image("/home/imayavan/Downloads/Portfolio/images/profile.jpeg", width=400)
    st.write("## **Name:** Hariprasath A")
    st.markdown("""
    <div style='font-size:20px; line-height:1.6; text-align: justify;'>
    As a forward looking-individual I posses a strong enthusiasm about leadership and team work. I’m eager to explore the advanced fields of
    Networking, Machine learning and Cyber security. I look forward to utilize my skills to explore the boundaries of the position i get. I’m eager to      explore the advanced fields of Networking, Machine Learning and Cyber Security. I'm a passionate OS explorer, and a budding kernel engineer with multilingual capabilities. I assure that I’ll put my full effort to my work.
</div>
""", unsafe_allow_html=True)
    
    st.markdown("### 🔊 Click on the languages below to see proficiency:")
    languages = {
        "English": ["✔", "✔", "✔", "✔"],
        "Tamil": ["✔", "✔", "✔", "✔"],
        "Hindi": ["✔", "✔", "✔", "✔"],
        "Telugu": [" ", " ", "✔", "✔"],
    }

    for lang, values in languages.items():
        if st.button(lang):
            df = pd.DataFrame([values], columns=["Read", "Write", "Understand", "Speak"])
            st.table(df)

    if st.button("🎯 Explore My Work"):
            st.markdown("# Click the below button to view my projects")
            st.session_state["page"] = "Projects"
            st.rerun()
elif page == "Education":
    st.title("🎓 My Education Journey")
    st.markdown("""
    <div class='box'>
        <h4>🧑‍🎓 SSLC</h4>
        <p>Jayam Vidhyalaya Matric Hr. Sec. School (2019)</p>
    </div>
    <div class='box'>
        <h4>🧑‍🎓 HSC</h4>
        <p>Jayam Vidhyalaya Matric Hr. Sec. School (2021)</p>
    </div>
    <div class='box'>
        <h4>💻 B.E - CSE</h4>
        <p>Sri Ramakrishna Engineering College (2022 - 2026)</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Expertise":
    st.title("🧠 Areas of Expertise")
    skills = [
        ("/home/imayavan/Downloads/Portfolio/images/web developement.jpeg", "Web Development"),
        ("/home/imayavan/Downloads/Portfolio/images/pngwing.png", "MongoDB"),
        ("/home/imayavan/Downloads/Portfolio/images/AdobeStock_752175894_Preview.jpeg", "Prompt Engineering"),
        ("/home/imayavan/Downloads/Portfolio/images/github.png", "Git & GitHub"),
        ("/home/imayavan/Downloads/Portfolio/images/python.jpg", "Python"),
        ("/home/imayavan/Downloads/Portfolio/images/C logo.png", "C Programming"),
        ("/home/imayavan/Downloads/Portfolio/images/shell scripting.png", "Shell Scripting")
    ]
    for img, text in skills:
        col1, col2 = st.columns([1, 3], gap="large")
        with col1:
            st.image(img, width=300)
        with col2:
            st.markdown(
                f"<p style='font-size:35px; font-weight:normal; line-height:7.0; padding-left:200px'>{text}</p>",
                unsafe_allow_html=True)

elif page == "Skills":
    st.title("🛠️ SKILLS")
elif page == "Projects":
    st.title("🚀 My Projects")

    year_filter = st.slider("Filter by Year", min_value=2022, max_value=2025, value=(2022, 2025))

    projects = [
        {
            "title": "Water Footprint Calculator",
            "desc": "AI-based solution to track daily water use.",
            "year": 2023,
            "img": "https://img.icons8.com/color/96/water.png",
            "link": "https://github.com/yourprofile/water-footprint"
        },
        {
            "title": "Automatic File Backup",
            "desc": "Python-MongoDB based backup system.",
            "year": 2024,
            "img": "https://img.icons8.com/color/96/database.png",
            "link": "https://github.com/yourprofile/auto-file-backup"
        },
        {
            "title": "Smart Grid Manager",
            "desc": "Streamlit app with XGBoost for energy forecasting.",
            "year": 2025,
            "img": "https://img.icons8.com/color/96/electrical.png",
            "link": "https://github.com/yourprofile/smart-grid"
        },
        {
            "title": "Portfolio",
            "desc": "Streamlit app with various designing elements and custom CSS.",
            "year": 2025,
            "img": "https://img.icons8.com/color/96/electrical.png",
            "link": "https://github.com/yourprofile/smart-grid"
        }
    ]

    filtered_projects = [p for p in projects if year_filter[0] <= p["year"] <= year_filter[1]]
    
    st.markdown("""
    <style>
    @keyframes fadeSlideUp {
        0% {
            opacity: 0;
            transform: translateY(30px);
        }
        100% {
            opacity: 1;
            transform: translateY(0px);
        }
    }

    .project-card {
        border: 1px solid #ccc;
        border-radius: 15px;
        padding: 20px;
        background-color: #0052cc;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        animation: fadeSlideUp 0.6s ease-out;
    }

    .project-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
    }

    .project-title {
        color: #FFA500;
        margin-bottom: 10px;
    }

    .project-desc, .project-year {
        color: #ffffff;
    }

    .project-img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }

    a.card-link {
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)


    # Display cards in 3 columns
    cols = st.columns(2)
    for i, project in enumerate(filtered_projects):
        with cols[i % 2]:
            st.markdown(
                f"""
                <a href="{project['link']}" target="_blank" class="card-link">
                <div class="project-card">
                    <img src="{project['img']}" class="project-img"/>
                    <h3 class="project-title">{project['title']}</h3>
                    <p class="project-desc">{project['desc']}</p>
                    <p class="project-year">📅 {project['year']}</p>
                </div>
                </a>
                """,
                unsafe_allow_html=True
            )

elif page == "Contact":
    st.title("📬 Get in Touch")
    st.markdown("""
    - **Email**: hariprasathasaithambi@gmail.com  
    - **Phone**: +91-9345930934  
    - **LinkedIn**: [www.linkedin.com/in/hari-prasath-782041296)  
    - **GitHub**: [github.com/imayavan](https://github.com/Imayavan-hub)
    """)

# === Footer ===
st.markdown("---")
st.markdown("<center>© 2025 Hariprasath A | All Rights Reserved</center>", unsafe_allow_html=True)

