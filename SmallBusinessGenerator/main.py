import streamlit as st
from Small_Business import generate_small_business_name_and_services  # Adjusted import

st.title("Small_Business Name Generator")

small_business = st.sidebar.selectbox(
    "Choose a small business", ("Cafe", "Boutique", "Salon", "Gym", "Deli"))

if small_business:
    response = generate_small_business_name_and_services(small_business)
    st.header(response['Business_name'].strip())
    Itemize_Services = response['Itemize_Services'].strip().split(",")
    st.write("**Itemize_Services**")
    for item in Itemize_Services:
        st.write("-", item)
