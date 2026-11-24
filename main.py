import streamlit as st
import langchain_helper as p
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("indian", "american", "mexican", "arabic", "african", "australian"))

if cuisine:
    response = p.generate(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("Menu Items")
    for i in menu_items:
        st.write("-", i)