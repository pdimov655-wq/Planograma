import streamlit as st

# 1. Основна конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ГЛОБАЛЕН CSS ЗА СКРИВАНЕ И СТИЛИЗИРАНЕ ---
st.markdown("""
    <style>
    /* Скриване на системни елементи */
    #MainMenu, footer, header, .stAppDeployButton { visibility: hidden !important; display: none !important; }
    [data-testid="stStatusWidget"] { visibility: hidden; }
    
    /* СТИЛИЗИРАНЕ НА БУТОНИТЕ (RADIO) КАТО ПЛОЧКИ */
    div[data-testid="stRadio"] > div {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 10px !important;
    }
    
    div[data-testid="stRadio"] label {
        background-color: #ffffff !important;
        border: 2px solid #1e3a8a !important;
        padding: 8px 16px !important;
        border-radius: 12px !important;
        color: #1e3a8a !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.2s ease-in-out;
    }

    /* Цвят при селекция - СИН */
    div[data-testid="stRadio"] label[data-selected="true"] {
        background-color: #1e3a8a !important;
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(30, 58, 138, 0.3);
    }

    /* Премахване на оригиналните кръгчета */
    div[data-testid="stRadio"] div[role="radiogroup"] > div > div:first-child { display: none !important; }
    
    /* Общи стилове за работния панел */
    .stApp { background-color: #f8f9fa; }
    .stMarkdown, p, label, h3 { color: #1e3a8a !important; font-weight: 600 !important; }
    
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
    }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД С ФОН ---
if "password_correct" not in st.session_state:
    bg_image = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/froneri-brand-images.jpg"
    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{bg_image}");
            background-size: cover; background-position: center; background-attachment: fixed;
        }}
        .login-card {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px);
            padding: 40px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.2);
            text-align: center; margin-top: 50px; color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        st.markdown("<div class='login-card'><h2>🔒 Вход</h2><p>Digital Planogram Assistant</p></div>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Парола...")
        if st.button("ВЛЕЗ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1 style='text-align: center;'>🍦 Дигитален Асистент за Планограми</h1>", unsafe_allow_html=True)

with st.sidebar:
    if st.button("Изход (Logout)"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📋 Параметри")
    
    # 1. ТИП КЛИЕНТ (Бутони вместо меню)
    st.write("**Тип на клиента:**")
    client_type = st.radio("ClientType", ["ТТ", "АТЦ", "Петролен канал"], horizontal=True, label_visibility="collapsed")
    
    sub_channel = client_type
    specific_layout = "Стандартен фризер"

    # 2. ПОДКАНАЛ (Ако е Петролен)
    if client_type == "Петролен канал":
        st.write("**Верига:**")
        sub_channel = st.radio("Chain", ["ОМВ", "Лукойл"], horizontal=True, label_visibility="collapsed")
        if sub_channel == "ОМВ":
            st.write("**Тип излагане (ОМВ):**")
            specific_layout = st.radio("OMVType", ["Стандартен фризер", "Гондола 4х11", "Гондола 4х8", "Гондола 4х4"], horizontal=True, label_visibility="collapsed")

    is_gondola = "Гондола" in specific_layout
    freezer_size, brand = "N/A", "Mix"

    if not is_gondola:
        st.write("**Размер на фризера:**")
        freezer_size = st.radio("Size", ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], horizontal=True, label_visibility="collapsed")
        st.write("**Марка:**")
        brand = st.radio("Brand", ["Milka", "Nestlé"], horizontal=True, label_visibility="collapsed")

with col2:
    st.subheader("🖼️ Визуализация")
    
    if is_gondola:
        current_selection = f"Микс Продукти | {specific_layout}"
        search_brand, search_target = "Mix", specific_layout
    else:
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        search_brand, search_target = brand, sub_channel
        
    st.info(f"📍 Избор: **{current_selection}**")

    # --- БАЗА ДАННИ ---
    planogram_links = {
        ("Mix", "Гондола 4х11", "N/A"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/%D0%9E%D0%BC%D0%B2%204x11.jpg",
        ("Nestlé", "АТЦ", "80см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_80_atc.jpg",
        ("Nestlé", "АТЦ", "100см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_100_atc.jpg",
        ("Nestlé", "АТЦ", "120см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_120_atc.jpg",
        ("Nestlé", "АТЦ", "150см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_150_atc.jpg",
        ("Nestlé", "АТЦ", "160см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_160_atc.jpg",
        ("Nestlé", "АТЦ", "180см"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_180_atc.jpg",
        ("Nestlé", "АТЦ", "Вертикален"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Nestle_vert_atc.jpg",
    }

    image_url = planogram_links.get((search_brand, search_target, freezer_size))

    if image_url:
        st.markdown(f"""
            <div style='border: 4px solid white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
                <img src='{image_url}' style='width: 100%; display: block;'>
            </div>
            <a href="{image_url}" target="_blank" class="zoom-btn">🔍 УВЕЛИЧИ (ZOOM)</a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Снимката не е намерена.")

st.markdown("<br><hr><center><small>© 2026 Ice Cream Sales Team</small></center>", unsafe_allow_html=True)
