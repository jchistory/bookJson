import streamlit as st
import json

def create_json():
    return json.dumps(book, indent=4).encode("utf-8")

with st.container(gap="xsmall"):
    st.title("Book JSON Generator")
    book_title = st.text_input("Book Title", required=True)
    book_subtitle = st.text_input("Book Subtitle")
    book_pageCount = st.number_input(
        "Page Count",
        min_value=1,
        value=1,
        step=1,
        required=True)
    book_imageFolder = st.text_input("Image Folder", required=True, value="pages")
    book_imagePrefix = st.text_input("Image Prefix", required=True, value="page_")
    book_imageExtension = st.text_input("Image Extension", value=".jpg", required=True)
    book_showCover = st.checkbox("Show Cover", value=True)
    book_sourceLabel = st.text_input("Source Label - must also include a URL")
    book_sourceUrl = st.text_input("Source URL - must also include a label")

book = {
    "title": book_title,
    "subtitle": book_subtitle,
    "pageCount": book_pageCount,
    "imageFolder": book_imageFolder,
    "imagePrefix": book_imagePrefix,
    "imageExtension": book_imageExtension,
    "showCover": book_showCover,
    "sourceLabel": book_sourceLabel,
    "sourceUrl": book_sourceUrl
}

if (
    (book_sourceLabel.strip() and not book_sourceUrl.strip())
    or  
    (book_sourceUrl.strip() and not book_sourceLabel.strip())
):
    st.error("Source Label or Source URL are empty. If one is filled, the other needs to be filled.")
else:
    st.download_button(
        label="Create JSON",
        data=create_json,
        file_name="book.json",
        mime="application/json",
        on_click="ignore"
    )

