import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt

st.header('st.button')

if st.button('Say hello'):
    st.write('Hello there')
else:
    st.write('Dadaaa')
    
st.title('===== NOMOR 3 =====\n')
st.title('Ini adalah title')
st.markdown('''Ini adalah markdown''')
st.header('Ini adalah header')
st.subheader('Ini adalah subheader')
st.caption('Ini adalah caption')
st.write('x=', 2023)


st.title('===== NOMOR 4 =====\n')
st.checkbox('yes')
st.button('klik')
st.radio('Pilih gender', ['Laki-laki', 'Perempuan'])
st.multiselect('Pilih gender', ['Laki-laki', 'Perempuan'])
st.selectbox('Pilih planet', ['Bumi', 'Mars', 'Jupiter', 'Saturnus', 'Uranus', 'Neptunus'])
st.select_slider('Pilih tanda',options=['buruk', 'baik', 'luar biasa'])
st.slider('Pilih nilai', 0, 50)


st.title('===== NOMOR 5 =====\n')
st.number_input('Pilih nomor', value=1)
st.text_input('Alamat email')
st.date_input('Tanggal perjalanan')
st.time_input('Jam sekolah')
st.text_area('Deskripsi')
st.file_uploader('Upload foto', type=['jpg', 'png', 'jpeg'])
st.color_picker('Pilih warna')

st.title('===== NOMOR 6 =====\n')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.title('===== NOMOR 7 =====\n')

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.title('===== NOMOR 8 =====\n')
menu = ["Home","Gambar", "Dataset", "Grafik"]
pilihan = st.sidebar.selectbox("Pilih menu", menu)

def grafik():
    st.subheader('Grfik random')
    chart_data = pd.DataFrame(np.random.randn(20, 5),columns=['a', 'b', 'c', 'd', 'e'])
    st.line_chart(chart_data)

if pilihan == "Home":
    st.write("Ini adalah Halaman Utama")
    
elif pilihan == "Gambar":
    st.subheader('Gambar animasi')
    st.image("assets/anger.png",width=300)
    
elif pilihan == "Dataset":
    st.subheader('Daftar tempat paling sering dikunjungi turis')
    df = pd.read_csv("assets/Wisata turis.csv")
    st.write(df.head())
    
else:
    grafik()