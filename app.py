import streamlit as st
import pickle
import numpy as np
import pandas as pd
import zipfile
import requests

# --------------------------
# Load model and pivot table
# --------------------------
with open('book_recommender_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('book_pivot.pkl', 'rb') as f:
    book_pivot = pickle.load(f)

# --------------------------
# Load books dataset from ZIP
# --------------------------
zip_path = "Datasets.zip"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    with zip_ref.open('BX-Books.csv') as file:
        books = pd.read_csv(file, sep=';', encoding='latin-1', on_bad_lines='skip')

books = books[['Book-Title', 'Book-Author', 'Image-URL-L']]
books.rename(columns={'Book-Title': 'title'}, inplace=True)
books['title'] = books['title'].str.strip()
book_pivot.index = book_pivot.index.str.strip()

# --------------------------
# Image Validity Check Function
# --------------------------
def is_valid_image(url):
    try:
        if not url or not url.startswith("http"):
            return False
        response = requests.get(url, stream=True, timeout=7)
        return response.status_code == 200 and 'image' in response.headers.get('Content-Type', '')
    except:
        return False


# --------------------------
# Recommendation function
# --------------------------
def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=7)

    recommended_books = []
    for i in suggestions[0][1:]:
        title = book_pivot.index[i]
        book_info = books[books['title'] == title].drop_duplicates('title')

        if not book_info.empty:
            # Fetch image and validate manually
            raw_url = book_info['Image-URL-L'].values[0].strip()
            image_url = raw_url if raw_url.startswith("http") and "amazon" in raw_url.lower() else ""

            if not image_url:
                image_url = "https://via.placeholder.com/150x220.png?text=No+Image"

            recommended_books.append({
                'title': title,
                'author': book_info['Book-Author'].values[0],
                'image': image_url
            })

    return recommended_books


# --------------------------
# Streamlit UI Setup
# --------------------------
st.set_page_config(page_title="My Book Buddy", layout="wide", page_icon="📖")

# --------------------------
# Custom Styling (Dark Theme)
# --------------------------
st.markdown("""
    <style>
    body {
        color: #F1F1F1;
        background-color: #0E1117;
    }
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    h1, h2, h3, label {
        color: #F1F1F1;
    }
    div.stButton > button {
        background-color: #2c2f35;
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        font-size: 16px;
        border-radius: 8px;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #3b3f47;
        color: #ffffff;
        cursor: pointer;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# App Header
# --------------------------
st.markdown("<h1 style='text-align: center;'>My Book Buddy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Find your next favorite book powered by Machine Learning</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>AI-Powered Book Picks Just for You</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0.5px solid #444;'>", unsafe_allow_html=True)

# --------------------------
# Book Selection
# --------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<label style='color:white; font-size:16px;'>Select a book you like:</label>", unsafe_allow_html=True)
    book_name = st.selectbox("", book_pivot.index)

# --------------------------
# Recommend Button
# --------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Recommend Similar Books", use_container_width=True):
    with st.spinner("Fetching your book recommendations..."):
        recommendations = recommend_book(book_name)

    st.markdown("### 🔍 You Might Also Like:")
    st.markdown("<hr style='border: 0.5px solid #444;'>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, book in enumerate(recommendations):
        with cols[idx % 3]:
            st.image(book['image'], use_container_width=True)
            st.markdown(
                f"<div style='font-size: 16px;'><strong>{book['title']}</strong><br><em>by {book['author']}</em></div>",
                unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)

# --------------------------
# Footer
# --------------------------
st.markdown("<hr style='border: 0.5px solid #444;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-size: 13px; color: #888'>
        Built with ❤️ using <strong>Streamlit</strong> & <strong>Machine Learning</strong> <br>
        © 2025 Book Recommender Inc.
    </div>
""", unsafe_allow_html=True)
