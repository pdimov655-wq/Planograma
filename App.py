import streamlit as st

# 1. Основна конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- СТРОГО СКРИВАНЕ НА СИСТЕМНИ ЕЛЕМЕНТИ ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none !important;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0) !important;}
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД С ФОН 1 ---
if "password_correct" not in st.session_state:
    login_bg = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/froneri-brand-images.jpg"

    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("{login_bg}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .login-card {{
            background: rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(15px);
            padding: 40px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            text-align: center;
            margin-top: 50px;
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        st.markdown(f"""
            <div class='login-card'>
                <h2 style='color: white;'>🔒 Вход</h2>
                <p style='color: white;'>Въведете парола</p>
            </div>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("", type="password", placeholder="Парола...")
        
        if st.button("ВЛЕЗ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- ДИЗАЙН ЗА ОСНОВНОТО МЕНЮ С НОВ ФОН 2 ---
main_menu_bg = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Main_backgroung.jpg"

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(248, 249, 250, 0.85), rgba(248, 249, 250, 0.85)), url("{main_menu_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Стил за белите карти с параметри */
    [data-testid="stVerticalBlock"] > div > div > div.stSelectbox, 
    [data-testid="stVerticalBlock"] > div > div > div.stRadio {{
        background-color: white !important;
        padding: 20px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        border: 1px solid #e0e0e0 !important;
        margin-bottom: 15px !important;
    }}

    .stMarkdown, p, label, h1, h3 {{
        color: #1e3a8a !important;
        font-weight: 600 !important;
    }}

    .zoom-btn {{
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
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1 style='text-align: center;'>🍦 Дигитален Асистент за Планограми</h1>", unsafe_allow_html=True)

with st.sidebar:
    if st.button("Изход (Logout)"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📋 Параметри")
    client_type = st.selectbox("1. Тип на клиента", ["ТТ", "АТЦ", "Петролен канал"])
    
    sub_channel = client_type
    specific_layout = "Стандартен фризер"

    if client_type == "Петролен канал":
        sub_channel = st.selectbox("Изберете верига", ["ОМВ", "Лукойл"])
        if sub_channel == "ОМВ":
            specific_layout = st.selectbox(
                "Тип излагане (ОМВ):", 
                ["Стандартен фризер", "Гондола 4х11", "Гондола 4х8", "Гондола 4х4"]
            )

    is_gondola = "Гондола" in specific_layout
    freezer_size, brand = "N/A", "Mix"

    if not is_gondola:
        st.write("**2. Размер на фризера:**")
        freezer_size = st.radio("", ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], horizontal=True)
        st.write("**3. Марка:**")
        brand = st.radio("", ["Milka", "Nestlé"], horizontal=True)
    else:
        st.info("💡 Гондолите са със смесено излагане (Mix).")

with col2:
    st.subheader("🖼️ Визуализация")
    
    if is_gondola:
        current_selection = f"Микс Продукти | {specific_layout}"
        search_brand, search_target = "Mix", specific_layout
    else:
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        search_brand, search_target = brand, sub_channel
        
    st.info(f"📍 Избор: **{current_selection}**")

    # --- БАЗА ДАННИ С ПЛАНОГРАМИ ---
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
        st.warning("⚠️ Снимката все още не е качена.")

st.markdown("<br><hr><center><small>© 2026 Ice Cream Sales Team</small></center>", unsafe_allow_html=True)
