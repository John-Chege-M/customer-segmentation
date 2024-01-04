import streamlit as st
import joblib

model = joblib.load("d:\MACHINE LEARNING PROJECTS\customer segmentation\Customer_Segmentation.pkl")

st.header("Clustering Customers Using Machine Learning")
st.write()
st.write('Want to know which cluster a customer belong to?')
st.write()
st.write('Lets get to work')

p1 = st.number_input('Enter your annual income (0-137 k$)', 0,137)
p2 = st.number_input('Enter your spending score (1-100)', 0,100)

if st.button('Predict cluster'):
    prediction = model.predict([[p1,p2]])
    if prediction == 0:
        st.success("Cluster 1. The customers with average salary and average spending")
    elif prediction == 1:
        st.success("Cluster 2. The customers with high income and high spending.")
    elif prediction == 2:
        st.success("Cluster 3. The customers with low income and high spending.")
    elif prediction == 3:
        st.success("Cluster 4. The customers with high income with low spending.")
    elif prediction == 4:
        st.success("Cluster 5. The Customers with low income but low spending.")