import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

customer_data = pd.read_csv('E:\MSIB\Bangkit\SubmissionAnalisisdata\dashboard\customers_dataset.csv')
product_data = pd.read_csv('E:\MSIB\Bangkit\SubmissionAnalisisdata\dashboard\products_dataset.csv')
order_data = pd.read_csv('E:\MSIB\Bangkit\SubmissionAnalisisdata\dashboard\order_items_dataset.csv')

order_data_merge = pd.merge(
  left = order_data,
  right = product_data,
  how="left",
  right_on="product_id",
  left_on="product_id"
)

st.write('## E-Commerce Public Dataset')

st.write('### Dataset')
st.dataframe(customer_data)

st.write('### Dataset Statistic')

col1, col2 = st.columns(2)
with col1:
  st.dataframe(customer_data.describe())
  
with col2:
  st.write("Persebaran Customer")
  plt.figure(figsize=(10,10))
  plt.pie(customer_data['customer_city'].value_counts().iloc[:10], labels=customer_data['customer_city'].value_counts().iloc[:10].index, autopct='%1.1f%%')
  st.pyplot(plt)
  
    
st.subheader('Kota dengan Customer terbanyak')    
plt.figure(figsize=(10,10))
sns.countplot(x='customer_city', data=customer_data, order=customer_data['customer_city'].value_counts().iloc[:10].index)
plt.xlabel('Customer City')
plt.xticks(rotation=90)
st.pyplot(plt)

st.subheader('Persebaran Harga Produk')
plt.figure(figsize=(16,10))
sns.barplot(x='product_category_name', y='price', data=order_data_merge)
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)