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
    /* Вмъкване на модерен шрифт от Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none !important;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0) !important;}
    
    /* Прилагане на новия шрифт за цялото приложение */
    html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, label, h1, h2, h3, button, select, input {
        font-family: 'Inter', sans-serif !important;
    }
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
        }}
        h2, p {{ color: white !important; font-weight: 600; }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        st.markdown(f"""
            <div class='login-card'>
                <h2 style='font-size: 2rem; letter-spacing: -1px;'>🔒 Влез в системата</h2>
                <p>Digital Sales Support Tool</p>
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

# --- ДИЗАЙН ЗА ОСНОВНОТО МЕНЮ С ФОН 2 И НОВ ШРИФТ ---
main_menu_bg = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/Main_backgroung.jpg"

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(248, 249, 250, 0.85), rgba(248, 249, 250, 0.85)), url("{main_menu_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Белите карти с избори */
    [data-testid="stVerticalBlock"] > div > div > div.stSelectbox, 
    [data-testid="stVerticalBlock"] > div > div > div.stRadio {{
        background-color: white !important;
        padding: 20px !important;
        border-radius: 18px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
        border: 1px solid rgba(0,0,0,0.05) !important;
    }}

    /* Стил на текста в основното меню */
    h1, h3, label {{
        color: #002d72 !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }}

    .zoom-btn {{
        display: block;
        background: #0046ad;
        color: white !important;
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        text-decoration: none;
        font-weight: 700;
        margin-top: 15px;
        font-size: 1.1rem;
        transition: 0.3s;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1 style='text-align: center; font-size: 2.5rem;'>🍦 Planogram Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    if st.button("Изход"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📋 Избери параметри")
    client_type = st.selectbox("📌 Тип на клиента", ["ТТ", "АТЦ", "Петролен канал"])
    
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
        st.info("💡 Гондолите използват комбинирано излагане (Mix).")

with col2:
    st.subheader("🖼️ Визуализация")
    
    if is_gondola:
        current_selection = f"MIX • {specific_layout}"
    else:
        current_selection = f"{brand.upper()} • {sub_channel.upper()} • {freezer_size}"
        
    st.info(f"📍 Избор: **{current_selection}**")

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

    image_url = planogram_links.get((brand if not is_gondola else "Mix", sub_channel if not is_gondola else specific_layout, freezer_size))

    if image_url:
        st.markdown(f"""
            <div style='border: 8px solid white; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.15);'>
                <img src='{image_url}' style='width: 100%; display: block;'>
            </div>
            <a href="{image_url}" target="_blank" class="zoom-btn">🔍 ПРЕГЛЕД НА ЦЯЛ ЕКРАН</a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Снимката не е налична.")

st.markdown("<br><center><small style='color: #1e3a8a;'>© 2026 FRONERI SALES SUPPORT</small></center>", unsafe_allow_html=True)
