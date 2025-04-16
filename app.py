import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="🎤 K-Pop Lovers", page_icon="🎶", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8cdda, #1e90ff, #e0c3fc);
        animation: gradientBG 15s ease infinite;
        background-size: 400% 400%;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }

    h1, h2, h3 {
        color: #ff1493;
        text-shadow: 2px 2px 4px #00000033;
    }

    .stButton>button {
        background-image: linear-gradient(to right, #ff6ec4, #7873f5);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.7em 1.2em;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 10px #fff;
        transform: scale(1.05);
    }

    .stSelectbox>div>div>div {
        background-color: #ffeefc;
    }

    .stTextInput>div>div>input,
    .stTextArea textarea {
        background-color: #fffaf3;
        border-radius: 8px;
        padding: 0.5em;
        border: 1px solid #ccc;
    }

    .css-1d391kg {  / Sidebar radio buttons /
        color: #6a0dad;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# Judul
st.title("🎤 Survei K-Pop Lovers")
st.markdown("Beritahu kami idol, grup, dan lagu K-Pop favoritmu! 💜")

# Navigasi
menu = st.sidebar.radio("Menu", ["Formulir", "Data Responden", "Statistik", "Tentang"])

# Dummy data responden
data_dummy = pd.DataFrame({
    "Nama": [f"Fan {i}" for i in range(1, 26)],
    "Grup Favorit": [
        "BTS", "BLACKPINK", "EXO", "TWICE", "Red Velvet",
        "NewJeans", "IVE", "NCT", "TXT", "ENHYPEN",
        "BTS", "BLACKPINK", "EXO", "Red Velvet", "TWICE",
        "NewJeans", "EXO", "BTS", "BLACKPINK", "Red Velvet",
        "TWICE", "NewJeans", "IVE", "BTS", "BLACKPINK"

    ],
    "Lagu Favorit": [
        "Butter", "DDU-DU DDU-DU", "Love Shot", "TT", "Psycho",
        "Hype Boy", "LOVE DIVE", "BEAUTIFUL", "0X1=LOVESONG", "Polaroid Love",
        "DNA", "Pink Venom", "Ko Ko Bop", "Feel My Rhythm", "Fancy",
        "ETA", "Tempo", "Spring Day", "Kill This Love", "Queendom",
        "What is Love?", "Attention", "After LIKE", "Boy With Luv", "Shut Down"
    ],
    "Frekuensi Dengar": [
        "Setiap Hari", "Setiap Hari", "Kadang-kadang", "Jarang", "Setiap Hari",
        "Sering", "Setiap Hari", "Kadang-kadang", "Sering", "Setiap Hari",
        "Setiap Hari", "Sering", "Kadang-kadang", "Jarang", "Sering",
        "Setiap Hari", "Jarang", "Setiap Hari", "Sering", "Kadang-kadang",
        "Sering", "Setiap Hari", "Setiap Hari", "Setiap Hari", "Sering"
    ]
})

# Formulir
if menu == "Formulir":
    st.header("📝 Formulir K-Pop Lovers")

    with st.form("form_kpop"):
        nama = st.text_input("Nama")
        usia = st.number_input("Usia", min_value=10, max_value=100, value=20)
        grup = st.selectbox("Grup K-Pop Favorit", [
            "BTS", "BLACKPINK", "EXO", "TWICE", "Red Velvet", "NewJeans", "IVE", "LE SSERAFIM", "TXT", "ENHYPEN", "NCT" "Lainnya"
        ])
        lagu = st.text_input("Lagu K-Pop Favorit")
        frekuensi = st.selectbox("Seberapa Sering Dengerin K-Pop?", [
            "Setiap Hari", "Sering", "Kadang-kadang", "Jarang"
        ])
        alasan = st.text_area("Kenapa kamu suka grup atau lagu ini?")
        submitted = st.form_submit_button("Kirim")

        if submitted:
            st.success("Terima kasih! Jawaban kamu sudah direkam.")
            st.write(f"Nama: {nama}")
            st.write(f"Grup Favorit: {grup}")
            st.write(f"Lagu Favorit: {lagu}")
            st.write(f"Frekuensi Dengar: {frekuensi}")
            st.write(f"Alasan: {alasan}")

# Data
elif menu == "Data Responden":
    st.header("📋 Data Responden Fans K-Pop")
    st.dataframe(data_dummy)

# Statistik
elif menu == "Statistik":
    st.header("📊 Statistik Grup Favorit")

    count_grup = data_dummy["Grup Favorit"].value_counts().reset_index()
    count_grup.columns = ["Grup", "Jumlah"]

    # Bar Chart
    st.subheader("📈 Diagram Batang")
    st.bar_chart(count_grup.set_index("Grup"))


    # Pie Chart
    st.subheader("🥧 Diagram Lingkaran")
    fig1, ax1 = plt.subplots()
    ax1.pie(count_grup["Jumlah"], labels=count_grup["Grup"], autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Line Chart
    st.subheader("📉 Diagram Garis")
    st.line_chart(count_grup.set_index("Grup"))

# Tentang
elif menu == "Tentang":
    st.header("💜 Tentang Website Ini")
    st.video("https://www.youtube.com/watch?v=3YqPKLZF_WU") 
    st.markdown(" Website ini dirancang untuk mengumpulkan data dari para fans K-Pop tentang grup dan lagu favorit mereka." \
    
     "Tujuannya adalah memahami tren fandom di kalangan K-Popers muda." \
    
     "Dibuat dengan ❤️ oleh: hysrenn ")
