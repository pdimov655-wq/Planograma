import streamlit as st

# 1. Конфигурация
st.set_page_config(
    page_title="Ice Cream Planogram Pro", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ПРОФЕСИОНАЛЕН ДИЗАЙН (CSS) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #f8f9fa; }
    div.stButton > button:first-child {
        background-color: #0046ad;
        color: white;
        border-radius: 12px;
        height: 50px;
        width: 100%;
        font-weight: bold;
    }
    .stSelectbox, .stRadio {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    h1 { color: #1e3a8a; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД ---
if "password_correct" not in st.session_state:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h2 style='text-align: center;'>🔒 Вход</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Парола", type="password")
        if st.button("ВЛЕЗ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Грешна парола!")
    st.stop()

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.title("🍦 Дигитален Асистент за Планограми")

with st.sidebar:
    if st.button("Изход"):
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

    # ЛОГИКА ЗА СКРИВАНЕ: Показваме размерите само ако НЕ е избрана Гондола
    is_gondola = "Гондола" in specific_layout
    
    freezer_size = "N/A" # Стойност по подразбиране за Гондола
    if not is_gondola:
        st.write("**2. Размер на фризера:**")
        freezer_size = st.radio(
            "", 
            ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], 
            horizontal=True
        )
    else:
        st.info("ℹ️ При избор на Гондола размерите на фризера са фиксирани.")

    # 3. Марка
    brand = st.radio("3. Марка", ["Milka", "Nestlé"], horizontal=True)

with col2:
    st.subheader("🖼️ Визуализация")
    
    # Формиране на име за избор
    display_name = specific_layout if is_gondola else sub_channel
    current_selection = f"{brand} | {display_name}"
    if not is_gondola:
        current_selection += f" | {freezer_size}"
        
    st.info(f"📍 Избор: **{current_selection}**")

    if st.button("📊 ВИЖ ПЛАНОГРАМА"):
        with st.spinner('Зареждане...'):
            # Речникът вече включва търсене по тип излагане или канал
            planogram_links = {
                ("Milka", "Гондола 4х11", "N/A"): "https://raw.githubusercontent.com/user/repo/main/images/milka_gondola_4x11.jpg",
                ("Milka", "ОМВ", "120см"): "https://raw.githubusercontent.com/user/repo/main/images/milka_omv_120.jpg",
                # Добави останалите линкове тук
            }

            search_target = specific_layout if is_gondola else sub_channel
            image_url = planogram_links.get((brand, search_target, freezer_size))

            if image_url:
                st.image(image_url, caption=current_selection, use_container_width=True)
            else:
                st.warning("⚠️ Няма качена снимка за този избор.")
                st.image("https://via.placeholder.com/800x500.png?text=No+Planogram", use_container_width=True)

st.markdown("<br><hr><center><small>© 2026 Ice Cream Sales Team | V 1.5</small></center>", unsafe_allow_html=True)
