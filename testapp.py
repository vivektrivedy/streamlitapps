import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("***Welcome*** to Learning Streamlit")
st.subheader("Hi I'm **:blue[Vivek]**!  I'm  PhD student at :red[Temple University] studying\
    computer science.  Welcome to my streamlit app! :sunglasses:")

if st.button("Say hello"):
    st.write("Why hello there")
elif st.button("Or don't..."):
    st.write("Goodbye!")
    
## Create a simple altair line chart with random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.markdown("Here's a simple line chart", help='this is help')
st.line_chart(chart_data)

## Create a simple altair bar chart with new random data
st.markdown("Here's a simple bar chart")
bar_data = pd.DataFrame(
    np.random.randn(10,3),
    columns=['a', 'b', 'c']
)
st.bar_chart(bar_data)

# Write a simple code block for a function that multiplies
# two numpy matrices
st.markdown("Here's a simple code block")
code = """
def matrix_multiply(a, b):
    return np.dot(a, b)
"""
st.code(code, language='python')
    