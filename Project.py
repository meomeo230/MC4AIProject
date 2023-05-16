import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#df_database = pd.read_csv("./data/data_BuLi_13_20_cleaned.csv")

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text('Giới tính')
        check = st.checkbox('Nam')
        check1 = st.checkbox('Nữ')
        
    with col2:
        radio = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', 'Lớp 12'), horizontal=False)
        
    with col3:
        option = st.selectbox('Phòng', ('Tất cả', 'A114', 'A115'))
        
    with col4:
        options = st.multiselect('Buổi', ('Sáng', 'Chiều'))

    st.text('Lớp chuyên')

#if st.button('OK'):

with tab2:
    tab5, tab6 = st.tabs(["Số lượng HS", "Điểm"])
    #with tab5:
        
    with tab6:
        radio1 = st.radio('Điểm từng Session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
with tab3:
    slider = st.slider('Số nhóm', 2, 5, 3)
    
with tab4:
    radio2 = st.radio('Số đặc trưng', ('2', '3'), horizontal=True)

  
