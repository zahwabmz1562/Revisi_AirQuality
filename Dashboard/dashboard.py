import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning

# Load data
data_url = 'merged_data.csv'
data = pd.read_csv(data_url).dropna()  # Menghapus baris dengan nilai yang hilang

# Sidebar (navbar)
st.sidebar.title('Navigation')
selected_page = st.sidebar.radio('Go to', ['About', 'Pie Chart', 'Heatmap', 'Boxplot', 'Histplot'])

# Main content
st.title('Air Quality Dashboard 2024')

if selected_page == 'About':
    st.header('About')
    st.write('Air Quality Dashboard 2024 adalah sebuah aplikasi interaktif yang dirancang untuk memvisualisasikan dan menganalisis data kualitas udara. Aplikasi ini memberikan informasi tentang berbagai parameter kualitas udara, seperti PM2.5, PM10, SO2, NO2, CO, dan O3.')
    st.write('Fitur Utama:Pie Chart Page: Halaman ini memungkinkan untuk memilih parameter tertentu dan melihat representasinya dalam bentuk diagram lingkaran (pie chart). Ini memberikan gambaran visual tentang proporsi setiap nilai parameter.')
    st.write('Heatmap Page: Menampilkan heatmap korelasi antar parameter kualitas udara. Ini membantu dalam memahami hubungan antar parameter dan mengidentifikasi pola korelasi.')
    st.write('Boxplot Page: Memberikan insight tentang distribusi statistik untuk beberapa parameter utama kualitas udara. Boxplot membantu dalam melihat sebaran nilai-nilai dan mendeteksi adanya pencilan (outliers).')
    st.write('Histogram Plot Page: Halaman ini memungkinkan untuk memilih parameter dan melihat distribusi frekuensi nilainya dalam bentuk histogram. Ini memberikan pemahaman lebih mendalam tentang pola distribusi data.')

elif selected_page == 'Pie Chart':
    st.header('Pie Chart')
    # Example code to display pie chart
    st.write("Select a parameter for the Pie Chart.")
    selected_parameter = st.selectbox('Select Parameter', data.columns)
    values = data[selected_parameter].value_counts()
    labels = values.index
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

elif selected_page == 'Heatmap':
    st.header('Heatmap')
    # Code to display heatmap
    plt.figure(figsize=(12, 6))
    corr_of_col = data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN']]
    korelasi = corr_of_col.corr()
    sns.heatmap(korelasi, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Heatmap of Correlation')
    st.pyplot()

elif selected_page == 'Boxplot':
    st.header('Boxplot')
    # Code to display boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']], palette='Set3')
    plt.title('Boxplot of Air Quality Parameters')
    st.pyplot()

elif selected_page == 'Histplot':
    st.header('Histogram Plot')
    # Code to display histplot
    selected_parameter = st.selectbox('Select Parameter', data.columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(data[selected_parameter], bins=20, kde=True, color='skyblue')
    plt.title(f'Histogram Plot of {selected_parameter}')
    plt.xlabel(selected_parameter)
    plt.ylabel('Frequency')
    st.pyplot()
