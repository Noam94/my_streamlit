import seaborn as sns
import streamlit as st
import pandas as pd


st.write("""
# My first app
Hello *world!*
""")

df = sns.load_dataset('dowjones')
df = df.set_index("Date")
print(df)
st.line_chart(df)
