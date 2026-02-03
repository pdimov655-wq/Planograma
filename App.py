import streamlit as st

# 1. Конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- МОДЕРЕН UI ДИЗАЙН (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* Основен фон и шрифтове */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Скриване на излишни елементи */
    #MainMenu, footer, header {visibility: hidden;}

    /* Градиентно заглавие */
    .main-title {
        background: linear-gradient(90deg, #0046ad, #009dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
        padding-top: 10px;
    }

    /* Стилизиране на белите карти за избор */
    [data-testid="stVerticalBlock"] > div > div > div.stSelectbox, 
    [data-testid="stVerticalBlock"] > div > div > div.stRadio {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        padding: 25px !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        margin-bottom: 20px !important;
    }

    /* Красиви заглавия на разделите */
    h3 {
        color: #1e3a8a !important;
        font-weight: 600 !important;
        letter-spacing: -0.5px;
    }

    /* Стилизиране на радио бутоните и текста */
    label, .stMarkdown p {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }

    /* Модерен ZOOM бутон */
    .zoom-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(45deg, #0046ad, #448aff);
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 4px 15px rgba(0, 70, 173, 0.3);
        margin-top: 20px;
    }
    .zoom-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 70, 173, 0.4);
    }

    /* Стил на Logout в страничното меню */
    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid #0046ad !important;
        background-color: white !important;
        color: #0046ad !important;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #0046ad !important;
        color: white !important;
    }

    /* Стилизиране на инфо блока */
    .stAlert {
        border-radius: 15px !important;
        border-left: 5px solid #0046ad !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД (ПРОФЕСИОНАЛНА КАРТА) ---
if "password_correct" not in st.session_state:
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div style='background: white; padding: 40px; border-radius: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); text-align: center;'>
                <h2 style='color: #1e3a8a; margin-bottom: 20px;'>🚀 ПЛАНOГРАМА PRO</h2>
                <p style='color: #666;'>Моля, въведете парола за достъп</p>
            </div>
        """, unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Парола...")
        if st.button("ОТКЛЮЧИ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1 class='main-title'>🍦 Ice Cream Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 👤 Профил")
    if st.button("Изход (Logout)"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.markdown("### 📋 Настройки")
    
    # 1. Избор на канал
    client_type = st.selectbox("📌 Тип клиент", ["ТТ", "АТЦ", "Петролен канал"])
    
    sub_channel = client_type
    specific_layout = "Стандартен фризер"

    if client_type == "Петролен канал":
        sub_channel = st.selectbox("⛽ Верига", ["ОМВ", "Лукойл"])
        if sub_channel == "ОМВ":
            specific_layout = st.selectbox(
                "🧊 Тип излагане (ОМВ):", 
                ["Стандартен фризер", "Гондола 4х11", "Гондола 4х8", "Гондола 4х4"]
            )

    is_gondola = "Гондола" in specific_layout
    freezer_size = "N/A"
    brand = "Mix"

    if not is_gondola:
        st.markdown("---")
        st.write("**📐 Размер на фризера:**")
        freezer_size = st.radio("", ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], horizontal=True)
        
        st.markdown("---")
        st.write("**🏷️ Марка:**")
        brand = st.radio("", ["Milka", "Nestlé"], horizontal=True)
    else:
        st.info("💡 Гондолите са със смесено излагане (Mix).")

with col2:
    st.markdown("### 🖼️ Планограма")
    
    # Текст на селекцията
    if is_gondola:
        current_selection = f"Микс | {specific_layout}"
        search_brand, search_target = "Mix", specific_layout
    else:
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        search_brand, search_target = brand, sub_channel
        
    st.info(f"📍 Активен избор: **{current_selection}**")

    # База данни
    planogram_links = {
        ("Mix", "Гондола 4х11", "N/A"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/%D0%9E%D0%BC%D0%B2%204x11.jpg",
    }

    image_url = planogram_links.get((search_brand, search_target, freezer_size))

    if image_url:
        # Рамка около снимката
        st.markdown(f"""
            <div style='border: 4px solid white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
                <img src='{image_url}' style='width: 100%; display: block;'>
            </div>
        """, unsafe_allow_html=True)
        
        # Модерен Zoom бутон
        st.markdown(f"""
            <a href="{image_url}" target="_blank" class="zoom-btn">
                🔍 КЛИКНИ ЗА ПЪЛЕН ZOOM
            </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Очаква се качване на снимка.")
        st.image("https://via.placeholder.com/800x500.png?text=No+Image+Available", use_container_width=True)

st.markdown("<br><br><center><p style='color: #7f8c8d;'>© 2026 Premium Sales Support | V 3.0</p></center>", unsafe_allow_html=True)
