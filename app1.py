import streamlit as st
import pandas as pd

st.write(" My first app Hello Mohan")

df = pd,read_csv("E:\NareshIT\Projects\KaggleProjects\movelens-20m-datase\genome_scores.csv")
st.line_chart(df)