import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

day_data = pd.read_csv('data/day.csv')

st.header('- Dashboard Sederhana -')

st.subheader('Bike Sharing Data')
st.dataframe(day_data)

st.subheader("Visualisasi Hubungan cuaca(suhu, kecepatan angin, kelembaban) terhadap Total Penyewaan Sepeda Memakai Scatter Plot")
col1, col2, col3 = st.columns(3)
with col1:
  st.write('Temperature Vs. Total Penyewaan')
  plt.figure(figsize=(6,5))
  sns.scatterplot(x='temp', y='cnt', data=day_data)
  plt.title('Temperature Vs. Total Penyewaan')
  plt.xlabel('Temperature')
  plt.ylabel('Total Penyewaan')
  st.pyplot(plt)
  
with col2:
  st.write('Windspeed Vs. Total Penyewaan')
  plt.figure(figsize=(6,5))
  sns.scatterplot(x='windspeed', y='cnt', data=day_data)
  plt.title('Windspeed Vs. Total Penyewaan')
  plt.xlabel('Windspeed')
  plt.ylabel('Total Penyewaan')
  st.pyplot(plt)

with col3:
  st.write('Humidity Vs. Total Penyewaan')
  plt.figure(figsize=(6,6))
  sns.scatterplot(x='hum', y='cnt', data=day_data)
  plt.title('Humidity Vs. Total Penyewaan')
  plt.xlabel('Humidity')
  plt.ylabel('Total')
  st.pyplot(plt)
  
st.subheader("Visualisasi Hubungan cuaca(suhu, kecepatan angin, kelembaban) terhadap Total Penyewaan Sepeda Memakai RegPlot")
cols1,cols2, cols3 = st.columns(3)
with cols1:
  st.write('Plot Regresi: Suhu vs Total Penyewaan Sepeda')
  plt.figure(figsize=(6,5))
  sns.regplot(x='temp', y='cnt', data=day_data, line_kws={'color': 'red'})
  plt.title('Plot Regresi: Suhu vs Total Penyewaan Sepeda')
  st.pyplot(plt)
  
with cols2:
  st.write('Plot Regresi: Wind Speed vs Total Penyewaan Sepeda')
  plt.figure(figsize=(6,5))
  sns.regplot(x='windspeed', y='cnt', data=day_data, line_kws={'color': 'red'})
  plt.title('Plot Regresi: Wind Speed vs Total Penyewaan Sepeda')
  st.pyplot(plt)
    
with cols3:
  st.write('Plot Regresi: Humidity vs Total Penyewaan Sepeda')
  plt.figure(figsize=(6,5))
  sns.regplot(x='hum', y='cnt', data=day_data, line_kws={'color': 'red'})
  plt.title('Plot Regresi: Humidity vs Total Penyewaan Sepeda')
  st.pyplot(plt)  

st.caption('Berdasarkan hasil analisis dan visualisasi apakah cuaca mempengaruhi tren penyewaan sepeda. Berdasarkan hasil analisis, untuk suhu itu semakin meningkat suhu maka tingkat penyewaan sepeda semakin banyak, dibuktikan dengan menggunakan regplot garis ny semakin meningkat. Untuk kecepatan angin, penyewaan sepeda paling banyak di antara 0,1 - 0,3 semakin banyak angin mungkin pengguna semakin tidak nyaman. Sementara itu untuk kelembaban bertumpuk pada 0,4 - 1. Meskipun tidak ada pola yang jelas, ini menandakan kelembaban mungkin tidak menjadi faktor utama dalam tingkat penyewaan sepeda')
  
st.subheader("Perkembangan Penyewaan Sepeda Sepanjang Tahun")
bulan = {
    1: 'Januari',
    2: 'Februari',
    3: 'Maret',
    4: 'April',
    5: 'Mei',
    6: 'Juni',
    7: 'Juli',
    8: 'Agustus',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Desember'
}
day_data['mnth'] = day_data['mnth'].map(bulan)
plt.figure(figsize=(10,4))
sns.lineplot(x='mnth', y='cnt', data=day_data)
plt.title('Perkembangan Penyewaan Sepeda Per Bulan')
plt.xticks(rotation=50)
plt.xlabel('Bulan')
plt.ylabel('Total Penyewaan')
st.pyplot(plt)
st.caption('Berdasarkan visualisasi tingkat penyewaaan semakin meningkat mulai dari januari sampai puncaknya di bulan Juni dan September dikarenakan cuaca yang lebih hangat sehingga memunkinkan untuk bersepeda sehingga tingkat penyewaan menjadi tinggi. Kemudian setelah September terjadi penurunan yang mungkin dikaitkan dengan perubahan cuaca menjadi lebih dingin sehingga terjadi penurunan penyewaan sepeda')