import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#df_database = pd.read_csv("./data/data_BuLi_13_20_cleaned.csv")

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('Giới tính')
        check = st.checkbox('Nam', value=True)
        check1 = st.checkbox('Nữ', value=True)
        
    with col2:
        radio = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', 'Lớp 12'), horizontal=False)
        
    with col3:
        option = st.selectbox('Phòng', ('Tất cả', 'A114', 'A115'))
        
    with col4:
        options = st.multiselect('Buổi', ('Sáng', 'Chiều'))

    st.write('Lớp chuyên')
    co1, co2, co3, co4, co5 = st.columns(5)
    with co1:
        k1 = st.checkbox('Văn', value=True)
        k2 = st.checkbox('Toán', value=True)
        
    with co2:
        k3 = st.checkbox('Lý', value=True)
        k4 = st.checkbox('Hóa', value=True)
        
    with co3:
        k5 = st.checkbox('Anh', value=True)
        k6 = st.checkbox('Tin', value=True)
        
    with co4:
        k7 = st.checkbox('Sử Địa', value=True)
        k8 = st.checkbox('Trung Nhật', value=True)
        
    with co5:
        k9 = st.checkbox('TH/SN', value=True)
        k0 = st.checkbox('Khác', value=True)
    st.write('Số HS:', 61)

with tab2:
    tab5, tab6 = st.tabs(["Số lượng HS", "Điểm"])
    #with tab5:
        
    with tab6:
        radio1 = st.radio('Điểm từng Session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
with tab3:
    slider = st.slider('Số nhóm', 2, 5, 3)
    
with tab4:
    radio2 = st.radio('Số đặc trưng', ('2', '3'), horizontal=True)

  
