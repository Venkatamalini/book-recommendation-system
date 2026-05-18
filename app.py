import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Load data
# -----------------------------
books = pickle.load(open('model/books.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# -----------------------------
# Recommendation function
# -----------------------------
def recommend(book_name):
    try:
        index = books[books['Book-Title'] == book_name].index[0]
        distances = similarity[index]
        books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_books = []

        for i in books_list:
            recommended_books.append(books.iloc[i[0]]['Book-Title'])

        return recommended_books

    except:
        return []

# -----------------------------
# UI Design
# -----------------------------
st.set_page_config(page_title="Book Recommender", layout="wide")

st.title("📚 Book Recommendation System")
st.markdown("Get similar books instantly!")

# Dropdown for book selection
book_list = books['Book-Title'].values
selected_book = st.selectbox("Select a book", book_list)

# Button
if st.button("Recommend"):

    recommendations = recommend(selected_book)

    if recommendations:
        st.subheader("📖 Recommended Books:")
        for book in recommendations:
            st.write("👉", book)
    else:
        st.error("Book not found or model not ready.")