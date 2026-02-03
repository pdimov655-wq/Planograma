import streamlit as st

# 1. Основна конфигурация и дизайн
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ПРОФЕСИОНАЛЕН ДИЗАЙН (CSS) ---
st.markdown("""
    <style>
    /* Скриване на системните менюта на Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Основен стил */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Стилизиране на бутоните */
    div.stButton > button:first-child {
        background-color: #0046ad;
        color: white;
        border-radius: 12px;
        border: none;
        height: 50px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #003087;
        border: none;
        color: white;
    }

    /* Стилизиране на белите контейнери за избор */
    .stSelectbox, .stRadio {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    
    /* Заглавия */
    h1 {
        color: #1e3a8a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД (ПАРОЛА) ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<h2 style='text-align: center;'>🔒 Вход в системата</h2>", unsafe_allow_html=True)
            pwd = st.text_input("Въведете парола за достъп", type="password")
            if st.button("ВЛЕЗ"):
                if pwd == "ice123": # <--- Парола
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Грешна парола! Опитайте отново.")
        return False
    return True

# --- ГЛАВЕН ИНТЕРФЕЙС ---
if check_password():
    # Заглавие
    st.title("🍦 Дигитален Асистент за Планограми")
    
    # Изход в страничното меню
    with st.sidebar:
        st.markdown("### Потребителски панел")
        if st.button("Изход (Logout)"):
            del st.session_state["password_correct"]
            st.rerun()

    # Разпределение на екрана
    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.subheader("📋 Избор на параметри")
        
        # 1. Избор на канал
        client_type = st.selectbox("1. Тип на клиента", ["ТТ", "АТЦ", "Петролен канал"])
        
        # Динамично подменю за бензиностанции (Само ОМВ и Лукойл)
        sub_channel = None
        if client_type == "Петролен канал":
            sub_channel = st.selectbox("Изберете верига", ["ОМВ", "Лукойл"])
        else:
            sub_channel = client_type

        # 2. Размер на фризера (Добавени 80см, 160см и Вертикален)
        freezer_size = st.radio(
            "2. Размер на фризера", 
            ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], 
            horizontal=False # Списъкът стана дълъг, вертикално е по-прегледно
        )

        # 3. Марка
        brand = st.radio("3. Изберете марка", ["Milka", "Nestlé"], horizontal=True)

    with col2:
        st.subheader("🖼️ Планограма за обекта")
        
        # Потвърждение на селекцията
        current_selection = f"{brand} | {sub_channel} | {freezer_size}"
        st.info(f"📍 Текущ избор: **{current_selection}**")

        # БУТОН ЗА ГЕНЕРИРАНЕ
        if st.button("📊 ВИЖ ПЛАНОГРАМА"):
            with st.spinner('Зареждане на изображението...'):
                
                # Тук описвате линковете към снимките
                planogram_links = {
                    ("Milka", "ОМВ", "120см"): "https://raw.githubusercontent.com/user/repo/main/images/milka_omv_120.jpg",
                    ("Nestlé", "Лукойл", "Вертикален"): "https://raw.githubusercontent.com/user/repo/main/images/nestle_lukoil_vert.jpg",
                }

                image_url = planogram_links.get((brand, sub_channel, freezer_size))

                if image_url and "raw.githubusercontent" in image_url:
                    st.image(image_url, caption=f"Одобрена подредба за {current_selection}", use_container_width=True)
                else:
                    st.warning("⚠️ Не е намерена специфична планограма за този избор.")
                    st.image("https://via.placeholder.com/800x500.png?text=No+Planogram+Available", use_container_width=True)

    # Футър
    st.markdown("<br><hr><center><small>© 2026 Ice Cream Sales Team | Version 1.3</small></center>", unsafe_allow_html=True)
