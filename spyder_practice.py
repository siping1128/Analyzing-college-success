#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:47:33 2024

@author: zhengsiping
"""
#starter 
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")


my_path=''

df = pd.read_csv(my_path+'dataset.csv')


#clean colume name
def clean_col(c):
    c = c.strip()
    c = c.replace('/', '_')
    c = c.replace(' ', '_')
    c = c.replace('(', '')
    c = c.replace(')', '')
    c = c.lower()
    return c

new_columns = []
for item in df.columns:
    clean_c = clean_col(item)
    new_columns.append(clean_c)
df.columns = new_columns


#converting the categorical data
df.loc[df['marital_status'] == 1, 'marital_status'] = 'Single'
df.loc[df['marital_status'] == 2, 'marital_status'] = 'Married'
df.loc[df['marital_status'] == 3, 'marital_status'] = 'Widower'
df.loc[df['marital_status'] == 4, 'marital_status'] = 'Divorced'
df.loc[df['marital_status'] == 5, 'marital_status'] = 'Facto union'
df.loc[df['marital_status'] == 6, 'marital_status'] = 'Legally seperated'

application_mode = {1:'General', 2:'General', 3:'Special', 4:'High course', 5:'Special', 6:'International(bachelor)', 7:'Special', 8:'General', 9:'General', 10:'Different Plan', 11:'Changed', 12:'Over 23', 13:'Transfer', 14:'Changed', 15:'High course', 16:'Changed', 17:'Short cycle diploma', 18:'Changed'}
df['application_mode'] = df['application_mode'].replace(application_mode)


course = {1:'Technologies (Biofuel)', 2:'Graphic Arts', 3:'Social Service', 4:'Agronomy', 5:'Comm Design', 6:'Veterinary Nursing', 7:'Informatics Engineering', 8:'Agriculture', 9:'Management', 10:'Social Service', 11:'Tourism', 12:'Nursing', 13:'Nursing', 14:'Management', 15:'Journalism & Comm', 16:'Basic Education', 17:'Management'}

df['course'] = df['course'].replace(course)




previous_qualification = {1:'Secondary education', 
                          2:'Bachelor', 
                          3:'Degree', 
                          4:'Master',
                          5:'Doctorate',
                          6:'Bachelor',
                          7:'Secondary education',
                          8:'Primary education',
                          9:'Other',
                          10:'Primary education',
                          11:'Primary education',
                          12:'Primary education',
                          13:'Primary education',
                          14:'Specialization course',
                          15:'Bachelor',
                          16:'Specialization course',
                          17:'Master'}
df['previous_qualification'] = df['previous_qualification'].replace(previous_qualification)



m_and_f_qualification = {1:'Secondary Education', 2:'Bachelor', 3:'Bachelor', 4:'Master', 5:'Doctorate', 6:'Bachelor', 7:'Secondary Education', 8:'Primary Education', 9:'Primary Education', 10:'Secondary Education', 11:'Secondary Education', 12:'Secondary Education', 13:'Commerce course', 14:'Secondary Education', 15:'Secondary Education', 16:'Technical-professional course', 17:'Secondary Education', 18:'Primary Education', 19:'Secondary Education', 20:'Secondary Education', 21:'Secondary Education', 22:'Commerce course', 23:'Accounting & Administration', 24:'Unknown', 25:'Unknown', 26:'Unknown', 27:'Primary Education', 28:'Primary Education', 29:'Specialization course', 30:' Bachelor', 31:'Specialization course', 32:'Specialization course', 33:'Master', 34:'Doctorate'}
df['father\'s_qualification'] = df['father\'s_qualification'].replace(m_and_f_qualification)
df['mother\'s_qualification'] = df['mother\'s_qualification'].replace(m_and_f_qualification)

m_and_f_occupation = {1:'Intermediate Level Technicians and Professions',2:'Intermediate Level Technicians and Professions',3:'Intermediate Level Technicians and Professions',4:'Intermediate Level Technicians and Professions',5:'Intermediate Level Technicians and Professions',6:'Intermediate Level Technicians and Professions',7:'Intermediate Level Technicians and Professions',8:'Intermediate Level Technicians and Professions',9:'Intermediate Level Technicians and Professions',10:'Intermediate Level Technicians and Professions',11:'Intermediate Level Technicians and Professions',12:'Unskilled Workers',13:'Unskilled Workers',14:'Unknown',15:'Administrative staff',16:'Administrative staff',17:'Administrative staff',18:'Intermediate Level Technicians and Professions', 19:'Intermediate Level Technicians and Professions',20:'Armed Forces Professions',21:'Armed Forces Professions',22:'Armed Forces Professions', 23:'Specialists in different realm',24:'Specialists in different realm',25:'Specialists in different realm', 26:'Intermediate Level Technicians and Professions',27:'Administrative staff',28:'Personal service workers', 29:'Personal service workers', 30:'Personal service workers',31:'Personal service workers', 32:'Personal service workers',33:'Personal service workers',34:'operators',35:'operators',36:'operators',37:'operators', 38:'Intermediate Level Technicians and Professions', 39:'Intermediate Level Technicians and Professions', 40:'Intermediate Level Technicians and Professions', 41:'Intermediate Level Technicians and Professions', 42:'Intermediate Level Technicians and Professions', 43:'Specialists in different realm', 44:'Specialists in different realm', 45:'Specialists in different realm', 46:'Specialists in different realm' }
df['mother\'s_occupation'] = df['mother\'s_occupation'].replace(m_and_f_occupation)
df['father\'s_occupation'] = df['father\'s_occupation'].replace(m_and_f_occupation)

gender = {1:'male', 0:'female'}
df['gender'] = df['gender'].replace(gender)

daytime_evening_attendance = {1:'daytime', 0:'evening'}
df['daytime_evening_attendance'] = df['daytime_evening_attendance'].replace(daytime_evening_attendance)

Displaced = {1:'yes', 0:'no'}
df['displaced'] = df['displaced'].replace(Displaced)

educational_special_needs = {1:'yes', 0:'no'}
df['educational_special_needs'] = df['educational_special_needs'].replace(educational_special_needs)


Debtor = {1:'yes', 0:'no'}
df['debtor'] = df['debtor'].replace(Debtor)


Tuition_fees_up_to_date = {1:'yes', 0:'no'}
df['tuition_fees_up_to_date'] = df['tuition_fees_up_to_date'].replace(Tuition_fees_up_to_date)


Scholarship_holder = {1:'yes', 0:'no'}
df['scholarship_holder'] = df['scholarship_holder'].replace(Scholarship_holder)


International = {1:'yes', 0:'no'}
df['international'] = df['international'].replace(International)
nacionality = {1:'Portuguese',
               2:'German', 
               3:'Spanish', 
               4:'Italian', 
               5:'Dutch', 
               6:'English', 
               7:'Lithuanian', 
               8:'Angolan', 
               9:'Cape Verdean', 
               10:'Guinean', 
               11:'Mozambican', 
               12:'Santomean', 
               13:'Turkish', 
               14:'Brazilian', 
               15:'Romanian', 
               16:'Moldova (Republic of)', 
               17:'Mexican', 
               18:'Ukrainian', 
               19:'Russian', 
               20:'Cuban', 
               21:'Colombia'}
df['nacionality'] = df['nacionality'].replace(nacionality)



#dictionaries
num_dict = {'age_at_enrollment':'Age at enrollment', 'curricular_units_1st_sem_credited':"1st sem credited", 'curricular_units_1st_sem_enrolled':'1st sem enrolled', 'curricular_units_1st_sem_evaluations':'1st sem evaluations', 'curricular_units_1st_sem_approved':'1st sem approved', 'curricular_units_1st_sem_grade':'1st sem grade', 'curricular_units_1st_sem_without_evaluations':'1st sem without evaluations', 'curricular_units_2nd_sem_credited':'2nd sem credited', 'curricular_units_2nd_sem_enrolled':'2nd sem enrolled', 'curricular_units_2nd_sem_evaluations':'2nd sem evaluations', 'curricular_units_2nd_sem_approved':'2nd sem_aproved', 'curricular_units_2nd_sem_grade':'2nd sem grade', 'curricular_units_2nd_sem_without_evaluations':'2nd sem without evaluations', 'unemployment_rate':"Local unemployment rate", 'inflation_rate':'Local inflation rate', 'gdp':"Gdp"}

cat_dict = {'marital_status':"Marital status", 'application_mode':'Application mode', 'course':'Course', 'daytime_evening_attendance':'Attendence time', "previous_qualification":"Previous qualification", 'nacionality':'Nacionality', 'mother\'s_qualification':'Mother\'s qualification', 'father\'s_qualification':'Father\'s qualification', 'mother\'s_occupation':'Mother\'s occupation', 'father\'s_occupation':'Father\'s occupation', "displaced":"Displaced", 'educational_special_needs':'Special needs', 'debtor':'Debtor', 'tuition_fees_up_to_date':'Fuition fees up to date', 'gender':'Gender', 'scholarship_holder':'Scholarship', 'international':'International', 'target':'Final result'}

all_col_dic = num_dict.copy()
all_col_dic.update(cat_dict.copy())



with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation Pane',
		options = ['Abstract', 'Background Information', 'Data Cleaning','Exploratory Analysis', 'Student background', 'Parent’s background', 'Analysis of final result', 'Conclusion', 'Bibliography'],
		menu_icon = 'music-note-list',
		icons = ['bookmark-check', 'book', 'box', 'map', 'music-player-fill', 'bar-chart', 'check2-circle'],
		default_index = 0,
		)




if selected=='Abstract':
    st.title("Education Pattern Abstract")
    st.markdown("In real life, there are always different and abundant factors that either motivates or influence people to make choices that are consistent with them. A good example of this is the possible factors that lead to dropout and academic success in the student population.")
    st.markdown("In this project, all of my possible conclusion or prediction will be based on a comprehensive presentation of data on the student profile of a variety of undergraduate degrees offered by institutions of higher education to help us better understand the possible reasons that lead to students dropping out or succeeding academically. The project is intended to dig deeper in to the topic and find more pattern inside the data presented etc.")
    st.markdown("")
    st.markdown("")  
    st.markdown("")  
    st.markdown("Note: Please view this case study in light mode (setting)")  

if selected=="Background Information":
    st.title("Background Information")
    st.markdown("This dataset<sup>1</sup> provides a comprehensive picture of students enrolled in a variety of undergraduate degrees offered by an institution of higher education. It includes demographic data, socioeconomic factors, and academic performance information that can be used to analyze possible predictors of student dropout and academic success. The dataset contains multiple disjointed databases that include information related to enrollment, such as mode of application, marital status, and courses taken. In addition, these data can be used to estimate overall student performance at the end of each semester by assessing course units for which credit/enrollment/assessment/approval has been earned and their respective grades. Finally, the database additionally provides the unemployment rate, inflation rate, and Gross Domestic Product (GDP) for the district, which can help us further understand how economic factors affect student dropout rates or academic performance.", unsafe_allow_html=True)
    st.markdown('This dataset contains data from a higher education institution on various variables related to undergraduate students, including demographics, social-economic factors, and academic performance, to investigate the impact of these factors on student dropout and academic success. This dataset was successfully contructed due to the support of the programe "SATDAP - Capacitação da Administração Pública under grant POCI-05-5762-FSE-000191, Portugal". Columns included, meanning and their data type are listed here: Marital status: The marital status of the student (Categorical). Application mode: The method of application used by the student (Categorical). Application order: The order in which the student applied (Numerical). Course: The course taken by the student (Categorical). Daytime/evening attendance: Whether the student attends classes during the day or in the evening (Categorical). Previous qualification: The qualification obtained by the student before enrolling in higher education (Categorical). Nacionality: The nationality of the student (Categorical). Mother\'s qualification: The qualification of the student\'s mother (Categorical). Father\'s qualification: The qualification of the student\'s father (Categorical). Mother\'s occupation: The occupation of the student\'s mother (Categorical). Father\'s occupation: The occupation of the student\'s father (Categorical). Displaced: Whether the student is a displaced person (Categorical). Educational special needs: Whether the student has any special educational needs (Categorical). Debtor: Whether the student is a debtor (Categorical). Tuition fees up to date: Whether the student\'s tuition fees are up to date (Categorical). Gender: The gender of the student (Categorical). Scholarship holder: Whether the student is a scholarship holder (Categorical). Age at enrollment: The age of the student at the time of enrollment (Numerical). International: Whether the student is an international student (Categorical). Curricular units 1st sem (credited): The number of curricular units credited by the student in the first semester (Numerical). Curricular units 1st sem (enrolled): The number of curricular units enrolled by the student in the first semester (Numerical). Curricular units 1st sem (evaluations): The number of curricular units evaluated by the student in the first semester (Numerical). Curricular units 1st sem (approved): The number of curricular units approved by the student in the first semester. (Numerical)')
    st.markdown('Based on the past study published in Medium<sup>2</sup>, it suggested several interesting facts: Application mode does matter, and the age of enrollment has the highest dropout rate of any other type.Scholarship holder tend to have fewer dropouts than non-scholarship holders. Gender, marital status, or a parent’s occupation does not matter in a drop-out case. Drop out Students who pay the current tuition fees up to date are two times more likely to drop out than students who pay the latter tuition fees.', unsafe_allow_html = True)
    st.markdown('Another study published in linkin<sup>3</sup> suggested the following conclusions. The four major factor is personal problems, academic difficulties, financial pressures, and school environment:', unsafe_allow_html = True)
    st.markdown('Personal problems: One of the most common reasons students drop out of school is personal issues. These can include health issues, family responsibilities, pregnancy, substance abuse, mental health challenges or trauma, to name a few. Everything can make it difficult for students to focus on their studies, attend classes regularly or cope with stress. Also, they may feel isolated, unsupported or ashamed of their situation and end up choosing to drop out of school.')
    st.markdown('Academic difficulties: Another common reason why students drop out of school is academic difficulties. These may include low grades, learning disabilities, lack of interest, boredom or frustration. Academic difficulties can leave students feeling discouraged, overwhelmed, or hopeless about their chances for success. They may also lose confidence in their abilities, skills, or goals.')
    st.markdown('Financial pressures: A third common reason students drop out of school is financial stress. These can include poverty, unemployment, debt, or the need to support themselves or their families. Financial pressures can cause students to feel stressed, anxious or desperate about their financial situation. They may also have to choose between work and study or sacrifice education for immediate income.')
    st.markdown('School environment: The fourth common reason students drop out of school is the school environment. This can include factors such as safety, discipline, bullying, peer pressure, or teacher-student relationships. The school environment can affect a student\'s sense of belonging, respect, and trust. It can also affect their attitudes, behaviors, and values. Students with negative school environments may feel unsafe, unhappy or alienated. They may also develop an aversion or distrust of school or authority figures.')
    st.markdown('The third source published in SCISPACE<sup>4</sup> suggested that there are many factors that contribute to students dropping out of school. Like mentioned in link in, these factors include personal factors such as gender, grade level, academic performance and depression. Family factors such as parental autonomy support, parental neglect, and parental divorce also contribute to dropout. In addition, school factors such as satisfaction with school life, invasion of student privacy, teacher abuse, and infrastructure can also have an impact on a student\'s intention to drop out. Other factors include dislike of school, school distance from home, parental displacement, student bullying, inability to enroll, parental neglect, and lack of investment in learning. Economic factors, learning satisfaction, academic performance and family finances also have an impact on student dropout. These factors can have varying degrees of influence in different countries, so it is important to analyze the many and comprehensive perspectives that lead to student success or dropout.', unsafe_allow_html = True)
    st.markdown('In this project, all of my possible conclusion or prediction will be based on a comprehensive presentation of data on the student profile of a variety of undergraduate degrees offered by institutions of higher education to help us better understand the possible reasons that lead to students dropping out or succeeding academically. The project is intended to dig deeper in to the topic and find more pattern inside the data presented etc.')
    st.markdown('The major reason that shows the importance to know the possible factors that could possibly led to the success or a drop in student’s learning process was because education it self was very important. As a student, it is informative to analyze and gain an in-depth understanding of the impact of different factors on students during their time as a student. Analyzing this data will provide us with an in-depth look at what motivates students to stay in school or to drop out of a variety of disciplines such as agronomy, design, education, nursing, journalism management, social services, or technology.')
    st.markdown('First of all, it was important to you. It helps to develop critical thinking and learn basic skill that you need as a grown up, the benefits of it includes a relatively healthy diets and body. Based on News medical.com<sup>5</sup>, researchers found that for every year of education, the risk of death, barring unforeseen accidents, decreased by two percent. This means that people who completed six years of elementary school had an average 13 percent lower risk of death; after high school, the risk of death was nearly 25 percent lower; and with 18 years of education, the risk of death was 34 percent lower. Dr. Terje Andreas Eikemo, the co-author and head of Centre for Global Health Inequalities Research (CHAIN) at the Norwegian University of Science and Technology (NTNU) have once said that :"Education is important in its own right, not just for its benefits on health, but now being able to quantify the magnitude of this benefit is a significant development.', unsafe_allow_html = True)
    st.markdown('Further more, it enabled you to find and develop your own expertise that made you unique and gives you an opportunity to earn money and live independently. According to oecd.com<sup>6</sup>, on average in OECD countries, the unemployment rate for those with higher education has been below 5 per cent, while the unemployment rate for those with only upper secondary education is below 8 per cent. Between 1998 and 2010, the unemployment rate for those with no upper secondary education exceeded 10 per cent on several occasions. During the economic crisis, the average increase in the unemployment rate for persons with no upper secondary education was 1.1 percentage points higher than for persons with at least upper secondary education. In addition, based on world bank blogs, an additional year of schooling increases earnings by 10 percent a year.', unsafe_allow_html = True)
    st.markdown('On top of that, in a more macro level, it benefits<sup>7</sup> the whole “humanity”. Educated people develops local industry, economy, infrastructures etc. especially the internet that made everyone’s lives being more efficient. ')

  
    
if selected=="Data Cleaning":
    st.title('Data Cleaning')
    st.markdown("The data cleaning process mainly involves standardizing the characters that in the column names, converting the numbers for the categorical data to words and group some similar category into one, and create two separate  dictionaries for categorical data and numeric data with the pretty names.")
    
    st.markdown("Starter: import necessary tool that will be used throughout the analysis encoding and read in data:")
    starter='''import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")

my_path='/Users/zhengsiping/data_science/'

df = pd.read_csv(my_path+'dataset.csv')'''
    st.code(starter,language='python')
    
    st.markdown("Clean column names: To avoid possible typos in future analyses, I have standardized the names in each column. I created a function called \"clean_col\" in the following code, which helped me to make all the names of the columns lowercase; to make all the '(' and ')' into '-'; and to make all the spaces into '-'. ' into '-'; it also helps me to turn all spaces into '-' and so on. I then applied the function and cleaned up the column names:")
    cleanning = '''def clean_col(c):
    c = c.strip()
    c = c.replace('/', '_')
    c = c.replace(' ', '_')
    c = c.replace('(', '')
    c = c.replace(')', '')
    c = c.lower()
    return c

new_columns = []
for item in df.columns:
    clean_c = clean_col(item)
    new_columns.append(clean_c)
df.columns = new_columns'''
    st.code(cleanning,language='python')
    
    st.markdown("Replace the values for categorical data: For some reason, all of the categorical data in the original dataset was presented in a numerical pattern (but each number had its own meaning, it all represent one small group inside one big category). In order to analyze it more efficiently and avoid mistake, I changed all the numbers to their original meanings according to the documentation of the dataset (instead of continuing to analyze them with numbers). I also combined some small group in each categorical data in to a slightly bigger group based on it’s meaning, this help to decrease the column in the graph and make it easier to analyze. The following data shows the process of transforming each column of categorical data:")
    datetime_code = '''df.loc[df['marital_status'] == 1, 'marital_status'] = 'Single'
df.loc[df['marital_status'] == 2, 'marital_status'] = 'Married'
df.loc[df['marital_status'] == 3, 'marital_status'] = 'Widower'
df.loc[df['marital_status'] == 4, 'marital_status'] = 'Divorced'
df.loc[df['marital_status'] == 5, 'marital_status'] = 'Facto union'
df.loc[df['marital_status'] == 6, 'marital_status'] = 'Legally seperated'

application_mode = {1:'General', 2:'General', 3:'Special', 4:'High course', 5:'Special', 6:'International(bachelor)', 7:'Special', 8:'General', 9:'General', 10:'Different Plan', 11:'Changed', 12:'Over 23', 13:'Transfer', 14:'Changed', 15:'High course', 16:'Changed', 17:'Short cycle diploma', 18:'Changed'}
df['application_mode'] = df['application_mode'].replace(application_mode)

course = {1:'Technologies (Biofuel)', 2:'Graphic Arts', 3:'Social Service', 4:'Agronomy', 5:'Comm Design', 6:'Veterinary Nursing', 7:'Informatics Engineering', 8:'Agriculture', 9:'Management', 10:'Social Service', 11:'Tourism', 12:'Nursing', 13:'Nursing', 14:'Management', 15:'Journalism & Comm', 16:'Basic Education', 17:'Management'}
df['course'] = df['course'].replace(course)

previous_qualification = {1:'Secondary education', 
                              2:'Bachelor', 
                              3:'Degree', 
                              4:'Master',
                              5:'Doctorate',
                              6:'Bachelor',
                              7:'Secondary education',
                              8:'Primary education',
                              9:'Other',
                              10:'Primary education',
                              11:'Primary education',
                              12:'Primary education',
                              13:'Primary education',
                              14:'Specialization course',
                              15:'Bachelor',
                              16:'Specialization course',
                              17:'Master'}
df['previous_qualification'] = df['previous_qualification'].replace(previous_qualification)

m_and_f_qualification = {1:'Secondary Education', 2:'Bachelor', 3:'Bachelor', 4:'Master', 5:'Doctorate', 6:'Bachelor', 7:'Secondary Education', 8:'Primary Education', 9:'Primary Education', 10:'Secondary Education', 11:'Secondary Education', 12:'Secondary Education', 13:'Commerce course', 14:'Secondary Education', 15:'Secondary Education', 16:'Technical-professional course', 17:'Secondary Education', 18:'Primary Education', 19:'Secondary Education', 20:'Secondary Education', 21:'Secondary Education', 22:'Commerce course', 23:'Accounting & Administration', 24:'Unknown', 25:'Unknown', 26:'Unknown', 27:'Primary Education', 28:'Primary Education', 29:'Specialization course', 30:' Bachelor', 31:'Specialization course', 32:'Specialization course', 33:'Master', 34:'Doctorate'}
df['father\'s_qualification'] = df['father\'s_qualification'].replace(m_and_f_qualification)
df['mother\'s_qualification'] = df['mother\'s_qualification'].replace(m_and_f_qualification)

m_and_f_occupation = {1:'Intermediate Level Technicians and Professions',2:'Intermediate Level Technicians and Professions',3:'Intermediate Level Technicians and Professions',4:'Intermediate Level Technicians and Professions',5:'Intermediate Level Technicians and Professions',6:'Intermediate Level Technicians and Professions',7:'Intermediate Level Technicians and Professions',8:'Intermediate Level Technicians and Professions',9:'Intermediate Level Technicians and Professions',10:'Intermediate Level Technicians and Professions',11:'Intermediate Level Technicians and Professions',12:'Unskilled Workers',13:'Unskilled Workers',14:'Unknown',15:'Administrative staff',16:'Administrative staff',17:'Administrative staff',18:'Intermediate Level Technicians and Professions', 19:'Intermediate Level Technicians and Professions',20:'Armed Forces Professions',21:'Armed Forces Professions',22:'Armed Forces Professions', 23:'Specialists in different realm',24:'Specialists in different realm',25:'Specialists in different realm', 26:'Intermediate Level Technicians and Professions',27:'Administrative staff',28:'Personal service workers', 29:'Personal service workers', 30:'Personal service workers',31:'Personal service workers', 32:'Personal service workers',33:'Personal service workers',34:'operators',35:'operators',36:'operators',37:'operators', 38:'Intermediate Level Technicians and Professions', 39:'Intermediate Level Technicians and Professions', 40:'Intermediate Level Technicians and Professions', 41:'Intermediate Level Technicians and Professions', 42:'Intermediate Level Technicians and Professions', 43:'Specialists in different realm', 44:'Specialists in different realm', 45:'Specialists in different realm', 46:'Specialists in different realm' }
df['mother\'s_occupation'] = df['mother\'s_occupation'].replace(m_and_f_occupation)
df['father\'s_occupation'] = df['father\'s_occupation'].replace(m_and_f_occupation)

gender = {1:'male', 0:'female'}
df['gender'] = df['gender'].replace(gender)

daytime_evening_attendance = {1:'daytime', 0:'evening'}
df['daytime_evening_attendance'] = df['daytime_evening_attendance'].replace(daytime_evening_attendance)

Displaced = {1:'yes', 0:'no'}
df['displaced'] = df['displaced'].replace(Displaced)

educational_special_needs = {1:'yes', 0:'no'}
df['educational_special_needs'] = df['educational_special_needs'].replace(educational_special_needs)

Debtor = {1:'yes', 0:'no'}
df['debtor'] = df['debtor'].replace(Debtor)

Tuition_fees_up_to_date = {1:'yes', 0:'no'}
df['tuition_fees_up_to_date'] = df['tuition_fees_up_to_date'].replace(Tuition_fees_up_to_date)

Scholarship_holder = {1:'yes', 0:'no'}
df['scholarship_holder'] = df['scholarship_holder'].replace(Scholarship_holder)

International = {1:'yes', 0:'no'}
df['international'] = df['international'].replace(International)
nacionality = {1:'Portuguese',
               2:'German', 
               3:'Spanish', 
               4:'Italian', 
               5:'Dutch', 
               6:'English', 
               7:'Lithuanian', 
               8:'Angolan', 
               9:'Cape Verdean', 
               10:'Guinean', 
               11:'Mozambican', 
               12:'Santomean', 
               13:'Turkish', 
               14:'Brazilian', 
               15:'Romanian', 
               16:'Moldova (Republic of)', 
               17:'Mexican', 
               18:'Ukrainian', 
               19:'Russian', 
               20:'Cuban', 
               21:'Colombia'}
df['nacionality'] = df['nacionality'].replace(nacionality)'''
    st.code(datetime_code,language='python')
    
    st.markdown("Create list for drop downs: I create two lists, they are cat_dict, that involve all the categorical data’s column name; and num_dict, that involve all the numeric data’s column name. These two dictionary are used to present the dropdown. I also change the original cleaned column names in to the “pretty names” to make it easier to understand by converting them using “:”:")
    datetime_code = '''num_dict = {'age_at_enrollment':'Age at enrollment', 'curricular_units_1st_sem_credited':"1st sem credited", 'curricular_units_1st_sem_enrolled':'1st sem enrolled', 'curricular_units_1st_sem_evaluations':'1st sem evaluations', 'curricular_units_1st_sem_approved':'1st sem approved', 'curricular_units_1st_sem_grade':'1st sem grade', 'curricular_units_1st_sem_without_evaluations':'1st sem without evaluations', 'curricular_units_2nd_sem_credited':'2nd sem credited', 'curricular_units_2nd_sem_enrolled':'2nd sem enrolled', 'curricular_units_2nd_sem_evaluations':'2nd sem evaluations', 'curricular_units_2nd_sem_approved':'2nd sem_aproved', 'curricular_units_2nd_sem_grade':'2nd sem grade', 'curricular_units_2nd_sem_without_evaluations':'2nd sem without evaluations', 'unemployment_rate':"Local unemployment rate", 'inflation_rate':'Local inflation rate', 'gdp':"Gdp"}

cat_dict = {'marital_status':"Marital status", 'application_mode':'Application mode', 'course':'Course', 'daytime_evening_attendance':'Attendence time', "previous_qualification":"Previous qualification", 'nacionality':'Nacionality', 'mother\'s_qualification':'Mother\'s qualification', 'father\'s_qualification':'Father\'s qualification', 'mother\'s_occupation':'Mother\'s occupation', 'father\'s_occupation':'Father\'s occupation', "displaced":"Displaced", 'educational_special_needs':'Special needs', 'debtor':'Debtor', 'tuition_fees_up_to_date':'Fuition fees up to date', 'gender':'Gender', 'scholarship_holder':'Scholarship', 'international':'International', 'target':'Final result'}''' 
    st.code(datetime_code,language='python')
    
    st.markdown("Below is the top 30 rows of the cleaned version of the dataset:")
    st.dataframe(df.head(30))
    








if selected=="Exploratory Analysis":
    st.title('Exploratory Analysis')
    my_colors = ['#46d2d2', '#1e7b7b', '#99ffcc', '#ccffe5', '#ffd9b3', '#ff8c1a', '#f2e6ff', '#ca99ff', '#cceeff', ' #4dc3ff', '#007399', '#004d66', '#ff5c33', '#b32400', '#df9f9f', '#cc6666', '#bf4040', '#732626', '#c6538c', '#993366', '#6666ff', '#1a1aff', '#e6e6ff', '#ddff99', '#ccff66', '#558000', '#b3b3cc', '#8585ad', ' #47476b', '#333333']
    
    #graph 1
    st.markdown("### <b>Graph 1 (Histogram): 2 Numeric variable and 1 categorical variables</b>", unsafe_allow_html=True)
    col1,col2=st.columns([3,5])
    with st.form("<b>Graph 1 (Histogram): 2 Nmeric variable and 1 categorical variables</b>l"):
        #creatig x axis input
        col1x = col1.selectbox('Choose a numerical variable to display in the X axis', num_dict.values(), key = 1)
        col1xdf = [k for k,v in num_dict.items() if v == col1x][0]
        
        #creatig y axis input
        col1y = col1.selectbox('Choose a numerical variable to display in the Y axis', np.setdiff1d(list(num_dict.values()), [col1x]), key = 2)
        col1ydf = [k for k,v in num_dict.items() if v == col1y][0] 
       
        #creatig color input
        col1c = col1.selectbox('Choose a categorical variable to present in colors', cat_dict.values(), key = 3)
        col1cdf = [k for k,v in cat_dict.items() if v == col1c][0]
         
        #add the check box
        check1 = col1.checkbox("Check to decide the number of bins",key=20)
        b1 = 5
        if check1:
            col1_ni1 = col1.number_input("Enter a number to decide the number of bins", min_value=5, placeholder="Type a number here")
            b1 = col1_ni1
    
        #make submite bottom
        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            fig1 = px.histogram(df, x = col1xdf, y = col1ydf, color = col1cdf, histfunc = 'avg', barmode = 'group', labels = all_col_dic, nbins = b1)
            fig1.update_traces(marker_line_width = 3)
            
            col2.plotly_chart(fig1)

    
    #graph 2
    st.markdown("### <b>Graph 2 (Histogram): 2 categorical variables and numeric variable</b>",unsafe_allow_html=True)
    col3,col4=st.columns([3,5])
    with st.form("<b>Graph 2 (Histogram): 2 categorical variables and numeric variable</b>"):
        #creatig x axis input
        col3x = col3.selectbox('Choose a numerical variable to display in the X axis', num_dict.values(), key = 4)
        col3xdf = [k for k,v in num_dict.items() if v == col3x][0]
        
        #creatig y axis input
        col3y = col3.selectbox('Choose a categorical variable to display in the Y axis', cat_dict.values(), key = 5)
        col3ydf = [k for k,v in cat_dict.items() if v == col3y][0]
       
        #creatig color input
        col3c = col3.selectbox('Choose a categorical variable to present in colors', np.setdiff1d(list(cat_dict.values()), [col3y]), key = 6)
        col3cdf = [k for k,v in cat_dict.items() if v == col3c][0]
  
    
        #make submite bottom
        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            fig2 = px.histogram(df, x = col3xdf, y = col3ydf, color = col3cdf, histfunc = 'avg', barmode = 'group', labels = all_col_dic)
            fig2.update_traces(marker_line_width = 1)
            col4.plotly_chart(fig2)
            
            
            
            
    #graph 3
    st.markdown("### <b>Graph 3 (Histogram): 1 categorical variables and 1 numeric variable</b>",unsafe_allow_html=True)
    col5,col6=st.columns([3,5])
    with st.form("<b>Graph 3 (Histogram): 1 categorical variables and 1 numeric variable</b>"):
        
        #creatig x axis input
        col5x = col5.selectbox('Choose a numerical variable to display in the X axis', num_dict.values(), key = 7)
        col5xdf = [k for k,v in num_dict.items() if v == col5x][0]
        
        #creatig color input
        col5c = col5.selectbox('Choose a categorical variable to present in colors', cat_dict.values(), key = 9)
        col5cdf = [k for k,v in cat_dict.items() if v == col5c][0]
        
        #check box for percent
        percent = None
        check5 = col5.checkbox('Check to display a normalized histogram', key = 10)
        if check5:
            percent = "percent"
        
        #add the check box
        check5_2 = col5.checkbox("Check to decide the number of bins",key=11)
        b2 = 5
        if check5_2:
            col5_ni2 = col5.number_input("Enter a number to decide the number of bins", min_value=5, placeholder="Type a number here")
            b2 = col5_ni2           
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the histogram")
        if submitted:
            fig3 = px.histogram(df, x = col5xdf, color = col5cdf, histnorm = percent, barmode = 'group', labels = all_col_dic, nbins = b2)
            fig3.update_traces(marker_line_width = 2)
            col6.plotly_chart(fig3)
       

        
    #graph 4
    st.markdown("### <b>Graph 4 (Histogram): 2 categorical variables</b>", unsafe_allow_html=True)
    col7,col8=st.columns([2,7])
    with st.form("<b>Graph 4 (Histogram): 2 categorical variables</b>"):
        
        #creatig y axis input
        col7y = col7.selectbox('Choose a categorical variable to display in the y axis', cat_dict.values(), key = 12)
        col7ydf = [k for k,v in cat_dict.items() if v == col7y][0]
        
        #creatig color input
        col7c = col7.selectbox('Choose a categorical variable to present in colors', np.setdiff1d(list(cat_dict.values()), [col7y]), key = 13)
        col7cdf = [k for k,v in cat_dict.items() if v == col7c][0]
        
        #check box for percent
        percent = None
        check7 = col7.checkbox('Check to display a normalized histogram', key = 14)
        if check7:
            percent = "percent"
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the histogram")
        if submitted:
            fig4 = px.histogram(df, x = col7ydf, color = col7cdf, histnorm = percent, barmode = 'group', labels = all_col_dic, facet_col = col7cdf, facet_col_wrap=3, height = 1000, width = 1800, facet_col_spacing = 0.15, color_discrete_sequence = my_colors)
            fig4.update_traces(marker_line_width = 0.5)
            fig4.update_yaxes(matches=None)
            fig4.update_xaxes(matches=None)
            fig4.update_layout(legend={
            "x": 1,
            "y": 1,
            "xref": "container",
            "yref": "container"})
            col8.plotly_chart(fig4)
        
            
            
    

    #graph 5
    st.markdown("### <b>Graph 5 (Scatter plot): 2 Numeric variable and 1 categorical variables</b>", unsafe_allow_html=True)
    col9,col10=st.columns([3,5])
    with st.form("<b>Graph 5 (Scatter plot): 2 Nmeric variable and 1 categorical variables</b>"):
        #creatig x axis input
        col9x = col9.selectbox('Choose a numerical variable to display in the X axis', num_dict.values(), key = 16)
        col9xdf = [k for k,v in num_dict.items() if v == col9x][0]
        
        #creatig y axis input
        col9y = col9.selectbox('Choose a numerical variable to display in the Y axis', np.setdiff1d(list(num_dict.values()), [col9x]), key = 17)
        col9ydf = [k for k,v in num_dict.items() if v == col9y][0]
       
        #creatig color input
        col9c = col9.selectbox('Choose a categorical variable to present in colors', cat_dict.values(), key = 18)
        col9cdf = [k for k,v in cat_dict.items() if v == col9c][0]
    
        #make submite bottom
        submitted=st.form_submit_button("Submit to produce the Scatter")
        if submitted:
            fig5 = px.scatter(df, x = col9xdf, y = col9ydf, color = col9cdf, labels = all_col_dic)
            fig5.update_traces(marker_line_width = 1)
            col10.plotly_chart(fig5)



    #graph 6
    st.markdown("### <b>Graph 6 (Box plot): 1 categorical variables and 1 numeric variable</b>",unsafe_allow_html=True)
    col11,col12=st.columns([3,5])
    with st.form("<b>Graph 6 (Box plot): 1 categorical variables and 1 numeric variable</b>"):
        
        #creatig x axis input
        col11x = col11.selectbox('Choose a categorical variable to display in the X axis', cat_dict.values(), key = 19)
        col11xdf = [k for k,v in cat_dict.items() if v == col11x][0]
        
        #creatig color input
        col11c = col11.selectbox('Choose a numeric variable to present in colors', num_dict.values(), key = 21)
        col11cdf = [k for k,v in num_dict.items() if v == col11c][0]
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Box")
        if submitted:
            fig6 = px.box(df, x = col11cdf, y = col11xdf, color = col11cdf, color_discrete_sequence= my_colors,labels = all_col_dic)
            fig6.update_traces(marker_line_width = 2)
            col12.plotly_chart(fig6)  
  
        
  
    #graph 7
    st.markdown("### <b>Graph 7 (Histogram): Target and 1 numeric variable</b>",unsafe_allow_html=True)
    col13,col14=st.columns([3,5])
    with st.form("### <b>Graph 7 (Histogram): Target and 1 numeric variable</b>"):
        
        #creatig x axis input
        col13x = col13.selectbox('Choose a numeric variable to display in the X axis', num_dict.values(), key = 22)
        col13xdf = [k for k,v in num_dict.items() if v == col13x][0]
        
        #creatig color input
        col13cdf = df['target']
        
        #check box for percent
        percent = None
        check13 = col13.checkbox('Check to display a normalized histogram', key = 35)
        if check13:
            percent = "percent"
        
        #add the check box
        check13_2 = col13.checkbox("Check to decide the number of bins",key=36)
        b13 = 4
        if check13_2:
            col13_ni2 = col13.number_input("Enter a number to decide the number of bins", min_value=4, placeholder="Type a number here")
            b13 = col13_ni2
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig7 = px.histogram(df, x = col13xdf, color = col13cdf, barmode = 'group', color_discrete_sequence= my_colors,labels = all_col_dic, histnorm = percent, nbins = b13)
            fig7.update_traces(marker_line_width = 3)
            col14.plotly_chart(fig7)
            
    
    
    
    #graph 8
    st.markdown("### <b>Graph 8 (Histogram): Target and 1 categorical variable</b>",unsafe_allow_html=True)
    col15,col16=st.columns([3,5])
    with st.form("### <b>Graph 8 (Histogram): Target and 1 categorical variable</b>"):
        
        #creatig x axis input
        col15x = col15.selectbox('Choose a categorical variable to display in the X axis', cat_dict.values(), key = 23)
        col15xdf = [k for k,v in cat_dict.items() if v == col15x][0]
        
        #creatig color input
        col15cdf = df['target']
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig8 = px.histogram(df, x = col15xdf, color = col15cdf, barmode = 'group', color_discrete_sequence= my_colors,labels = all_col_dic)
            fig8.update_traces(marker_line_width = 3)
            col16.plotly_chart(fig8)
            



    #graph 9
    st.markdown("### <b>Graph 9 (Histogram): Student’s background information and 1 numeric variable:</b>",unsafe_allow_html=True)
    col17,col18=st.columns([2,6])
    with st.form("### <b>Graph 9 (Histogram): Student’s background information and 1 numeric variable</b>"):
        
        #creatig x axis input
        col17x = col17.selectbox('Choose a numeric variable to display in the X axis', num_dict.values(), key = 24)
        col17xdf = [k for k,v in num_dict.items() if v == col17x][0]
            
        #check box for percent
        percent = None
        check17 = col17.checkbox('Check to display a normalized histogram', key = 37)
        if check17:
            percent = "percent"
        
        #add the check box
        check17_2 = col17.checkbox("Check to decide the number of bins",key=38)
        b17 = 5
        if check17_2:
            col17_ni2 = col17.number_input("Enter a number to decide the number of bins", min_value=5, placeholder="Type a number here")
            b17 = col17_ni2
        
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig9 = px.histogram(pd.melt(df, id_vars= [col17xdf], value_vars = ['marital_status', 'scholarship_holder']), x = col17xdf, color = 'value', barmode = 'group', color_discrete_sequence= my_colors, facet_col = 'variable', labels = all_col_dic, nbins = b17, histnorm = percent, facet_col_wrap =2)
            fig9.update_traces(marker_line_width = 2)
            col18.plotly_chart(fig9)
            
            
            
    #graph 10
    st.markdown("### <b>Graph 10 (Histogram): Student’s background information and 1 categorical variable</b>",unsafe_allow_html=True)
    col19,col20=st.columns([2,6])
    with st.form("### <b>Graph 10 (Histogram): Student’s background information and 1 categorical variable</b>"):
        
        #creatig x axis input
        col19x = col19.selectbox('Choose a categorical variable to display in the X axis', cat_dict.values(), key = 25)
        col19xdf = [k for k,v in cat_dict.items() if v == col19x][0]

        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig10 = px.histogram(pd.melt(df, id_vars= [col19xdf], value_vars = ['marital_status', 'scholarship_holder']), x = col19xdf, color = 'value', barmode = 'group', color_discrete_sequence= my_colors, facet_col = 'variable', labels = all_col_dic, facet_col_wrap =2)
            fig10.update_traces(marker_line_width = 3)
            col20.plotly_chart(fig10)
            
            
            
    #graph 11
    st.markdown("### <b>Graph 12 (Histogram): Parent's background characteristic and 1 numeric variable</b>",unsafe_allow_html=True)
    col21,col22=st.columns([2,6])
    with st.form("### <b>Graph 12 (Histogram): Parent's background characteristic and 1 numeric variable</b>"):
        
        #creatig x axis input
        col21x = col21.selectbox('Choose a numeric variable to display in the X axis', num_dict.values(), key = 26)
        col21xdf = [k for k,v in num_dict.items() if v == col21x][0]
        
        #creatig color input
        col21cdf = df['mother\'s_qualification']
        
        #check box for percent
        percent21 = None
        check21 = col21.checkbox('Check to display a normalized histogram', key = 39)
        if check21:
            percent21 = "percent"
        
        #add the check box
        check21_2 = col21.checkbox("Check to decide the number of bins",key=40)
        b21 = 6
        if check21_2:
            col21_ni2 = col21.number_input("Enter a number to decide the number of bins", min_value=6, placeholder="Type a number here")
            b21 = col21_ni2
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig11 = px.histogram(pd.melt(df, id_vars=[col21xdf], value_vars=['mother\'s_occupation', 'father\'s_occupation', 'mother\'s_qualification', 'father\'s_qualification']), x = col21xdf, color = 'value', barmode = 'group', color_discrete_sequence= my_colors,labels = all_col_dic, facet_col = 'variable', facet_col_wrap = 2, nbins = b21, histnorm = percent21)
            fig11.update_traces(marker_line_width = 0.3)
            fig11.update_yaxes(matches=None)
            col22.plotly_chart(fig11)


    #graph 13
    st.markdown("### <b>Graph 13 (Histogram): Parent's background characteristic and 1 cetegorical variable</b></b>",unsafe_allow_html=True)
    col23,col24=st.columns([2,6])
    with st.form("### <b>Graph 13 (Histogram): Parent's background characteristic and 1 cetegorical variable</b>"):
        
        #creatig x axis input
        col23x = col23.selectbox('Choose a numeric variable to display in the X axis', cat_dict.values(), key = 30)
        col23xdf = [k for k,v in cat_dict.items() if v == col23x][0]
        
        #creatig color input
        col21cdf = df['mother\'s_qualification']

        #check box for percent
        percent23 = None
        check23 = col23.checkbox('Check to display a normalized histogram', key = 31)
        if check23:
            percent23 = "percent"        

        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig12 = px.histogram(pd.melt(df, id_vars=[col23xdf], value_vars=['mother\'s_occupation', 'father\'s_occupation', 'mother\'s_qualification', 'father\'s_qualification']), x = col23xdf, color = 'value', barmode = 'group', color_discrete_sequence= my_colors,labels = all_col_dic, facet_col = 'variable', facet_col_wrap = 2, histnorm = percent23)
            fig12.update_traces(marker_line_width = 0.3)
            fig12.update_yaxes(matches=None)
            col24.plotly_chart(fig12)
    
    
    #graph 13
    st.markdown("### <b>Graph 14 (Pie chart): Target and 1 categorical variable</b>",unsafe_allow_html=True)
    col33,col34=st.columns([3,5])
    with st.form("### <b>Graph 14 (Pie chart): Target and 1 categorical variable</b>"):
        
        #creatig an input
        col33x = col33.selectbox('Choose a numeric variable', cat_dict.values(), key = 27)
        col33xdf = [k for k,v in cat_dict.items() if v == col33x][0]
        
        #creatig color input
        col33cdf = df['target']
            
        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig17 = px.pie(df, names = col33xdf, color = col33cdf, color_discrete_sequence= my_colors,labels = all_col_dic)
            col34.plotly_chart(fig17)


    #graph 14
    st.markdown("### <b>Graph 15 (Pie chart): Target and 1 numeric variable</b>",unsafe_allow_html=True)
    col35,col36=st.columns([3,5])
    with st.form("### <b>Graph 15 (Pie chart): Target and 1 numeric variable</b>"):
        
        #creatig an input
        col35x = col35.selectbox('Choose a numeric variable', num_dict.values(), key = 28)
        col35xdf = [k for k,v in num_dict.items() if v == col35x][0]
        
        #creatig color input
        col35cdf = df['target']

        #submite bottom
        submitted = st.form_submit_button("Submit to produce the Histogram")
        if submitted:
            fig18 = px.pie(df, names = col35xdf, color = col35cdf, color_discrete_sequence= my_colors,labels = all_col_dic)
            col36.plotly_chart(fig18)



#41


if selected == "Student background":
    st.title("Student background")
    st.header("Student's background analysis with different variables")
    
    st.subheader("Scholarship holder and martial status")
    col1,col2=st.columns([4,5])
    with st.form("Scholarship holder and martial status"):
        fig_8 = px.histogram(pd.melt(df, id_vars= ['curricular_units_2nd_sem_grade'], value_vars = ['marital_status', 'scholarship_holder']), x = 'curricular_units_2nd_sem_grade', color = 'value', barmode = 'group', facet_col = 'variable', labels = all_col_dic, nbins = 5, histnorm = 'percent', facet_col_wrap =2, title = 'Student\'s background information & Grade in sem 2')
        fig_8.update_traces(marker_line_width = 1)
        col2.plotly_chart(fig_8)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Scholarship holder: There were 95 students that does have scholarship gets 0 for their second semester grade; The qualification for scholarship is based on multiple requirement wasn’t only about the grade that student get, otherwise there are probably no scholarship awarded for students that gets scores from 10 -15 for their second semester grades ; The probability for student to get scholarship increases as the scores rises. Below the score level of 12.25 to 12.749, the number of scholarship holder compared to normal student was below 50%; but as student’s achieve a higher academic performances (getting scores that are mot than the level of 12.25to 12.749), then the percentage of the number of scholarship holder compared to normal students are more than 50%, at some situation, it even reaches 70%. For example, the score level of 15.75 to 16.246. ; For some reason, for the top scores, only top one have one scholarship holder, while there were only normal students for top 2 and 3.")
        col1.markdown(" ")
        col1.markdown("Marital status: Similar to the previous observation, as single people are the major marital status in the school, it also account for the most numbers of people getting different scores. In higher score range, like 17.25 to 17.74, married people is accounting for 50% of the number of students that are single")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        
    col1,col2=st.columns([4,5])
    with st.form("Histograme 9: Student's background information & Course"):
        fig_9 = px.histogram(pd.melt(df, id_vars= ['course'], value_vars = ['marital_status', 'scholarship_holder']), x = 'course', color = 'value', barmode = 'group', facet_col = 'variable', labels = all_col_dic, facet_col_wrap =2, title = 'Student\'s background information & Course')
        fig_9.update_traces(marker_line_width = 0.3)
        col2.plotly_chart(fig_9)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Scholarship holder: Except for nursing and social service courses, for all other courses, the number of scholarship holder in each course is always less than 50 percent; Scholarship especially favors nursing students; The number of scholarship holders are significantly low in agronomy, informatics engineering, and there were 0 scholarship holders in technologies courses that focus on biofuels; Students likes to major managements the most, but the number of scholarship holder in this course was very little, the quantity of scholarship holders is very similar to social service even though there was a huge gap between total number of people majoring managements and social service")
        col1.markdown(" ")
        col1.markdown("Summary: Based on the following features that I have pointed out, scholarship are not given to student’s proportionally in each major, it is given in a relatively random way. Therefore, the probability of a students that might be scholarship holder can’t be determined or predicted based on the number of students majoring different courses")
        col1.markdown(" ")
        col1.markdown("Marital status: Light blue bar consist of most people in all score range, they represent single people, or at least aren’t married. They favors Nursing and managements the most.The second large marital status group is married people, they also favors management and nursing, but they also like social services. Widower people like the same three subjects as married people did. ")
        
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
    st.subheader("Age at enrollment")
    col1,col2=st.columns([4,5])
    with st.form("Grade & age at enrollment & attendence time"):
       fig_1 = px.histogram(df, x = 'curricular_units_2nd_sem_grade', y = 'age_at_enrollment', color = 'daytime_evening_attendance', histfunc = 'avg', barmode = 'group', labels = all_col_dic, nbins = 5, title = 'Grade & age at enrollment & attendence time') 
       fig_1.update_traces(marker_line_width = 2)
       col2.plotly_chart(fig_1)
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown("There are three major feature in this graph: Firstly, the average of male student’s enrollments age are much more higher than average female student’s enrollment’s age; Secondly, people that are older, or have a higher average age at enrollment normally attend evening attendance (it may because they have a part time or a full time job in the morning); Thirdly, students that get the highest score in this graph is 18.25-18.74, their and age at enrollment is 18, which is very young.")
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown(" ")
    

    col1,col2=st.columns([4,5])
    with st.form("Histogram 2: Course & age at enrollment & marital status"):
       fig_2 = px.histogram(df, x = 'age_at_enrollment', y = 'course', color = 'marital_status', histfunc = 'avg', barmode = 'group', labels = all_col_dic, title = 'Course & age at enrollment & marital status')
       fig_2.update_traces(marker_line_width = 1)
       col2.plotly_chart(fig_2)
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown("Legally separated people like to attend social service type courses the most; Widower people especially favors managements and agronomy; Married people favors managements the most as well; Divorced people likes social services type of courses; Facto union people majors management type of courses the most; Single people favor the largest amount of courses, especially nursing.")
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown(" ")


    col1,col2=st.columns([4,5])
    with st.form("Histogram 3: Courses people in different age favors"):
       fig_3 = px.histogram(df, x = 'age_at_enrollment', color = 'course', histnorm = 'percent', barmode = 'group', labels = all_col_dic, nbins =5, title = 'Courses people in different age favors')
       fig_3.update_traces(marker_line_width = 1)
       col2.plotly_chart(fig_3)
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown(" ")
       col1.markdown("People who have an age of enrollment in 20-39 favors biofuel production of technology and managements a lot, which account for 100 percent and more than 80 percent; There were lesser people enrolled in collage as the age grows up; The age of 20-39 is the age that have the most people enrolled in college; For young people who have an age between 0-19, they especially favor journalism & communication and nursing; For older people who have an age around 49.5, they especially favor agronomy and managements. I think older people is more targeted when they are choosing courses while younger people tends to choose more broader course.")
    


if selected=="Parent’s background":
    st.title('Parent’s background')    
    
    col1,col2=st.columns([2,5])
    with st.form("Histograme 11: Parent's background & grades"):
        fig_11 = px.histogram(pd.melt(df, id_vars=['curricular_units_2nd_sem_grade'], value_vars=['mother\'s_occupation', 'father\'s_occupation', 'mother\'s_qualification', 'father\'s_qualification']), x = 'curricular_units_2nd_sem_grade', color = 'value', barmode = 'group', labels = all_col_dic, facet_col = 'variable', facet_col_wrap = 2, nbins = 5, histnorm = 'percent', title = 'Parent\'s background & grades')
        fig_11.update_traces(marker_line_width = 0.3)
        col2.plotly_chart(fig_11)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Mother's qualification': Based on the graph, the color that was the higher thought the graph was white, it represent mother’s who qualifies as commerce courses. No matter if the student is getting a high score or note, most of student’s mother’s qualification in each score level was commerce course. The second top mother’s qualification was light blue, it represent secondary education, it was always the second high mother’s qualification throughout each score level. The third top mother’s qualification was dark blue with a it green inside it, this color represent bachelor degree. In higher score range like 13.75 to 14.246, the number of student’s mother’s qualification of secondary education is increased, and was closer to the numbers of student’s mother’s qualification of commerce courses. Mother’s qualification’s of bachelor and commerce course is at the same education level (I separated them because there were lots of different type of commerce courses, and the numbers of people who have commerce course as their qualification was also a lot), while secondary education was significantly lower, compared to bachelor degrees. Thus, mother’s qualification, or their education level does not have a direct bond with student’s score, but it might have some influence, as mothers that are educated is still the top in quantity in different score level.")
        col1.markdown(" ")
        col1.markdown("Father's qualification: Different from mothers qualification, the top frequent father’s qualification that are displayed in the graph for students getting different score was primary education and secondary education, which was a relatively lower education level compared to mother’s qualification. There were only little percentage of father that have a qualification for a degree higher or equal to bachelor. There were not significant change for father’s qualification for student’s that are getting either higher or lower scores, there were only the top two frequent qualifications")
        col1.markdown(" ")
        col1.markdown("Mother's occupation: The number of mothers that have an occupation of intermediate level technicians and professions are the most for students getting different scores. Due to the significant different between the number of mothers that occupies in intermediate level technicians and professions compared to other occupations, there was also a significant difference in each score level between them. As the scores increases, lesser student in each score bands, numbers of mothers who occupies in personal service workers are increasing and is similar to numbers of mother occupies in intermediate level technicians and professions. To be more specific, it was in the score band of 16.75 to 17.249. ")
        col1.markdown(" ")
        col1.markdown("The situation and features in the graph of father’s occupation and 2nd Sem grade was pretty much the same with mother’s occupation. Except it have fathers occupies in administrative staff chasing after number of father’s occupies intermediate level technicians and professions in higher scores, rather than personal service workers. ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
    col1,col2=st.columns([2,5])
    with st.form("Histograme 12: Parent's background & result"):
        fig_112 = px.histogram(pd.melt(df, id_vars=['target'], value_vars=['mother\'s_occupation', 'father\'s_occupation', 'mother\'s_qualification', 'father\'s_qualification']), x = 'target', color = 'value', barmode = 'group', labels = all_col_dic, facet_col = 'variable', facet_col_wrap = 2, nbins = 5, histnorm = 'percent', title = 'Parent\'s background & final result')
        fig_112.update_traces(marker_line_width = 0.3)
        col2.plotly_chart(fig_112)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Mother’s occupation: In the drop out bar, the most frequently appear occupation was unskilled worker, which accounts for 75.6 percent in total. And then there was intermediate level technician and profession followed after unskilled worker column, and it accounts for 31 percent in total. The last two occupation for mother’s who have a kid that drop outs are administrative staff and personal service worker. It is quite special with the situation presented in this graph, there were only four occupation for mother’s presented, means that other occupation for mothers don’t have any kid that dropped out.")
        col1.markdown("In the graduate column, the occupation of specialist in different realm accounts for 71 percent here, it was closely followed by intermediate level technicians profession, personal service worker and armed forces professions, their corresponding percentages are 50.4, 49 and 52,9. Then there is unskilled worker and administrative staff at the bottom, accounting for a lower percentage. The graduated bar is still missing one occupation of unknown for mother’s occupation, but it includes all other occupation.")
        col1.markdown("In the enrolled column, it includes all the occupations for mothers in this bar. The only thing that was strange was the unknown occupation column is account for 100%, it also doesn’t appear in any of the graduated or drop out category.")
        col1.markdown(" ")
        col1.markdown("Father’s occupation: In the dropout bar, similar to mother’s occupation, father’s occupation of unskilled worker in accounting for the highest percent, 75. Then it was followed by administrative staff and intermediate level technicians and professions, which was accounting for 22 and 31 each. Different form mother’s occupation, there was a small percent of occupation of specialist in different realm appeared in the group out column.")
        col1.markdown("In the graduated bar, all the father’s that have a occupation of unknown have their kids graduated. There was personal service worker, armed forces professions, socialist in different realm, administrative staff and intermediate profession and technicians. Which  accounts for 62, 50 44, 44 and 50 percent separately. It have a smaller percent of unskilled worker and operated at the lower zone of the graph. ")
        col1.markdown("For enrolled column, father’s occupation of operators accounts for the highest percent, then there was specialist in different realm and armed forces profession followed after it. Father’s occupation of unskilled worker have a really low enrolled percentage in this graph.")
        col1.markdown(" ")
        col1.markdown("Mother’s qualification: In the drop out column, surprisingly, mother’s qualification of specialization courses and technical preprofessional courses have both dropped out for 100 percent. Then it was followed by lots of other qualification, it is’s mainly on one percentage level, except for mother’s qualification of Master, it was still in a rarely low percent, 16%.")
        col1.markdown("In the graduated bar, The qualification that accounts for the most percent was accounting and administrating, then it was followed by master. Their percentages are 58 and 53 percents. Except for doctorate, which accounts for the least percent in graduated bar, other ones was on the same or similar level of percentages. ")
        col1.markdown("In the enrolled bar, all the columns are in a fairly low zone, mother’s qualification of master, Bachelor and doctorate was on the lead. Their percentages are 30, 23, 24 percent. ")
        col1.markdown(" ")
        col1.markdown("The situation and features in the graph of father’s occupation and 2nd Sem grade was pretty much the same with mother’s occupation. Except it have fathers occupies in administrative staff chasing after number of father’s occupies intermediate level technicians and professions in higher scores, rather than personal service workers. ")
        col1.markdown(" ")
        col1.markdown("Father’s qualification: In the dropout column, there was a clear three level differences. For the top one, there are drop out for every single qualification, and there were three qualification that have 100 percent drop out, they are accepting and administrative, technical professional courses and commerce courses. For the middle one, there were qualifications of unknown, bachelor and doctorate, which accounts for 72, 60 and 57. For the lowest one, they are all the in the rand form 30 to 39 percent.")
        col1.markdown("In the graduated column, secondary education, primary education and master was on the lead, the percentages are 51, 51 and 48 percent. It was closely followed by Bachelor, which accounts for 40 percents. There was qualification of unknown, doctorate, and specialization courses in the similar level at a lower zone, they are around 25 to 26 percent.")
        col1.markdown("In the enrolled, column, similar to mother’s qualification, they are all in a relatively lower zone for father’s qualification as well. Father’s qualification of specialization courses and bachelor were exceptionally high, while all other qualification were at a similar level except for unknown qualification, it was really low. ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")

    

    col1,col2=st.columns([4,5])
    with st.form("Histogram 4: Courses people in different age favors"):
        fig_4 = px.histogram(df, x = 'mother\'s_qualification', color = 'course', histnorm = 'percent', barmode = 'group', labels = all_col_dic, facet_col = 'course', facet_col_wrap=3, height = 1000, width = 1800, facet_col_spacing = 0.15, title = 'Courses people in different age favors')
        fig_4.update_traces(marker_line_width = 0.1)
        col2.plotly_chart(fig_4)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Summaries: Their mother’s qualification may have influence towards the choice of the student’e major to a certain extent; There were lots of mother’s qualification was commerce courses, therefore, it donates literally every single source that the student majors; There was a huge difference between the number of students that major different courses.")
        col1.markdown(" ")
        col1.markdown("Features I observed: For student’s major management, over half of their mother’s qualification is commerce courses; For student’s major animation, the top 3 sources of their mother’s qualification was commerce course, Bachelor, and secondary education; For student’s major tourism, the top 2 qualification that their mother; For student’s major communication design, the top 2 qualification that their mother have was also secondary education and commerce course; For student’s major journalism, over half of their mother’s qualification is commerce courses; For student’s major social service, over half of their mother major commerce courses; For student’s major nursing, around 95percent of their mother’s qualification was commerce course, secondary education, accounting & administration and a Bachelor degree; For student’s major basic education, most of their mother’s qualification was ; For student’s major veterinary nursing, mother’s qualification of Bachelor starts to be slightly higher than accounting & administrating; For student’s major agriculture, the top three qualification for their mother was commerce courses, bachelor degree and secondary education (Bachelor degree was the top for this course); For student’s major agronomy, around 80 percent of their mother’s qualification was still the four qualification; For student’s major technology (biofuel), here were only three type of qualification for their mother, it was Bachelor, commerce courses, and administration & accounting, all of them were also in a very small number as well; For student’s major informatics engineering, the mother’s qualification of commerce courses and secondary education was on the lead.")








if selected=="Analysis of final result":
    st.title('Analysis of final result') 

    col1,col2=st.columns([4,5])
    with st.form("GDP & Grade & Result"):
        fig_5 = px.scatter(df, x = 'gdp', y = 'curricular_units_2nd_sem_grade', color = 'target', labels = all_col_dic, title = 'GDP & Grade & Result')
        fig_5.update_traces(marker_line_width = 1)
        col2.plotly_chart(fig_5)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("In the graph presented above, there were different column that were plot by the dotes in the graph, it represents different GDP level for the X axis. The length (height) of the line plates by the dotes were the 2nd semester grades for students. All the line starts around the level of 10, and all ends around 17 for their grades, doesn’t show any significant different. A note is that there were overlap between the dotes, therefore, the target (dropout, enrolled, graduate) was not accurate if only uses visual to measure. For summary, there were no major differences between student’s target, which is whether they dropout or not. Thus, proves that GDP is barely connected to student’s grades.")
        col1.markdown(" ")
        col1.markdown("People major different courses when the local unemployment rate changes. Based on my observation for the courses that were favors by student living in a relatively higher unemployment area and low unemployment area: People living in a relatively low unemployment area tends to favors entertainments fields, or areas that might not help them to earn lots of money; People living in a relatively higher unemployment area tends to major courses that normally involve a lot of unique skills and specialties in a certain area.")
        col1.markdown(" ")
        col1.markdown("Detail features: For areas that have a relatively low unemployment rate, the top majors for students are animation & multimedia design; tourism; communication design; journalism and communication; social service; managements; basic education; veterinary nursing; agriculture; and information engineering; For areas that have a relatively higher unemployment rate, the top courses for students are Nursing, agronomy technologies (biofuel).")

        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")  
    col1,col2=st.columns([4,5])
    with st.form("Histograme 6_1: Result & Grade in sem 1"):
        fig_6 = px.histogram(df, x = 'curricular_units_1st_sem_grade', color = 'target', barmode = 'group', labels = all_col_dic, histnorm = 'percent', nbins = 5, title = 'Result & Grade in sem 1')
        fig_6.update_traces(marker_line_width = 3)
        col2.plotly_chart(fig_6)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("People that successfully graduated gets the most score; Dropout student overall score counts was higher than enrolled students; This graph presents a standards in terms of score for student to graduates; It was the same with first semester grades, people who successfully graduated gets the highest score.")

        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")

    col1,col2=st.columns([4,5])
    with st.form("Histograme 6_2: Result & Grade in sem 2"):
        fig6_2 = px.histogram(df, x = 'curricular_units_2nd_sem_grade', color = 'target', barmode = 'group', labels = all_col_dic, histnorm = 'percent', nbins = 5, title = 'Result & Grade in sem 2')
        fig6_2.update_traces(marker_line_width = 3)
        col2.plotly_chart(fig6_2)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Dropout students get 0 as their sec semester grade the most. Surprisingly, there were 75 people that graduated also gets 0 as their second semester grade. Graduated student get the highest score, or have the most student in higher scores compared to group outs and enrolled student’s, for instance, from 11.25-11.749 to 16.75-17.249. The number of student enrolled or dropout are similar in every score level except for 0.")

    
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")    
    col1,col2=st.columns([4,5])
    with st.form("Histograme 7: Result & marital status"):
        fig_7 = px.histogram(df, x = 'marital_status', color = 'target', barmode = 'group', labels = all_col_dic, title = 'Result & marital status')
        fig_7.update_traces(marker_line_width = 3)
        col2.plotly_chart(fig_7)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("Single is the group that includes the most people among all the category in marital status; Single people are also the only one that have this much graduates in this single group / have the largest different between either enrolled or dropouts; On the contrary, for married and divorced people, they all have more dropout than graduated; In literally all the group, enrolled is the smallest category in target")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        
    st.subheader("Pie charts")
    col1,col2=st.columns([4,5])
    with st.form("pie: Target and marital status"):
        pie1 = px.pie(df, names = 'marital_status', color = 'target', labels = all_col_dic, title = 'Target & marital status')
        col2.plotly_chart(pie1)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown("There were 88.6 percent of single people dropout; There are 8.57% of married people graduated; 2.06% of divorced people graduated; 0.565% of divorced people graduated; 0.136% of facto union dropouts; 0.09% of widower enrolled.")
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(" ")
        
    with st.form("pie: Target and grade"):
        pie2 = px.pie(df, names = 'curricular_units_2nd_sem_grade', color = 'target',labels = all_col_dic, title = 'Target & grade')
        col2.plotly_chart(pie2)



    
 

    
    
    
if selected=="Conclusion":
    st.title("Conclusion")
    
    st.markdown("For student’s background analysis:")
    st.markdown("The analysis of student backgrounds indicates that scholarships are more frequently awarded to higher-performing students and unevenly distributed across different majors, with a notable emphasis on Nursing students. Despite high enrollment in Management programs, scholarship holders in these courses are relatively few, suggesting a somewhat random allocation process. Marital status plays a significant role in academic performance and course preferences, with single students making up the majority and favoring Nursing and Management, while married and widowed students also show interest in these fields alongside Social Services. Legally separated and divorced individuals lean towards Social Services. Age at enrollment reveals that older students, who often attend evening classes due to work commitments, are more targeted and specific in their course selection, particularly favoring Biofuel Technology and Management. Younger students tend to enroll in a broader range of courses, especially Journalism & Communication and Nursing. High-scoring students typically enroll at a younger age, around 18. This analysis underscores the complex factors influencing scholarship distribution, course preferences, and academic success among students based on age and marital status.")
    st.markdown("")
    st.markdown("For parents background analysis:")
    st.markdown("The graph shows that the top three qualifications of a mother are commerce courses, secondary education, and bachelor degrees. These qualifications are at the same education level, but secondary education is significantly lower than bachelor degrees. Mothers' qualifications do not have a direct bond with students' scores, but they might have some influence. Father's qualifications are displayed differently, with primary education and secondary education being the most frequent for students getting different scores. There were only a few percentages of fathers with a degree higher or equal to bachelor's. The situation and features in the graph of father's occupation and 2nd Sem grade were similar with mother's occupation, except fathers were in administrative staff chasing after intermediate level technicians and professions in higher scores.")
    st.markdown("")
    st.markdown("In the dropout bar, unskilled workers account for 75.6% of mothers' occupations, followed by intermediate level technicians and professions, administrative staff, and personal service workers. The last two occupations for mothers who have a kid that drop out are administrative staff and personal service workers. In the graduate bar, the occupation of specialists in different realm accounts for 71%, followed by intermediate level technicians, personal service worker, and armed forces professions. The graduated bar still missing one occupation of unknown for mother's occupation, but it includes all other occupations.")
    st.markdown("")
    st.markdown("In the enrolled column, father's occupation of operators accounts for the highest percent, followed by specialists in different realm and armed forces professions. Unknown occupations have a very low enrolled percentage in this graph.")
    st.markdown("")
    st.markdown("Mother's qualifications drop out for 100% in the dropout column, with specialization courses and technical preprofessional courses dropping out for 100%. Accounting and administrating account for the most percent, followed by master's and doctorate. In the enrolled bar, all columns are in a fairly low zone, with master's, bachelor's, and doctorate qualifications on the lead. The situation and features in the graph of father's occupation and 2nd Sem grade were similar with mother's occupation, except fathers were in administrative staff chasing after intermediate level technicians and professions in higher scores.")
    st.markdown("")
    st.markdown("For causes that different mother’s factor interns of their qualification, I found that mother’s qualification may have influence towards the choice of the student’e major to a certain extent; There were lots of mother’s qualification was commerce courses, therefore, it donates literally every single source that the student majors; There was a huge difference between the number of students that major different courses.")
    st.markdown("")
    st.markdown("For Target analysis:")
    st.markdown("The graph presented shows that GDP is barely connected to student's grades, with no significant differences between students' targets, such as dropout or not. Students in areas with higher and lower unemployment rates tend to major in courses that involve unique skills and specialties. For areas with low unemployment rates, top majors include animation & multimedia design, tourism, communication design, journalism and communication, social service, managements, basic education, veterinary nursing, agriculture, and information engineering. For areas with higher unemployment rates, top majors include nursing and agronomy technologies (biofuel). Successfully graduated students receive the highest scores, while dropout students receive the lowest scores. Single people have the most graduates among all marital status categories, with the largest difference between enrolled and dropouts. In all groups, enrolled is the smallest category in target. The graph also reveals that students in areas with low unemployment tend to major in fields like entertainment, while those in areas with high unemployment tend to major in fields like nursing and agronomy technologies.")

    
    
if selected=="Bibliography":
    st.title("Bibliography")
    st.markdown("[1]“Predict Students’ Dropout and Academic Success.” Kaggle, Kaggle, www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention. Accessed 18 June 2024.")
    st.markdown("[2]Shahari, Priya. “Predicting Students’ Dropout and Academic Success.” Medium, Medium, 3 Dec. 2023, medium.com/@shaharipriya.nandlal/predicting-students-dropout-and-academic-success-cfc9d39e8e04.")
    st.markdown("[3]K-12 Education K-12 Education                                                                                                                        . “What Are the Most Common Reasons Students Drop out of School?” Common Reasons Students Drop Out of School, linkin, www.linkedin.com/advice/1/what-most-common-reasons-students-drop-out-school-xfcxc. Accessed 18 June 2024.")
    st.markdown("[4]“What Are the Factors That Influence a Student’s Decision to Drop out of School? | 5 Answers from Research Papers.” Typeset, scispace, typeset.io/questions/what-are-the-factors-that-influence-a-student-s-decision-to-4yohfkxax9. Accessed 18 June 2024.")
    st.markdown("[5]Norwegian University of Science and Technology. “Education Saves Lives across All Demographics, Study Reveals.” News, News, 24 Jan. 2024, www.news-medical.net/news/20240123/Education-saves-lives-across-all-demographics-study-reveals.aspx.")
    st.markdown("[6]OECD. “Site Homepage.” OECD iLibrary, OECD iLibrary, www.oecd-ilibrary.org/. Accessed 18 June 2024.")
    st.markdown("[7]“How Effective Education Spending Can Reduce Poverty and Boost Earnings.” World Bank Blogs, World Bank Blogs, blogs.worldbank.org/en/education/How-effective-education-spending-can-reduce-poverty-and-boost-earnings. Accessed 18 June 2024.")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
















