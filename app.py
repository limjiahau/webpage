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
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_vnikrcia.json")
lottie_aircraft = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_tto68aem.json")
lottie_space = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_lbtOZb.json")
img_income_expense = Image.open("images/income_expense_tracker.JPG")
img_badminton = Image.open("images/badminton.JPG")
img_aircraft_thai = Image.open("images/rsaf_thai.JPG")
img_aircraft_darwin = Image.open("images/rsaf_darwin.JPG")
img_transcelestial = Image.open("images/transcelestial.PNG")

# Header Section
with st.container():
    st.subheader("Hello, I am Joseph :wave:")
    st.title("An undergraduate student from Singapore")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("A current undergraduate student, majoring in Mechanical Engineering at Nanyang Technological University.")
        st.write("Learning about Data Science, Machine Learning, Artificial Intelligence, and Cloud Computing ☁️.")
        st.write("Looking for a long term career in the tech industry and pursue a Masters in Computing if given the opportunity. 🙂")
        st.write("[LinkedIn >](https://www.linkedin.com/in/limjiahau/)")
        st.write("[GitHub >](https://github.com/limjiahau)")
        st.write("[Kaggle >](https://www.kaggle.com/jiahaulim)")
        st.write("[Resume >](https://docs.google.com/document/d/1kbwpSgbnK1KIC--Mh3nigywnwblRmixwkpXJVzBPox4/edit?usp=sharing)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# My Work Experiences
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work Experiences")
        st.write("##") # add space
        st.subheader("Transcelestial - Engineering Intern")
        st.write("**May 2022 - Jul 2022**")
        st.image(img_transcelestial, caption="Transcelestial logo")

    with right_column:
        st.write("## \n ## \n ## \n ## \n ##")
        st.write(
            """
            - Transcelestial is a laser communications startup built on the principle that connectivity is a human right. With a vision to connect billions of people who do not have internet access.
            - A mission to develop the fastest, long-distance, point-to-point wireless communication network possible delivered as a space data network.
            - My internship objectives were to: 
                1. Build up a portable optical ground station with the Celestron CPC 925 Computerised Telescope to establish high-speed laser communication.
                2. Develop an automated computer vision software using Python and OpenCV (Pypogs) to communicate with space payloads. 
            """
        )    
        st_lottie(lottie_space, height=200, key="space")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("RSAF - Air Force Engineer (Maintenance)")
        st.write("**Sep 2017 - Apr 2022**")
        st.image(img_aircraft_thai, caption="RSAF-RTAF 35th Anniversary Combined Exercise 2019 (Cr: RSAF Facebook)", width=500)
        st.image(img_aircraft_darwin, caption="RSAF Darwin Detachment 2021 (Cr: RSAF Facebook)", width=500)

    with right_column:
        st.write("## \n ## \n ## \n ## \n ##")
        st.write(
            """
            - After completing General Maintenance Training in 2017, I was posted to 145 Squadron, home of the Hornets 🐝.
            - I got qualified to work on the F-16D+ Fighting Falcons in 2018 as a Flight Line Crew and ground engineer.
            - My first overseas detachment was in Thailand 2019, as a newly qualified engineer. Nerve-racking, but definitely a memoriable experience!
            - With my management's support and guidance,  I was awarded the RSAF Best Serviceman of 2020 (Engineering Support).
            - Forged friendships with 150+ Full-time National Servicemen (NSF), whom I got to work closely with.            
            - These days, instead of maintaining fighter jets, we are working together to solve tutorial problems in university 🤓.
            """
        )            
        st_lottie(lottie_aircraft, height=450, key="aircraft")

# Projects
with st.container():
    st.write("---")
    st.header("My Personal Projects")
    st.write("##")
    
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://github.com/limjiahau/webpage/blob/main/images/market_analysis_2.GIF?raw=true", width=400)
    with text_column:
        st.subheader("Market Analysis in Dublin")
        st.write(
            """
            The goal of this project was to analyze, understand, visualize, and communicate the demand/supply of the market in Dublin.
            My aim was to answer the following questions:
            - What guests are searching for in Dublin,
            - Which inquiries hosts tend to accept.
            - What gaps exist between guest demand and host supply
            - Any other information that deepens the understanding of the data 
            
            Tools Used
            - Pandas
            - Numpy
            - Seaborn
            - Matplotlib.pyplot
            """
        )
        st.markdown("[GitHub Repository](https://github.com/limjiahau/market-analysis-in-dublin)")

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
    st.write("Check out my [Kaggle](https://www.kaggle.com/jiahaulim) for more projects related to **Data Science**")

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
