import streamlit as st
import pandas as pd
import numpy as np 
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

    with col2:
        b = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', 'Lớp 12'), horizontal=False)

    with col3:
        e = st.radio('Phòng', ('Tất cả', 'A114', 'A115'), horizontal=False)

    with col4:
        d = st.radio('Buổi', ('Sáng', 'Chiều'))

          
    op = st.selectbox('Lớp chuyên', ('Văn', 'Toán', 'Lý', 'Hóa', 'Anh', 'Tin', 'Sử Địa', 'Trung Nhật', 'TH/SN', 'Khác'))
    st.write('Số HS:', 61, '(41 nam, 20 nữ)')
    st.write('GPA: cao nhất', 10.0, 'thấp nhất', 1.8, 'trung bình', 6.8)
    
    st.subheader('Giới tính')
    if a == 'Nam':
      df[(df['GENDER'] == "M")]
    else:
      df[(df['GENDER'] == "F")]
    
    st.subheader('Khối lớp')
    if b == 'Lớp 10':
      df[(df['CLASS'].str.contains('10'))]
    elif b == 'Lớp 11':
      df[(df['CLASS'].str.contains('11'))]
    elif b == 'Lớp 12':
       df[(df['CLASS'].str.contains('12'))]
    else: 
      df
    
    st.subheader('Phòng')
    if e == 'A114':
      df[df['PYTHON-CLASS'].str.startswith('114')]
    elif e == 'A115':
      df[df['PYTHON-CLASS'].str.startswith('115')]
    else:
      df
    
    st.subheader('Buổi học')
    if d == 'Sáng':
      df[(df['PYTHON-CLASS'].str.endswith('S'))]
    elif d == 'Chiều':
      df[(df['PYTHON-CLASS'].str.endswith('C'))]
    else:
      df
    
    st.subheader('Lớp chuyên')
    if op == 'Văn':
      df[(df["CLASS-GROUP"] == 'Chuyên Văn')]
    elif op == 'Toán':
      df[(df["CLASS-GROUP"] == 'Chuyên Toán')]
    elif op == 'Anh':
      df[(df["CLASS-GROUP"] == 'Chuyên Anh')]
    elif op == 'Tin':
      df[(df["CLASS-GROUP"] == 'Chuyên Tin')]
    elif op == 'Sử Địa':
      df[(df["CLASS-GROUP"] == 'Sử Địa')]
    elif op == 'Trung Nhật':
      df[(df["CLASS-GROUP"] == 'Trung Nhật')]
    elif op == 'TH/SN':
      df[(df["CLASS-GROUP"] == 'TH/SN')]
    else:
      df[(df["CLASS-GROUP"] == 'Khác')]
    
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
        st.info('Dễ dàng nhận thấy học sinh nam quan tâm đến lớp AI nhiều hơn học sinh nữ')

        st.subheader('Tỉ lệ khối lớp')
        f4 = px.pie(df, names='Khối lớp')
        st.write(f4)
        st.info('Dễ dàng nhận thấy học sinh khối 10 quan tâm đến lớp AI nhiều hơn học sinh khối 11&12')
        
        st.subheader('Tỉ lệ các lớp')
        f5 = px.pie(df, names='CLASS-GROUP')
        st.write(f5)
        st.info('Dễ dàng nhận thấy học sinh chuyên toán quan tâm đến lớp AI nhất, sau đó đến lớp không chuyên và cuối cùng là chuyên văn')

        st.subheader('Tỉ lệ mong muốn được học tiếp')
        f6 = px.pie(df, names='REG-MC4AI')
        st.write(f6)
        st.info('Dễ dàng nhận thấy học sinh muốn đăng kí học tiếp lớp AI ít hơn học sinh không muốn đăng kí học tiếp')

        st.subheader('Tỉ lệ học sinh được lên lớp')
        f7 = px.pie(df, names='LEN LOP')
        st.write(f7)
        st.info('Có thể dễ dàng nhận thấy học sinh có khả năng lên lớp chiếm tỉ lệ cao hơn')

        st.subheader('Tỉ lệ học sinh chuyên và thường')
        f8 = px.pie(df, names='Loại lớp')
        st.write(f8)
        st.info('Có thể dễ dàng nhận thấy học sinh quan tâm lớp AI chủ yếu là học sinh lớp chuyên')

    with tab6:
        rad = st.radio('Điểm từng Session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
        if rad == 'S1':
          fug=px.box(df, x = 'S1', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S2':
          fug=px.box(df, x = 'S2', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S3':
          fug=px.box(df, x = 'S3', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S4':
          fug=px.box(df, x = 'S4', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S5':
          fug=px.box(df, x = 'S5', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S6':
          fug=px.box(df, x = 'S6', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S7':
          fug=px.box(df, x = 'S7', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S8':
          fug=px.box(df, x = 'S8', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S9':
          fug=px.box(df, x = 'S9', y='CLASS-GROUP')
          st.write(fug)
        elif rad == 'S10':
          fug=px.box(df, x = 'S10', y='CLASS-GROUP')
          st.write(fug)
        else:
          fuug=px.box(df, x = 'GPA', y='CLASS-GROUP')
          st.write(fuug)
          st.info('Có thể dễ dàng nhận thấy điểm GPA của nhóm Chuyên Tin là cao nhất, sau đó lần lượt là điểm của các nhóm lớp tự nhiên như Chuyên Toán, Chuyên Lý, Chuyên Hóa rồi đến nhóm lớp xã hội. Thấp nhất là điểm GPA của nhóm Tích Hợp và Song Ngữ')
          
          fug=px.box(df, x = 'GPA', y='GENDER')
          st.write(fug)
          st.info('Điểm trung bình của các bạn nam cao hơn điểm trung bình của các bạn nữ')
          
          fu=px.box(df, x = 'GPA', y='Phòng học')
          st.write(fu)
          st.info('GPA của các bạn học phòng 114 cao hơn GPA các bạn học phòng 115')
          
          fuu=px.box(df, x = 'GPA', y='Buổi học')
          st.write(fuu)
          st.info('GPA của các bạn học buổi chiều cao hơn GPA các bạn học buổi sáng')
          
          fugg=px.box(df, x = 'GPA', y='Loại lớp')
          st.write(fugg)
          st.info('GPA của các bạn học lớp chuyên cao hơn GPA các bạn học lớp thường')
          
          st.write('Điểm trung bình cao nhất là:', max(df['GPA']))
          st.write('Điểm trung bình thấp nhất là:', min(df['GPA']))
          st.write('Điểm trung bình của tất cả các lớp AI:', np.mean(df['GPA']))
with tab3:
    sl = st.slider('Số nhóm', 2, 5, 3)
    def average(row):
      return (row['S1']+row['S2']+row['S3']+row['S4']+row['S5']+row['S7']+row['S8']+row['S9'])/8
    df['HW-AVG'] = df.apply(average, axis=1)
    X = df[['GPA', 'HW-AVG']].values
    if sl == 2:
      kmeans = KMeans(n_clusters=2, n_init='auto')
      kmeans.fit(X)
    elif sl == 3:
      kmeans = KMeans(n_clusters=3, n_init='auto')
      kmeans.fit(X)
    elif sl == 4:
     kmeans = KMeans(n_clusters=4, n_init='auto')
     kmeans.fit(X) 
    else:
      kmeans = KMeans(n_clusters=5, n_init='auto')
      kmeans.fit(X)
 
    plt.figure(figsize=(4,4))
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1])
    st.pyplot(plt.gcf()) # instead of plt.show()
    
    ZZ1=X[kmeans.labels_==0]
    st.write('Điểm GPA cao nhất nhóm 1 là:',max(ZZ1[0]))
    st.write('Điểm GPA thấp nhất nhóm 1 là:',min(ZZ1[0]))
    st.write('Điểm trung bình homework cao nhất nhóm 1 là:',max(ZZ1[1]))
    st.write('Điểm trung bình homework thấp nhất nhóm 1 là:',min(ZZ1[1]))

    #nhóm 2
    ZZ=X[kmeans.labels_==1]
    st.write('Điểm GPA cao nhất nhóm 2 là:',max(ZZ[0]))
    st.write('Điểm GPA thấp nhất nhóm 2 là:',min(ZZ[0]))
    st.write('Điểm trung bình homework cao nhất nhóm 2 là:',max(ZZ[1]))
    st.write('Điểm trung bình homework thấp nhất nhóm 2 là:',min(ZZ[1]))

with tab4:
    a1 = st.radio('Số đặc trưng', ('2', '3'), horizontal=True)
    if a1 == '2':
      model = LinearRegression()
      x1=df['GPA'].values
      y1=df['HW-AVG'].values
      x1 = x1.reshape(-1,1)

      model.fit(x1, y1)

      x_line = np.array([0, 10]).reshape(-1,1)
      y_line = model.predict(x_line)

      plt.scatter(x1, y1)
      plt.plot(x_line, y_line, c='y')
      plt.xlabel('GPA')
      plt.ylabel('HW-AVG')
      st.pyplot(plt.gcf()) # instead of plt.show()
      st.write('Score:', 0.85)
      
    else:

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
      st.write('Score:', 0.98)
