from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load Assets
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_BX96aR.json")
lottie_aircraft = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_tto68aem.json")
lottie_space = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_cmdcmgh0.json")
img_income_expense = Image.open("images/income_expense_tracker.JPG")
img_badminton = Image.open("images/badminton.JPG")

# Header Section
with st.container():
    st.subheader("Hello, I am JiaHau :wave:")
    st.title("An undergraduate student from Singapore")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Interested in Data Science, Machine Learning, Artificial Intelligence, and Cloud Computing ☁️")
        st.write("[LinkedIn >](https://www.linkedin.com/in/limjiahau/)")
        st.write("[GitHub >](https://github.com/limjiahau)")
        st.write("[Kaggle >](https://www.kaggle.com/jiahaulim)")
        st.write("[Resume >](https://docs.google.com/document/d/1kbwpSgbnK1KIC--Mh3nigywnwblRmixwkpXJVzBPox4/edit?usp=sharing)")
    with right_column:
        st_lottie(lottie_coding, height=150, key="coding")

# My Work Experiences
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work Experiences")
        st.write("##") # add space

        st.subheader("Transcelestial - Engineering Intern")
        st.write("**May 2022 - Jul 2022**")
        st.write(
            """
            - Developed an automated computer vision software using Python and OpenCV to communicate with space payloads via laser communication.
            """
        )    

    with right_column:
        st_lottie(lottie_space, height=150, key="space")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("RSAF - Air Force Engineer(Maintenance)")
        st.write("**Sep 2017 - Apr 2022**")
        st.write(
            """
            - Supervised 150+ Full-time National Servicemen (NSF) during high-risk aircraft operations and inculcated good engineering practices, achieving 100% success in operations and safety.
            """
        )    

    with right_column:
        st.write("##")
        st.write("##")
        st_lottie(lottie_aircraft, height=150, key="aircraft")

# Projects
with st.container():
    st.write("---")
    st.header("My Personal Projects")
    st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_income_expense)
    with text_column:
        st.subheader("Income and Expense Tracker")
        st.write(
            """
            Keep track of monthly income and expenses on an interactive web app created by leveraging Python and the Streamlit library. 

            Using the NoSQL database from deta.

            Visualise monthly spending usinga Sankey Chart from Plotly.

            Uploaded onto Streamlit Cloud.

            Utilised Streamlit's Secrets Management to secure sensitive finance data. 
            """
        )
        st.markdown("[GitHub Repository](https://github.com/limjiahau/income-expense-tracker)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_badminton)
    with text_column:
        st.subheader("Badminton Ladder and Management System")
        st.write(
            """
            Developed a data management program for managing a badminton ladder. 
            
            Features of the program:
            1. Issue a challenge (stating opponent and play-by date)
            2. Record the result of the challenge
            3. Join the ladder
            4. Withdraw from the ladder
            5. Make a query

            Data is stored in two local text files, "ladder.txt" and "data.txt".
            """
        )
        st.markdown("[GitHub Repository](https://github.com/limjiahau/Badminton-Ladder-and-Management-System)")

with st.container():
    st.write("##")
    st.write("Check out my [Kaggle](https://www.kaggle.com/jiahaulim) for more projects related to Data Science")

# Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/josephlimjiahau@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()