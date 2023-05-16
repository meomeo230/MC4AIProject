import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/meomeo230/MC4AIProject/main/score.csv")

df.dropna(subset=['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'BONUS'], inplace=True)
df['REG-MC4AI'].fillna('N', inplace=True)

def calculate(row):
  if row['CLASS'].find("CV") !=-1:
    return 'Chuyên Văn' 
  elif (row['CLASS'].find("CT") !=-1) & (row['CLASS'].find("CTIN") ==-1):
    return 'Chuyên Toán'
  elif row['CLASS'].find("CL") !=-1:
    return 'Chuyên Lý' 
  elif row['CLASS'].find("CH") !=-1:
    return 'Chuyên Hóa' 
  elif row['CLASS'].find("CA") !=-1:
    return 'Chuyên Anh'
  elif (row['CLASS'].find("CT") !=-1) & (row['CLASS'].find("CTIN") !=-1):
    return 'Chuyên Tin'
  elif row['CLASS'].find("CTRN") !=-1:
    return 'Trung Nhật'
  elif row['CLASS'].find("CSD") !=-1:
    return 'Sử Địa'
  elif (row['CLASS'].find("TH") !=-1) | (row['CLASS'].find("SN") !=-1):
    return 'Tích Hợp/Song Ngữ'
  else: 
    return 'Khác'
df['CLASS-GROUP'] = df.apply(calculate, axis=1)

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        a = st.radio('Giới tính', ('Nam', 'Nữ'), horizontal=False)
        if a == 'Nam':
          df[(df["GENDER"] == "M")]
        else:
          df[(df["GENDER"] == "F")]
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
    st.write('Số HS:', 61, '(41 nam, 20 nữ)')
    st.write('GPA: cao nhất', 10.0, 'thấp nhất', 1.8, 'trung bình', 6.8)

with tab2:
    tab5, tab6 = st.tabs(["Số lượng HS", "Điểm"])
    #with tab5:
        
    with tab6:
        radio1 = st.radio('Điểm từng Session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
with tab3:
    slider = st.slider('Số nhóm', 2, 5, 3)
    
with tab4:
    radio2 = st.radio('Số đặc trưng', ('2', '3'), horizontal=True)

  
