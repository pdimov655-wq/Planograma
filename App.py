import streamlit as st

# 1. Основна конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- СИСТЕМА ЗА ВХОД С ПЕРСОНАЛИЗИРАН ФОН ---
if "password_correct" not in st.session_state:
    bg_image = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/froneri-brand-images.jpg"

    st.markdown(f"""
        <style>
        /* Фон само за началната страница */
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("{bg_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Изчистване на заглавната част входа */
        header, [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
        }}

        /* Стилизирана карта за вход */
        .login-card {{
            background: rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(15px);
            padding: 40px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            text-align: center;
            margin-top: 50px;
        }}

        /* Цвят на текста при входа */
        .login-card h2, .login-card p {{
            color: white !important;
            font-family: 'Inter', sans-serif;
        }}

        /* Стил на полето за парола при входа */
        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 10px !important;
            color: black !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        st.markdown(f"""
            <div class='login-card'>
                <h2>🍦 ПЛАНOГРАМА PRO</h2>
                <p>Въведете парола за достъп до системата</p>
            </div>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("", type="password", placeholder="Парола...")
        
        if st.button("ОТКЛЮЧИ ПАНЕЛ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- СТИЛОВЕ ЗА ВЪТРЕШНИЯ ИНТЕРФЕЙС (След Login) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* Смяна на фона за работния панел (по-чист) */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .main-title {
        background: linear-gradient(90deg, #0046ad, #009dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Карти за избор */
    [data-testid="stVerticalBlock"] > div > div > div.stSelectbox, 
    [data-testid="stVerticalBlock"] > div > div > div.stRadio {
        background: white !important;
        padding: 20px !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        border: 1px solid #eee !important;
        margin-bottom: 15px !important;
    }

    label, p { color: #1e3a8a !important; font-weight: 600 !important; }

    /* Zoom Бутон */
    .zoom-btn {
        display: block;
        background: linear-gradient(45deg, #0046ad, #448aff);
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0 4px 12px rgba(0, 70, 173, 0.2);
    }

    /* Скриване на Streamlit бутона Manage app */
    .stAppDeployButton { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1 class='main-title'>🍦 Ice Cream Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 👤 Профил")
    if st.button("Изход (Logout)"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("📋 Настройки")
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
    freezer_size, brand = "N/A", "Mix"

    if not is_gondola:
        st.write("**📐 Размер на фризера:**")
        freezer_size = st.radio("", ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], horizontal=True)
        st.write("**🏷️ Марка:**")
        brand = st.radio("", ["Milka", "Nestlé"], horizontal=True)
    else:
        st.info("💡 Гондолите са със смесено излагане (Mix).")

with col2:
    st.subheader("🖼️ Планограма")
    
    if is_gondola:
        current_selection = f"Микс | {specific_layout}"
        search_brand, search_target = "Mix", specific_layout
    else:
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        search_brand, search_target = brand, sub_channel
        
    st.info(f"📍 Активен избор: **{current_selection}**")

    # БАЗА ДАННИ
    planogram_links = {
        ("Mix", "Гондола 4х11", "N/A"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/%D0%9E%D0%BC%D0%B2%204x11.jpg",
    }

    image_url = planogram_links.get((search_brand, search_target, freezer_size))

    if image_url:
        st.markdown(f"""
            <div style='border: 4px solid white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
                <img src='{image_url}' style='width: 100%; display: block;'>
            </div>
            <a href="{image_url}" target="_blank" class="zoom-btn">🔍 КЛИКНИ ЗА ПЪЛЕН ZOOM</a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Очаква се качване на снимка.")
        st.image("https://via.placeholder.com/800x500.png?text=No+Image+Available", use_container_width=True)

st.markdown("<br><center><p style='color: #7f8c8d;'>© 2026 Ice Cream Sales Team | V 3.2</p></center>", unsafe_allow_html=True)
