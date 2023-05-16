import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
from sklearn.cluster import KMeans


df = pd.read_csv("https://raw.githubusercontent.com/meomeo230/MC4AIProject/main/score.csv")

df['BONUS'].fillna(0, inplace=True)
df['S1'].fillna(0, inplace=True)
df['S2'].fillna(0, inplace=True)
df['S3'].fillna(0, inplace=True)
df['S4'].fillna(0, inplace=True)
df['S5'].fillna(0, inplace=True)
df['S6'].fillna(0, inplace=True)
df['S7'].fillna(0, inplace=True)
df['S8'].fillna(0, inplace=True)
df['S9'].fillna(0, inplace=True)
df['S10'].fillna(0, inplace=True)
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

def calculate3(row):
  if row['PYTHON-CLASS'].find("114") !=-1:
    return '114'
  else:
    return '115' 
df['Phòng học'] = df.apply(calculate3, axis=1)

def calculate2(row):
  if row['PYTHON-CLASS'].find("S") !=-1:
    return 'Sáng'
  else:
    return 'Chiều' 
df['Buổi học'] = df.apply(calculate2, axis=1)

def calculate4(row):
  if row['CLASS-GROUP'] =='Khác':
    return 'Thường'
  else:
    return 'Chuyên'
df['Loại lớp'] = df.apply(calculate4, axis=1)

#Phân loại học sinh khối:
def calculate5(row):
  if row['CLASS'].find("10") !=-1:
    return 'Khối 10'
  else:
    return 'Khối 11&12' 
df['Khối lớp'] = df.apply(calculate5, axis=1)

def calculate1(row):
  if row['GPA'] >=5:
    return 'Y'
  else:
    return 'N'
df['LEN LOP'] = df.apply(calculate1, axis=1)

st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        a = st.radio('Giới tính', ('Nam', 'Nữ'), horizontal=False)
        if a == 'Nam':
          df[(df['GENDER'] == "M")]
        else:
          df[(df['GENDER'] == "F")]
          
    with col2:
        b = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', 'Lớp 12'), horizontal=False)
        if b == 'Lớp 10':
          df[(df['CLASS'].str.contains('10'))]
        elif b == 'Lớp 11':
          df[(df['CLASS'].str.contains('11'))]
        elif b == 'Lớp 12':
          df[(df['CLASS'].str.contains('12'))]
        else: 
          df
          
    with col3:
        c = st.radio('Phòng', ('Tất cả', 'A114', 'A115'), horizontal=False)
        if c == 'A114':
          df[df['PYTHON-CLASS'].str.startswith('114')]
        elif c == 'A115':
          df[df['PYTHON-CLASS'].str.startswith('115')]
        else:
          df
          
    with col4:
        d = st.radio('Buổi', ('Sáng', 'Chiều'))
        if d == 'Sáng':
          df[(df['PYTHON-CLASS'].str.endswith('S'))]
        elif d == 'Chiều':
          df[(df['PYTHON-CLASS'].str.endswith('C'))]
        else:
          df
    
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
    with tab5:
        st.subheader('Tỉ lệ học sinh học sáng chiều')
        f1 = px.pie(df, names='Buổi học')
        st.write(f1)

        st.subheader('Tỉ lệ học sinh học phòng học')
        f2 = px.pie(df, names='Phòng học')
        st.write(f2)

        st.subheader('Tỉ lệ giới tính')
        f3 = px.pie(df, names='GENDER')
        st.write(f3)

        st.subheader('Tỉ lệ khối lớp')
        f4 = px.pie(df, names='Khối lớp')
        st.write(f4)

        st.subheader('Tỉ lệ các lớp')
        f5 = px.pie(df, names='CLASS-GROUP')
        st.write(f5)

        st.subheader('Tỉ lệ mong muốn được lên lớp')
        f6 = px.pie(df, names='REG-MC4AI')
        st.write(f6)

        st.subheader('Tỉ lệ học sinh được lên lớp')
        f7 = px.pie(df, names='LEN LOP')
        st.write(f7)

        st.subheader('Tỉ lệ học sinh chuyên và thường')
        f8 = px.pie(df, names='Loại lớp')
        st.write(f8)
    with tab6:
        radio1 = st.radio('Điểm từng Session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
with tab3:
    slider = st.slider('Số nhóm', 2, 5, 3)
    def average(row):
      return (row['S1']+row['S2']+row['S3']+row['S4']+row['S5']+row['S7']+row['S8']+row['S9'])/8
    df['HW-AVG'] = df.apply(average, axis=1)
    X = df[['GPA', 'HW-AVG']].values
    def xetnhom(aa):
      kmeans = KMeans(n_clusters=aa, n_init='auto')
      kmeans.fit(X)
      kmeans.labels_
    def draw1():
      plt.figure(figsize=(4,4))
      plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
      plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1])
      plt.show()
      
    xetnhom(slider)
    draw1()

with tab4:
    radio2 = st.radio('Số đặc trưng', ('2', '3'), horizontal=True)
    model = LinearRegression()
    x1=df['GPA'].values
    y1=df['HW-AVG'].values
    x1 = x1.reshape(-1,1)

    model.fit(x1, y1)
#print("weights", model.coef_)
#print("bias", model.intercept_)

    x_line = np.array([0, 10]).reshape(-1,1)
    y_line = model.predict(x_line)

    plt.scatter(x1, y1)
# plt.scatter(x_new, y_new)
    plt.plot(x_line, y_line, c='y')
    plt.xlabel('GPA')
    plt.ylabel('HW-AVG')
    plt.show()

#3 đặc trưng

    X2 = df[['S6', 'S10']].values
    y2 = df['HW-AVG'].values

    model=LinearRegression()
    model.fit(X2,y2)

    x3 = np.linspace(0, 10,100 )
    y3 = np.linspace(0, 10, 100)
    xx, yy = np.meshgrid(x3, y3)
    xy = np.c_[xx.ravel(), yy.ravel()]
    z=model.predict(xy)
    z=z.reshape(xx.shape)
    fig = go.Figure(data=[go.Scatter3d(x=df['S6'], y=df['S10'], z=df['HW-AVG'], mode='markers'),
                         go.Surface(x=x3, y=y3, z=z)])
    st.write(fig)
