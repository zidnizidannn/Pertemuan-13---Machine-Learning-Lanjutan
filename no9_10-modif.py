import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('modelPrediksi.sav', 'rb'))

st.title('Prediksi Harga Mobil')
st.subheader('Dataset')

df1 = pd.read_csv('CarPrice.csv')

st.subheader("Grafik Highway-mpg")
chartHighwaympg = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chartHighwaympg)

st.subheader("Grafik curbweight")
chartCurbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chartCurbweight)

st.subheader("Grafik horsepower")
chartHorsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chartHorsepower)

st.sidebar.header('Prediksi Harga')
highwaympg = st.sidebar.slider('Pilih Highway-mpg:', min_value=df1['highwaympg'].min(), max_value=df1['highwaympg'].max())
curbweight = st.sidebar.slider('Pilih Curbweight:', min_value=df1['curbweight'].min(), max_value=df1['curbweight'].max())
horsepower = st.sidebar.slider('Pilih Horsepower:', min_value=df1['horsepower'].min(), max_value=df1['horsepower'].max())

if st.sidebar.button('Prediksi'):
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    harga_mobil_float = float(car_prediction[0])
    harga_mobil_formatted = f'Harga Mobil: $ {harga_mobil_float:,.2f}'

    st.sidebar.subheader("Hasil Prediksi:")
    st.sidebar.write(harga_mobil_formatted)

    st.subheader("Perbandingan Harga Mobil Prediksi dengan Data Aktual")
    prediksi = pd.DataFrame({'Prediction': [harga_mobil_float], 'Mean Price': [df1['price'].mean()]})
    st.bar_chart(prediksi)

st.sidebar.subheader("Inputan dari Anda:")
st.sidebar.write(f"Highway-mpg: {highwaympg}, Curbweight: {curbweight}, Horsepower: {horsepower}")
