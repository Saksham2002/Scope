import streamlit as st
import streamlit.components.v1 as components
from pyecharts import options as opts
import numpy as np
import pandas as pd
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.area_chart(chart_data)