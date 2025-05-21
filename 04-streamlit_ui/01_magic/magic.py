# Magic
# Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will appear in your app.


import streamlit as st
import pandas as pd
import numpy as np



df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["a", "b"],
)
st.write(df)
st.write("This is a magic command")


x: int = 100
'x', x
st.write("This is a magic command with a variable")

import matplotlib.pyplot as plt


abc = np.random.normal(size=(100, 2))
flg , ax = plt.subplots()
ax.scatter(abc[:, 0], abc[:, 1])


st.pyplot(flg)
st.write("This is a magic command with a plot")



