import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

with tab1:
    check = st.checkbox('Giới tính', ('Nam', 'Nữ'), horizontal=False)
    radio = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', 'Lớp 12'), horizontal=False)

    option = st.selectbox('Phòng', ('Tất cả', 'A114', 'A115'))
    options = st.multiselect('Buổi', ('Sáng', 'Chiều'))

if st.button('OK'):

with tab2:
    st.header("A dog")

with tab3:
    st.header("An owl")
    
with tab4:
    st.header("An owl")

  
