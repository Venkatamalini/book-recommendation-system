import streamlit as st
import pickle

# -----------------------------
# Load Model Files
# -----------------------------
pt = pickle.load(open('model/books.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(book_name):
    matches = [book for book in pt.index if book_name.lower() in book.lower()]
    
    if len(matches) == 0:
        return []
    
    book_name = matches[0]
    index = list(pt.index).index(book_name)

    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    return [pt.index[i[0]] for i in distances]


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Book Recommendation System", page_icon="📚")

# Title
st.title("📚 Book Recommendation System")

# Business Objective (from README)
st.markdown("""
### 🎯 Business Objective  
Recommend books to users based on their preferences using **collaborative filtering**.

This system analyzes user-book interactions and suggests similar books using **cosine similarity**.
""")

# Dataset Info (short version from README)
with st.expander("📂 Dataset Information"):
    st.write("""
    - **Users**: User ID, Location, Age  
    - **Books**: Title, Author, Publisher, Year  
    - **Ratings**: Ratings from 1–10 (0 = implicit)  
    """)

# -----------------------------
# User Input
# -----------------------------
st.markdown("### 🔍 Enter a Book Name")
book_name = st.text_input("Type here...")

# -----------------------------
# Recommendation Button
# -----------------------------
if st.button("Recommend"):

    if book_name.strip() == "":
        st.warning("⚠️ Please enter a book name")
    
    else:
        recommendations = recommend(book_name)

        if len(recommendations) == 0:
            st.error("❌ Book not found in dataset")
        
        else:
            st.success("✅ Top Recommended Books:")

            for i, book in enumerate(recommendations, 1):
                st.write(f"**{i}. {book}**")


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("""
💡 **Model Used:** Item-Based Collaborative Filtering  
⚙️ **Technique:** Cosine Similarity  
📊 Built using Pandas, NumPy, Scikit-learn, Streamlit
""")