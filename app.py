import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide')
from PIL import Image


def main():
    st.title("Factors affecting student performance in school")
    @st.cache
    def data_reader():
        df = pd.read_csv('student_data.csv')
        return df
    df = data_reader()

    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Data', 'EDA'], 
            icons=['house', 'file-spreadsheet', 'bar-chart-line'], menu_icon="cast", default_index=0)

    if selected == 'Home':
        st.subheader("There number of factors affecting stuent performance in school")
        st.write("Students' academic performance is affected by several factors which include students' learning skills, parental background, peer influence, teachers' quality, learning infrastructure among others.")
        ## importing image
        student_img = Image.open("student.jpg")
        st.image(student_img, caption='Student during data science hackathon')
    

    elif selected == 'Data':
        st.subheader('Student Dataset')
        st.write(df)

    elif selected == 'EDA':
        st.subheader("Visualizations for Insight generation")
        school_list = ['All','GP', "MS"]
        school_selector = st.selectbox('Select School', school_list)

        gender_col, address_col, inter_col, rom_col = st.columns(4)

        if school_selector == 'All':
            df1 = df
        elif school_selector == 'GP':
            df1 = df[df['school']=='GP']
        else:
             df1 = df[df['school']=='MS']
        with gender_col:
            def gender_donut():
                df2 = df1.groupby(['Gender'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='Gender', names=df2.index, title='Number of students', hole=0.5, template='ggplot2')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "Total Sales by Region", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            gender_donut()
        
        with address_col:
            def address_donut():
                df2 = df1.groupby(['address'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='address', names=df2.index, title='Number of students', hole=0.5, template='seaborn')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "addrees", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            address_donut()

        with inter_col:
            def inter_donut():
                df2 = df1.groupby(['internet'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='internet', names=df2.index, title='Number of students', hole=0.5, template='plotly')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "Intenet access", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            inter_donut()
        
        with rom_col:
            def rom_donut():
                df2 = df1.groupby(['romantic'])[['Gender', 'address', 'internet',	'romantic' ]].count()
                fig = px.pie(df2, values='romantic', names=df2.index, title='Number of students', hole=0.5, template='ggplot2')
                fig.update_traces(textinfo = 'percent + value', textfont_size=15)
                fig.update_layout(title_text = "In romantic relationship", title_x = 0.5)
                fig.update_layout(legend = dict(
                    orientation = 'h', 
                    yanchor = 'bottom', 
                    y = -0.1, 
                    xanchor = 'center', 
                    x = 0.5
                ))
                st.plotly_chart(fig, use_container_width=True)
            rom_donut()
        
        st.markdown("<h3 style='text-align: center;  margin: 3px'>Performance in Exam 1 and Examp 2</h1>", unsafe_allow_html=True)
        school_list_1 = ['All','GP', "MS"]
        school_selector_1 = st.selectbox('Select School', school_list_1, key='dist')
        if school_selector_1 == 'All':
            df3 = df
        elif school_selector_1 == 'GP':
            df3 = df[df['school']=='GP']
        else:
             df3 = df[df['school']=='MS']
        exam1_col, exam2_col = st.columns(2)

        with exam1_col:
            def exam1_box():
                fig = px.box(df3, x='Gender', y='Exam1_score', color='internet', template='ggplot2')
                fig.update_layout(title_text = "Exam 1 Performance", title_x = 0.5)
                # fig.update_layout(legend = dict(
                #     orientation = 'h', 
                #     yanchor = 'bottom', 
                #     y = -0.1, 
                #     xanchor = 'center', 
                #     x = 0.5
                st.plotly_chart(fig, use_container_width=True)
            exam1_box()
        with exam2_col:
            def exam2_box():
                fig = px.box(df3, x='Gender', y='Exam2_score', color='internet', template='ggplot2')
                fig.update_layout(title_text = "Exam 2 Performance", title_x = 0.5)
                # fig.update_layout(legend = dict(
                #     orientation = 'h', 
                #     yanchor = 'bottom', 
                #     y = -0.1, 
                #     xanchor = 'center', 
                #     x = 0.5
                st.plotly_chart(fig, use_container_width=True)
            exam2_box()

        

        




if __name__ == '__main__':
    main()