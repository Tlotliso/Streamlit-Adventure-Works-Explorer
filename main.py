import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sb
import matplotlib.pyplot as plt

#data
df_HR = pd.read_csv('main.csv')
df_HR.Gender.value_counts()

#creating departments dataframe for analysis
departments = df_HR.groupby('DepartmentID').mean().sort_values(
    by = 'Rate', ascending=False)
departments = departments.filter(['DepartmentID','Rate'])

#creating genders dataframe to analyse gender data
genders = df_HR.groupby('Gender').mean()
genders = genders.filter(['Gender','Rate'])

#creating dataframe to analyse vacation hours
vac = df_HR.groupby('Gender').mean()
vac = vac.filter(['VacationHours'])


#creating containers for the dashboard
header = st.container()
univariate = st.container()
bivariate = st.container()
multivariate = st.container()
conclusions = st.container()

with header:
    st.title('Adventure Works 2019 dataset')
    st.markdown('- The adventure works database is a database of a fictitious multinational company called Adventure Works Cycles. The database is made by Microsoft. I will be analyzing the HR data in this database to draw insights on the employees at Adventure Works.')
    

with univariate:
    st.header('Univariate exploration')
    st.markdown('**Question: How many men and women work for adventure works, is there more employees of one gender?**')
    fig = px.histogram(df_HR, x='Gender', title='Count of Men and Women working for Adventure Works')
    st.plotly_chart(fig)
    st.markdown('From the graph above I have noted that there are more men working at Adventure works than women, 237 men work at Adventure works while 97 women work at Adventure works.')

    st.markdown('**Question: Which departments are paid the highest?**')
    fig = px.bar(departments, title='Plot of Average Rate per hour per department', labels={'DepartmentID':'Department', 'value':'Rate per hour ($)'})
    st.plotly_chart(fig)
    st.markdown('From the graph above I noted that the departments with the highest rate per hour are Executives and Research and Development, while the 2 departments with the lowest rate per hour Facilities and Maintenance and Shipping and Recievinng ')

    st.markdown('**Question: What is the average pay per gender?**')
    fig = px.bar(genders, title='Plot of Average Rate per hour per Gender', labels={ 'value':'Rate per hour ($)'})
    st.plotly_chart(fig)
    st.markdown('**The average rate per hour:**  for women is about \$20 per & for men is about \$17.5 per hour.')

    st.markdown('**Question: Is there descrapency with regards to vacation hours given to each gender?**`')
    fig = px.bar(vac, title='Plot of Average vacation hours per Gender', labels={ 'value':'Vacation hours'})
    st.plotly_chart(fig)
    st.markdown('* Vacation hours dont differ between male and female employees.')


with bivariate:
    st.header('Bivariate exploration')
    st.markdown('**What is the relationship between Vacation Hours and Hourly Rate**')
    fig = px.scatter(df_HR, x = 'VacationHours', y = 'Rate', labels={'VacationHours':'Vacation Hours'},title='Scatter plot of Rate and Vacation Hours')
    st.plotly_chart(fig)
    st.markdown('From the scatter plot above there is no clear relationship between the vacation hours and hourly rate. Vacation hours differ from in different rate per hour ranges.')


with multivariate   :
    st.header('Multivariate exploration')
    st.markdown('What is the relationship between rate per hour and number of available Vacation Hours for men and women?')
    fig = px.scatter(df_HR, x = 'VacationHours', y = 'Rate', color='Gender', labels={'VacationHours':'Vacation Hours'},title='Scatter plot of Rate and Vacation Hours')
    st.plotly_chart(fig)
    st.markdown('From the scatter plot above there is no clear relationship between the vacation hours and hourly rate for men and women. Vacation hours differ from in different rate per hour ranges.')

with conclusions:
    st.header('Conclusions')
    st.markdown('* There are more men working for Adventure works than woman.')
    st.markdown('* The production department is the department with the most employees with 180 employees.')
    st.markdown('* The highest paying departments are Executives, Research and Development and Information systems')
    st.markdown('* The lowest paying departments are Shippping and recieving, Facilities and Engineering and Production')
    st.markdown('* The avearage rate per hour for women is \\$20 and the average rate per hour for men is \\$17.5')
    st.markdown('* Vacation hours differ in different income ranges, with some employees in a certain range having considerably more vacation hours than other employees')




