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
lottie_data_analysis = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_49rdyysj.json")
lottie_cat = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_DnLK6k.json")
img_income_expense = Image.open("images/income_expense_tracker.JPG")
img_badminton = Image.open("images/badminton.JPG")
img_aircraft_thai = Image.open("images/rsaf_thai.JPG")
img_aircraft_darwin = Image.open("images/rsaf_darwin.JPG")
img_transcelestial = Image.open("images/transcelestial.PNG")
img_stock_market = Image.open("images/stock_market.JPG")

# Header Section
with st.container():
    st.subheader("Hello, I am Jia Hau :wave:")
    st.title("An undergraduate student from Singapore")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Majoring in Engineering at Nanyang Technological University (NTU).")
        st.write("Trying to break into the field of Data Science and Artificial Intelligence.")
        st.write("Actively pursuing for opportunities to develop my technical and collaborative skills!")
        st.write("[LinkedIn >](https://www.linkedin.com/in/limjiahau/)")
        st.write("[GitHub >](https://github.com/limjiahau)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# My Work Experiences
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work Experiences")
        st.write("##") # add space
        st.subheader("NTU Wellbeing Office - Data Analyst")
        st.write("**March 2023 - Present**")
        st_lottie(lottie_data_analysis, height=400, key="data")

    with right_column:
        st.write("## \n ## \n ## \n ## \n ##")
        st.write(
            """
            - My role as a Data Analyst includes identifiyng data, metrics and analysis needs for employees while collaborating with subject matter specialists to drive initiatives
            - To allow participants to better understand themselves and aid quality data collection, I developed a profiler survey using Python and Flask to display personalised results.
            - Lead full data life cycle of collecting data to generating insights through behavioural analysis of workshop effectiveness
            - To allow management to make swift decisions, I develop and maintain data models to automate visualisation dashboards.
            """
        )

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##") 
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

with st.container():
    st.write("**Click [here](https://github.com/limjiahau) for my up-to-date projects on GitHub**")
    st.write("##")
    
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_stock_market)
    with text_column:
        st.subheader("Stock Price Direction Prediction")
        st.write(
            """
            1. Predict the day price direction of a stock (i.e. AMZN). 
                - To be profitable, we need to predict correctly whether the price tomorrow will be higher or lower than the price today.
            2. Performed Data Exploration on training, validation and testing set to check for similar distribution and anomalies. 
            3. Carried out Feature Enginering for easier data manipulation.
            4. Machine Learning Algorithms
                - Logistic Regression (AUC: 0.49)
                - Decision Tree (AUC: 0.51)
                - Random Forest (AUC: 0.51)
                - Gradient Boosting Ensemble (AUC: 0.55)
            5. Deep Learning Algorithm
                - Tensorflow, Keras (AUC: 0.5)
            """
        )
        st.markdown("[GitHub Repository](https://github.com/limjiahau/prediction-of-stock-price-direction)")
    
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://github.com/limjiahau/webpage/blob/main/images/market_analysis_2.GIF?raw=true", width=330)
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
            
            Tools Used:
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

            1. Using the NoSQL database from deta.
            2. Visualise monthly spending usinga Sankey Chart from Plotly.
            3. Uploaded onto Streamlit Cloud.
            4. Utilised Streamlit's Secrets Management to secure sensitive finance data. 
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
            Developed an interactive Badminton app with local data management to display a player leaderboard and track scores of completed matches using Python.
            
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

# Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/josephlimjiahau@gmail.com" method="POST" />
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
        # st.empty()
        st_lottie(lottie_cat, height=400, key="cat")
