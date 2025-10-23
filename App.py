import streamlit as st
from PIL import Image

# ---------------------
# CONFIGURAÇÕES DA PÁGINA
# ---------------------
st.set_page_config(
    page_title="Site do Matheus",
    page_icon="🌤️",
    layout="wide"
)

# ---------------------
# ESTILO PERSONALIZADO (CSS)
# ---------------------
st.markdown("""
    <style>
    /* Fundo com imagem e gradiente */
    .stApp {
        background-image: linear-gradient(
            rgba(0,0,0,0.5),
            rgba(0,0,0,0.5)
        ), url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=80');
        background-size: cover;
        background-position: center;
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Centralização e espaçamento */
    .center {
        text-align: center;
        padding-top: 10%;
        padding-bottom: 10%;
    }

    /* Título principal animado */
    .title {
        font-size: 60px;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }

    /* Subtítulo */
    .subtitle {
        font-size: 30px;
        margin-top: 10px;
        opacity: 0.85;
    }

    /* Sessão sobre mim */
    .about {
        background: rgba(255, 255, 255, 0.1);
        padding: 40px;
        border-radius: 15px;
        margin-top: 50px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    }

    /* Animação suave */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# CONTEÚDO
# ---------------------
st.markdown("""
    <div class="center">
        <div class="title">☀️ Olá, eu sou o Matheus!</div>
        <div class="subtitle">Estudante de programação — este é o meu primeiro site de muitos!</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------
# SESSÃO SOBRE MIM
# ---------------------
st.markdown("""
    <div class="about">
        <h2>Sobre mim</h2>
        <p>Sou um apaixonado por tecnologia e estou começando minha jornada no mundo da programação.
        Meu objetivo é aprender cada vez mais sobre desenvolvimento web, Python e inteligência artificial.</p>

        <p>Gosto de desafios, de resolver problemas e de criar coisas bonitas — como este site! 😄</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------
# IMAGEM OPCIONAL
# ---------------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(
        "https://cdn.pixabay.com/photo/2015/01/09/02/45/keyboard-593367_1280.jpg",
        caption="Meu mundo é o código 💻",
        use_container_width=True
    )

# ---------------------
# RODAPÉ
# ---------------------
st.markdown("""
    <div style='text-align: center; margin-top: 50px; opacity: 0.7;'>
        Feito com ❤️ por Matheus — 2025
    </div>
""", unsafe_allow_html=True)
