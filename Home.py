import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MyBookBuddy | Your Personal Reading Companion",
    layout="wide",
    page_icon="📚"
)

# -----------------------------
# Sidebar Navigation (Optional)
# -----------------------------
with st.sidebar:
    st.title("📚 MyBookBuddy")
    nav = st.radio("Navigate", ["🏠 Home", "📖 Recommender"])
    if nav == "📖 Recommender":
        st.switch_page("pages/1_Book_Recommender.py")  # Path must be correct in your folder

# -----------------------------
# Custom CSS for Dark Theme
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #F1F1F1;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4, p {
        color: #F1F1F1;
    }
    div.cta-button button {
        background-color: #2C2F35 !important;
        color: white !important;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 18px;
        border-radius: 8px;
        transition: 0.3s ease;
    }
    div.cta-button button:hover {
        background-color: #3B3F47 !important;
        transform: scale(1.05);
        cursor: pointer;
    }
    hr {
        border: 0.5px solid #444;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>📖 Welcome to MyBookBuddy</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 18px; max-width: 800px; margin: auto;'>
Your smart, AI-powered reading companion. Discover your next favorite book based on what you already love.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CTA Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='cta-button'>", unsafe_allow_html=True)
    go = st.button("🚀 Get Recommendations", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if go:
    st.switch_page("pages/1_Book_Recommender.py")  # Make sure this exists

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------
# Features Section
# -----------------------------
st.markdown("<h2 style='text-align: center;'>✨ Why MyBookBuddy?</h2>", unsafe_allow_html=True)

features = [
    "🔍 Personalized book suggestions tailored just for you",
    "🤖 Powered by Machine Learning for smarter discovery",
    "📸 Book covers, authors & more – visually rich results",
    "🎯 No signup needed – just pick and discover!"
]

for feat in features:
    st.markdown(f"<p style='text-align: center; font-size: 16px;'>{feat}</p>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------
# Testimonials with Names and Circular Avatars
# -----------------------------
st.markdown("<h3 style='text-align: center;'>💬 What Our Users Say</h3>", unsafe_allow_html=True)

# CSS for circular images
st.markdown("""
    <style>
    .testimonial-img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .testimonial-name {
        font-weight: bold;
        font-size: 16px;
        color: #F1F1F1;
        text-align: center;
    }
    .testimonial-text {
        font-size: 14px;
        color: #DDD;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://avatars.githubusercontent.com/u/155903223?v=4' class='testimonial-img'>
            <div class='testimonial-name'>Syed Hammad</div>
            <div class='testimonial-text'>“Found books I never thought I'd love. Brilliant!”<br>⭐️⭐️⭐️⭐️⭐️</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://randomuser.me/api/portraits/men/46.jpg' class='testimonial-img'>
            <div class='testimonial-name'>Ahmed Rehman</div>
            <div class='testimonial-text'>“MyBookBuddy understands my taste better than my friends.”<br>⭐️⭐️⭐️⭐️⭐️</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://avatars.githubusercontent.com/u/151808307?v=4' class='testimonial-img'>
            <div class='testimonial-name'>Umer Abbasi</div>
            <div class='testimonial-text'>“Love the clean interface and fast suggestions.”<br>⭐️⭐️⭐️⭐️</div>
        </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Footer
# -----------------------------

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0.5px solid #444;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-size: 13px; color: #888'>
        Built By Ehtesham with ❤️ using <strong>Streamlit</strong> & <strong>Machine Learning</strong> <br>
        © 2025 MyBookBuddy Inc.
    </div>
""", unsafe_allow_html=True)
