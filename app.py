import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Set page title
st.set_page_config(page_title="Harry Chang", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

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

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_utown = Image.open("images/utown.JPG")
img_quest = Image.open("images/quest.jpg")
img_ifg = Image.open("images/ifg.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_lifehack = Image.open("images/lifehack.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_sji = Image.open("images/sji.jpg")
img_tpjc = Image.open("images/tpjc.jpg")
img_nus = Image.open("images/nus.jpeg")
img_questlogo = Image.open("images/questlogo.jpg")
img_scor = Image.open("images/scor.jpg")
img_sephora = Image.open("images/sephora.jpg")
img_iasg = Image.open("images/iasg.jpg")
img_sshsph = Image.open("images/sshsph.jpg")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
img_anime = Image.open("images/anime.jpg")
img_biopics = Image.open("images/biopics.jpg")
img_cellphone = Image.open("images/cellphone.jpg")
img_spotify = Image.open("images/spotify.jpg")
img_videogames = Image.open("images/videogames.jpg")
img_word2vec = Image.open("images/word2vec.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_runes = Image.open("images/runes.png")
#img_lottie_animation = Image.open("images/lottie_animation.gif")
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

with st.sidebar:
    choose = option_menu("Harry Chang", ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Featured Articles", "Contact"],
                         icons=['person fill', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'pencil square', 'envelope'],
                         menu_icon="file-bar-graph", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# Create header
if choose == "About Me":
    with st.container():
        left_column, right_column = st.columns((1,0.55))
        with left_column:
            st.title("Harry Chang")
            st.subheader("Aspiring Data Analyst/Data Scientist")
            st.write("👋🏻 Hi, I'm Harry! I'm a data science and analytics undergraduate based in Singapore. Having prior relevant experiences in tech, reinsurance and consulting sectors, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation.")
            st.write("💼 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to exercise in the gym, run, write, play video games and... eat good food in my free time.")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/13CHoDfb-mYr9F8YSA4ZDV3tZPpNF6eck/view?usp=sharing) | [CV (2 pages)](https://drive.google.com/file/d/1-aubNVEKkgmHdeCtlp_O1M99tVChXfYs/view?usp=sharing)")
        with right_column:
            st.image(img_utown)
            # Create nested columns in the right column
            #spacer_column, image_column = right_column.columns([1, 1])
            # Place the image in the last nested column
            #image_column.image(img_utown, width=300)  # Adjust the width as needed
        
        #st.image(img_utown, width=300, output_format='JPEG')
        #st.write(
            #f"""
            #<style>
            #.reportview-container .main .block-container{{
                #max-width: 100%;
                #padding-top: 0rem;
                #padding-right: 0rem;
                #padding-left: 0rem;
                #padding-bottom: 0rem;
            #}}
            #.reportview-container .main .block-container div {{
                #text-align: center;
            #}}
            #</style>
            #,
            #unsafe_allow_html=True,
        #)

# Create section for About Me
#st.write("---")
#st.header("About Me")
#st.write("Hi, I'm Harry! I'm a data science and analytics undergraduate based in Singapore. Having prior relevant experiences in tech, reinsurance and consulting sectors, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation. With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. With the increase in need for data analytics from both online and brick-and-mortar sales, I am thus aiming to branch into this industry for my first full-time job.")
#st.write("[Resume (1 page)](https://drive.google.com/file/d/13CHoDfb-mYr9F8YSA4ZDV3tZPpNF6eck/view?usp=sharing) | [CV (2 pages)](https://drive.google.com/file/d/1-aubNVEKkgmHdeCtlp_O1M99tVChXfYs/view?usp=sharing)")
#st.write("##")

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_sephora)
        with text_column:
            st.subheader("Product Data Analyst Intern, [Sephora](https://sephora.sg)")
            st.write("June to December 2023 (Upcoming)")
            #st.markdown("- Built, documented and hosted SQL queries and processes to enable reproducible and effective pipelines, analysis and dashboards using BigQuery")
            #st.markdown("- Utilised Domo to create dataflows and visualizations that provide quick insights into product health and performance of e-commerce features (web and mobile)")
            #st.markdown("- Implemented A/B testing to measure potency of new e-commerce features before reporting results")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_questlogo)
        with text_column:
            st.subheader("Marketing Intern, [Quest](https://quest-inc.co)")
            st.write("April to June 2023 (Ongoing)")
            st.markdown("""
            - Launched marketing ad campaigns using Google Ads to target businesses to visit company's landing page
            - Drafted content articles on Wordpress for search engine optimisation (SEO)
            - Performed weekly reporting of user acquisition metrics from various marketing channels, including [TikTok](https://www.tiktok.com/@questhireahero?lang=en) and [Instagram](https://www.instagram.com/questhireahero/)
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_scor)
        with text_column:
            st.subheader("Actuarial Intern, [SCOR](https://scor.com)")
            st.write("May to August 2022 | [Testimonial](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
            st.markdown("""
            - Performed actuarial analysis of reinsurance treaties in various APAC markets, including entry of client portfolio and loss data into xAct (treaty pricing system)
            - Regularly updated and analysed risk profiles and claims databases for insurance markets in Pakistan, Thailand and Vietnam
            - Trained machine learning models (logistic regression, random forest) to predict insurance claims, with an average accuracy of 80% for each model
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_questlogo)
        with text_column:
            st.subheader("Data Analytics Intern, [Quest](https://quest-inc.co)")
            st.write("February to May 2022")
            st.markdown("""
            - Conducted cohort analysis to optimise user acquisition and retention rates
            - Collected, analysed and interpreted trends within user data to improve company’s growth and marketing strategies
            - Built visualizations and dashboards using RStudio and Tableau to report monthly key metrics of company’s mobile application
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_sshsph)
        with text_column:
            st.subheader("Public Health Intern, [Saw Swee Hock School of Public Health](https://sph.nus.edu.sg/)")
            st.write("January to May 2021")
            st.markdown("""
            - Conducted literature reviews and summarized papers related to public health
            - Drafted case study report on British population health system, including impacts from COVID-19
            - Collaborated with other students to compare successes and challenges of Britain, Canada and New Zealand’s healthcare systems
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_iasg)
        with text_column:
            st.subheader("Data Migration Intern, [Immigration@SG LLP](https://iasg.com.sg/)")
            st.write("October 2020 to January 2021 | [Testimonial](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
            st.markdown("""
            - Cleaned over 30,000 records using Pandas to facilitate smooth data migration into new CRM system
            - Derived customer segmentation models using regression models and market basket analysis (association rule mining) to improve company’s marketing strategies
            - Completed time series analysis using past sales data to forecast future monthly revenue
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_yll)
        with text_column:
            st.subheader("Temporary Management Support Staff, [Yong Loo Lin School of Medicine](https://medicine.nus.edu.sg/)")
            st.write("February to June 2019")
            st.markdown("""
            - Answered up to 100 different queries daily regarding undergraduate admissions
            - Managed venue preparations for admissions interviews involving over 1,000 candidates over the span of 2 weeks
            - Supported set-up of faculty booth for NUS Open House, with an estimated attendance of 30,000 visitors in one day
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_saf)
        with text_column:
            st.subheader("Adminisrative Support Assistant, [Singapore Armed Forces](https://www.mindef.gov.sg/web/portal/mindef/home)")
            st.write("January 2017 to January 2019 | [Testimonial](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
            st.markdown("""
            - Assisted in organising division-level In-Camp Trainings, conferences and welfare events
            - Handled daily administration of Operations Branch, including indentation of office equipment, budget management and food rations
            - Promoted to Corporal First Class (CFC) for outstanding efforts
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`R`, `Python`, `SQL`, `Java`, `Stata`, `MATLAB`")
    txt3("Academic Interests","`Data Visualization`, `Market Basket Analysis`, `Recommendation Systems`, `Natural Language Processing`")
    txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Gephi`, `Tableau`, `Power BI`, `Looker (Google Data) Studio`, `Domo`, `Google Analytics`")
    txt3("Database and Cloud Systems", "`MySQL`, `PostgreSQL`, `BigQuery`, `Cloud Firestore`, `Google Cloud Platform`, `Amazon Web Services`")
    txt3("Version Control", "`Git`, `Docker`")
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`, `Wordpress`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `JAX`, `NLTK`")
    txt3("Task Management Tools", "`Asana`, `Notion`, `ClickUp`, `Slack`")
    txt3("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

#st.subheader("Programming Languages")
#st.write("R, Python, SQL, Java, Stata")
#st.subheader("Academic Interests")
#st.write("Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
#st.subheader("Data Visualization")
#st.write("ggplot2, matplotlib, seaborn, Gephi, Tableau, Power BI, Looker (Google Data) Studio, Domo, Google Analytics")
#st.subheader("Database and Cloud Systems")
#st.write("MySQL, PostgreSQL, BigQuery, Cloud Firestore, Google Cloud Platform, Amazon Web Services")
#st.subheader("Version Control")
#st.write("Git, Docker")
#st.subheader("Design and Front-end Development")
#st.write("Canva, Figma, HTML, CSS, Streamlit, Wordpress")
#st.subheader("Data Science Techniques")
#st.write("Regression, Clustering, Association Rules Mining, Random Forest, Decison Trees, Principal Components Analysis, Natural Language Processing, Matrix Factorisation, Collaborative Filtering")
#st.subheader("Machine Learning Frameworks")
#st.write("TensorFlow, Keras, JAX, NLTK")
#st.subheader("Task Management Tools")
#st.write("Asana, Notion, ClickUp, Slack")
#st.subheader("Miscellaneous")
#st.write("Google Firebase, Microsoft Office, Retool, Google Ads")

#st.write("##")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_nus)
        with text_column:
            st.subheader("Bachelor of Science - [Data Science and Analytics](https://www.stat.nus.edu.sg/wp-content/uploads/sites/8/2022/12/NUS-CHS-DSA-Print-FA.pdf), [National University of Singapore](https://nus.edu.sg) (2020-2024)")
            st.write("Relevant Coursework: Computers and the Humanities, Convex Optimization, Data Science in Practice, Data Structures and Algorithms, Data Visualization, Database Technology and Management, Linear Algebra, Multivariable Calculus, Optimization for Large-Scale Data-Driven Inference, Probability, Programming Tools for Economics, Regression Analysis, Statistical Learning")
            st.markdown("""
            Notable Student Activities:
            - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022); Marketing Director (2021-22)
            - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
            - [NUS Inter-Faculty Games](https://ifg.nussportsclub.org/) - Track and Field (Science) Captain (2022)
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_tpjc)
        with text_column:
            st.subheader("GCE A Level - [Tampines Junior College](https://www.tmjc.moe.edu.sg/our-heritage/tampines-jc/) (2015 - 2016)")
            st.write("Coursework: H2 Chemistry, H2 Economics, H2 Mathematics, H1 Project Work, H1 Chinese, H1 History")
            st.markdown("""
            Notable Student Activities: 
            - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
            - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_sji)
        with text_column:
            st.subheader("GCE O Level - [Saint Joseph's Institution](https://www.sji.edu.sg/) (2011 - 2014)")
            st.write("Coursework: English, Mathematics, Additional Mathematics, Physics, Chemistry, History, Geography Elective, Chinese")
            st.markdown("""
            Notable Student Activities: 
            - Track and Field (Long Jump, 100m) 
            - [Business Design Thinking](https://www.sp.edu.sg/sp/news/sp/Secondary-students-learn-to-innovate)
            - Josephian International Experience Programme (Siem Reap, Cambodia)
            """)
#st.write("##")

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Statistical Learning: Analysis on Video Game Sales")
            st.write("Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2")
            st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            - Initial data cleaning and exploratory data analysis (EDA)
            - Multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
            - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
            - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
            """)
            st.write("[Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf) | [Github Repo](https://github.com/harrychangjr/st4248-termpaper)")
        with image_column:
            st.image(img_videogames)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Science Project on Biopics Dataset from Kaggle")
            st.write("Self-initiated project using various machine learning methods on [Kaggle dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)")
            st.markdown("""
            - Performed data preprocessing and drafted visualizations to understand more about the dataset
            - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
            - Used k-means clustering with principal components analysis to identify similar types of movies
            - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
            """)
            st.write("[RPubs](https://rpubs.com/harrychangjr/biopics) | [Github Repo](https://github.com/harrychangjr/biopics)")
        with image_column:
            st.image(img_biopics)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
            st.write("Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2")
            st.markdown("""
            - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
            - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
            - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
            """)
            st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
        with image_column:
            st.image(img_anime)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
            st.write("Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2")
            st.markdown("""
            - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
            - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
            """)
            st.write("[Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf) | [Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb)")
        with image_column:
            st.image(img_word2vec)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data-Driven Marketing: Exploration on 3 datasets related to cellphone billing and subscriber data")
            st.write("Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing")
            st.markdown("""
            - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
            - Trained logit and probit models, as well as providing model estimations for duration models
            - Utilised random forest classifier to predict customer churn
            """)
            st.write("[RPubs](https://rpubs.com/harrychangjr/cellphone) | [Github Repo](https://github.com/harrychangjr/cellphone-billing)")
        with image_column:
            st.image(img_cellphone)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
            st.write("Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2")
            st.markdown("""
            - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
            - Explored how do the four seasons affect number of songs produced in each period
            - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
            """)
            st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
        with image_column:
            st.image(img_spotify)

elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack)
        with text_column:
            st.subheader("[NUS LifeHack 2022](https://lifehack-2022.vercel.app/) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Theme Best - Safety and Overall 2nd Place out of 117 team submissions")
            st.write("Ideated and developed Drive Woke! - a Flutter-based mobile application that aims to keep drivers awake by simulating conversations")
            st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_he4d)
        with text_column:
            st.subheader("NUS Fintech Month Hackathon 2021 - Hosted by [NUS Fintech Society](https://fintechsociety.comp.nus.edu.sg/)")
            st.write("Awarded Overall 2nd Place")
            st.write("Ideated a multi-pronged approach using blockchain and machine learning methods to improve fraud detection amongst complex entities in a digital or hybrid (digital and manual) operating environment")
            st.write("[Pitch Deck](https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_shopee)
        with text_column:
            st.subheader("[Shopee Product and Design Challenge 2021](https://careers.shopee.sg/event-detail/396)")
            st.write("Redesigned user interface of Shopee mobile app using Figma to reduce clutter and increase user utilization of in-app rewards")
            st.write("[Pitch Deck](https://drive.google.com/file/d/12qnveB-SMjG_gF_gwNj3Nr-JsKeyKd6g/view) | [Figma Prototype](https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_sbcc)
        with text_column:
            st.subheader("Singapore Business Case Competition 2020 - Hosted by [NTU Business Solutions Club](https://clubs.ntu.edu.sg/businesssolutions/)")
            st.write("Proposed solutions to help increase competitiveness of BreadTalk after performing market research and analysis on the F&B industry")
            st.write("[Pitch Deck](https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_runes)
        with text_column:
            st.subheader("Contest 2.2 Beautiful Runes - CS1010S Programming Methodology")
            st.write("Awarded 1st Place for 2D Runes category out of over 600 students enrolled in the module for Academic Year 2020/21 Semester 1")
            st.write("2D pixel art created using Pillow (PIL) Library in Python")
            st.write("[Github Repo](https://github.com/harrychangjr/runes)")
#st.write("##")

elif choose == "Featured Articles":
    st.header("Featured Articles")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with text_column:
            st.subheader("Finding success as an outlier")
            st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
            st.write("A personal reflection of my tumultous undergraduate journey so far - and how I finally found my resolve")
            #st.write("[Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
        with image_column:
            st.image(img_outlier)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with text_column:
            st.subheader("Reflections on Organising an 850-participant Data Analytics Competition")
            st.write("February 18, 2022 | [Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
            st.markdown("""
            A personal reflection of organising a large-scale online competition over the course of 6 months - co-written with [Axel Lau](https://www.linkedin.com/in/axel-lau/)
            """)
            #st.write("[Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
        with image_column:
            st.image(img_dac)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with text_column:
            st.subheader("Essays for Final Test - GES1037: A History of Singapore in Ten Objects")
            st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
            st.markdown("""
            Essays written within 24-hour window in Academic Year 2021/22 Semester 2:
            - Q4: Should the statue of Sir Stamford Raffles disappear for good?
            - Q6: Should the Women's Charter replace one of the existing ten objects in the module? 
            """)
        with image_column:
            st.image(img_raffles)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with text_column:
            st.subheader("Does gender inequality still have a place in Singapore's society today?")
            st.write("April 29, 2022 | [Term Paper](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
            st.markdown("""
            Term paper submitted for the module GES1037: A History of Singapore in Ten Objects in Academic Year 2021/22 Semester 2
            """)
        with image_column:
            st.image(img_gender)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with text_column:
            st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
            st.write("April 29, 2021 | [Final Essay](https://github.com/harrychangjr/ges1010/blob/main/GES1010%20Final%20Essay%20A0201825N.pdf)")
            st.markdown("""
            Final essay submitted for the module GES1010: Nation-building in Singapore in Academic Year 2020/21 Semester 2
            """)
        with image_column:
            st.image(img_hci)


elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    with st.container():
        text_column, image_column = st.columns((1,1.5))
        with text_column:
            st.write("Let's connect! You can reach me at harrychang.work@gmail.com")
            st.write("[LinkedIn](https://linkedin.com/in/harrychangjr) | [Github](https://github.com/harrychangjr) | [Linktree](https://linktr.ee/harrychangjr)")
        with image_column:
            st_lottie(lottie_coding, height=500, key="coding")
#st.write("##")
