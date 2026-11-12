import streamlit as st
st.title("Book JSON Generator")
book_title = st.text_input("Book Title")
st.write(book_title)
image_extension = st.text_input("Image Extension", value=".jpg")