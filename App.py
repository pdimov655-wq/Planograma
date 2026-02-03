import streamlit as st

# 1. Основна конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ПРОФЕСИОНАЛЕН ДИЗАЙН СЪС ЗАЩИТА ОТ DARK MODE ---
st.markdown("""
    <style>
    /* Скриване на системни менюта */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ФОРСИРАНЕ НА СВЕТЛА ТЕМА (Force Light Theme) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #f8f9fa !important;
    }

    /* Фиксиране на основния цвят на текста */
    .stMarkdown, p, label, .stSelectbox label, .stRadio label {
        color: #1e3a8a !important;
        font-weight: 600 !important;
    }

    /* Стилизиране на белите контейнери за избор */
    [data-testid="stVerticalBlock"] > div > div > div.stSelectbox, 
    [data-testid="stVerticalBlock"] > div > div > div.stRadio {
        background-color: white !important;
        padding: 20px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        border: 1px solid #e0e0e0 !important;
    }

    /* Стилизиране на бутоните */
    div.stButton > button:first-child {
        background-color: #0046ad !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important;
        width: 100% !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }

    /* Фиксиране на цветовете в падащите менюта (Selectbox) */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: #1e3a8a !important;
    }

    /* Заглавие */
    h1 {
        color: #1e3a8a !important;
        text-align: center !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* Инфо съобщения */
    .stAlert {
        background-color: #e3f2fd !important;
        color: #0d47a1 !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД ---
if "password_correct" not in st.session_state:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><h2 style='text-align: center; color: #1e3a8a;'>🔒 Вход</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Въведете парола", type="password")
        if st.button("ВЛЕЗ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<h1>🍦 Дигитален Асистент за Планограми</h1>", unsafe_allow_html=True)

# Изход в страничното меню
with st.sidebar:
    if st.button("Изход (Logout)"):
        del st.session_state["password_correct"]
        st.rerun()

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📋 Параметри")
    
    # 1. Тип клиент
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

    # Логика за скриване на менютата при Гондола
    is_gondola = "Гондола" in specific_layout
    
    freezer_size = "N/A"
    brand = "Mix"

    if not is_gondola:
        st.write("**2. Размер на фризера:**")
        freezer_size = st.radio(
            "", 
            ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], 
            horizontal=True
        )
        
        st.write("**3. Марка:**")
        brand = st.radio("", ["Milka", "Nestlé"], horizontal=True)
    else:
        st.info("💡 Гондолите са със смесено излагане (Mix).")

with col2:
    st.subheader("🖼️ Визуализация")
    
    # Подготовка на избора
    if is_gondola:
        current_selection = f"Микс Продукти | {specific_layout}"
        search_brand = "Mix"
        search_target = specific_layout
    else:
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        search_brand = brand
        search_target = sub_channel
        
    st.info(f"📍 Избор: **{current_selection}**")

    if st.button("📊 ВИЖ ПЛАНОГРАМА"):
        with st.spinner('Зареждане на изображението...'):
            
            planogram_links = {
                # ОМВ Гондола 4х11
                ("Mix", "Гондола 4х11", "N/A"): "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/%D0%9E%D0%BC%D0%B2%204x11.jpg",
            }

            image_url = planogram_links.get((search_brand, search_target, freezer_size))

            if image_url:
                st.image(image_url, caption=current_selection, use_container_width=True)
            else:
                st.warning("⚠️ Снимката все още не е качена в базата данни.")
                st.image("https://via.placeholder.com/800x500.png?text=No+Planogram+Available", use_container_width=True)

st.markdown("<br><hr><center><small style='color: #1e3a8a;'>© 2026 Ice Cream Sales Team | V 1.8</small></center>", unsafe_allow_html=True)
