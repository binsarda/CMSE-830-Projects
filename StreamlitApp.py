import pandas as pd
import streamlit as st
import plotly.express as px

heartdisease=pd.read_csv("heartdisease.csv")
lungcancer=pd.read_csv("lungcancer.csv")
stroke=pd.read_csv("stroke.csv")
##print("Panda dataframe is given below-")
#print(p_df.head(7));
#cols=p_df.columns;
#print(f"No. of columns are {len(cols)} and name of the columns are given below-\n{cols}")

##intro to streamlit
st.markdown("*Welcome to my website!!!!*")
st.write("Owner Name: Sardar Nafis Bin Ali")
st.write("Institution: Michigan State University")
##taking some basic functions
visitor_name=st.text_input("Enter your name:"," ");
st.write("Thank you",visitor_name,", for visiting my website.")
st.markdown("*Here you can find datasets related to serious diseases.*")
st.write("There are 3 datsets-")
st.markdown("***")
st.write("1. Heart Disease")
st.markdown("***")
st.write("2.Lungs Cancer")
st.markdown("***")
st.write("3.Brain Stroke")
st.markdown("***")

data_button=st.selectbox('Please select one dataset from the following:',['Heart Disease','Lungs Cancer','Brain Stroke'])

if data_button=='Heart Disease':
    df1=heartdisease
    st.write("You have selected 'Heart Disease' Dataset")
elif data_button=='Lungs Cancer':
    df1 = lungcancer
    st.write("You have selected 'Lungs Cancer' Dataset")
elif data_button == 'Brain Stroke':
    df1 = stroke
    st.write("You have selected 'Brain Stroke' Dataset")
st.write(df1.head(12))
df=df1;

button=st.radio('Do you want to delete any row having NaN in at least one of the fields', ['No', 'Yes'])
if button=='Yes':
    df.dropna();
    st.write("You deleted rows having NaN in at least one of the fields")
elif button=='No':
    df = df1;

button1=st.button("Show Statistics");
if button1:
    st.write(df.describe())
if st.button("Hide Statistics"):
    button1=False

cols=df.columns
red_df=df.iloc[:,0:6]
red_cols=red_df.columns
button2=st.button("Show Columns");
if button2:
    st.write("No. of columns are ",len(cols))
    st.write("The columns are following-")
    st.write(df.columns)
if st.button("Hide Columns"):
    button2=False
st.write("Please select following variables for different plotting")
xv=st.selectbox('Please select x or first variable:',cols)
yv=st.selectbox('Please select y or second variiable:',cols)
zv=st.selectbox('Please select hue or third variiable:',red_cols)

button3=st.button("Bar Chart");
if button3:
    st.bar_chart(data=df, x=xv, y=yv)

if st.button("Hide Bar Chart"):
    button3=False

heatmap_fig = px.density_heatmap(df, x=xv, y=yv,marginal_x="histogram", marginal_y="histogram")
st.plotly_chart(heatmap_fig, theme=None)
st.write("Done until this!!!")
