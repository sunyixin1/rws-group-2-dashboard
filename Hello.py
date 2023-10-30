import streamlit as st
from PIL import Image
tab1, tab2 = st.tabs(["Data Cleaning", "Nearest Node"])
with tab1:
    st.header("Data Cleaning")
    st.markdown("In this section, we will introduce the steps and methods of data cleaning.")
    st.subheader("Details of Data Cleaning")
    st.markdown("HTML Content:123", unsafe_allow_html=True)
    with open("map123.html", "r", encoding="utf-8") as f:
        map1_html = f.read()
        st.components.v1.html(map1_html, height=300)
    st.markdown("More information about data cleaning.")

with tab2:
    st.header("Data washing")
    st.markdown("In this section, we will introduce the steps and methods of data cleaning.")
    st.subheader("Details of Data Cleaning")
    st.markdown("HTML Content:123", unsafe_allow_html=True)
    with open("map123.html", "r", encoding="utf-8") as f:
        map1_html = f.read()
        st.components.v1.html(map1_html, height=300)
    st.markdown("More information about data cleaning.")
