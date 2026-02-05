import streamlit as st

# 1. Основна конфигурация
st.set_page_config(
    page_title="Planogram Pro v4.1", 
    page_icon="🍦", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- PREMIUM UI/UX ДИЗАЙН С БУТОНИ (CHIPS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
        font-family: 'Inter', sans-serif !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display: none !important;}

    /* СТИЛИЗИРАНЕ НА РАДИО БУТОНИТЕ КАТО ПЛОЧКИ (CHIPS) */
    div[data-testid="stRadio"] > div {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 10px !important;
    }

    div[data-testid="stRadio"] label {
        background-color: white !important;
        border: 2px solid #0046ad !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        color: #0046ad !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }

    /* Стил при избран бутон - СВЕТВА В СИНЬО */
    div[data-testid="stRadio"] label[data-selected="true"] {
        background-color: #0046ad !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(0, 70, 173, 0.3) !important;
    }

    /* Скриване на малките кръгчета на оригиналното радио */
    div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0 !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > div > div:first-child {
        display: none !important;
    }

    /* Заглавия и карти */
    .main-title {
        color: #1e3a8a;
        font-weight: 800;
        font-size: 2rem;
        text-align: center;
        margin-bottom: 25px;
    }

    .config-card {
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .selection-tag {
        background: #0046ad;
        color: white;
        padding: 8px 15px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 15px;
        display: inline-block;
    }

    .zoom-btn {
        display: block;
        background: linear-gradient(90deg, #0046ad, #0072ff);
        color: white !important;
        padding: 18px;
        border-radius: 15px;
        text-align: center;
        text-decoration: none;
        font-weight: 800;
        margin-top: 20px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- СИСТЕМА ЗА ВХОД (Бърза проверка) ---
if "password_correct" not in st.session_state:
    bg_image = "https://raw.githubusercontent.com/pdimov655-wq/Planograma/refs/heads/main/Images/froneri-brand-images.jpg"
    st.markdown(f"<style>[data-testid='stAppViewContainer'] {{ background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{bg_image}'); background-size: cover; }}</style>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.1, 1, 0.1])
    with col2:
        st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: white; text-align: center;'>🍦 Planogram Pro</h1>", unsafe_allow_html=True)
        pwd = st.text_input("Парола", type="password")
        if st.button("ВЛЕЗ"):
            if pwd == "ice123":
                st.session_state["password_correct"] = True
                st.rerun()
    st.stop()

# --- ГЛАВЕН ИНТЕРФЕЙС ---
st.markdown("<div class='main-title'>🍦 Digital Assistant</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### ⚙️ ИЗБЕРЕТЕ ПАРАМЕТРИ")
    
    # 1. ТИП КЛИЕНТ (ВЕЧЕ С БУТОНИ)
    st.write("**📍 Тип на клиента:**")
    client_type = st.radio("", ["ТТ", "АТЦ", "Петролен канал"], horizontal=True, key="client_type")
    
    sub_channel = client_type
    specific_layout = "Стандартен фризер"

    # 2. ПОДКАНАЛ (Ако е Петролен)
    if client_type == "Петролен канал":
        st.write("**⛽ Верига:**")
        sub_channel = st.radio("", ["ОМВ", "Лукойл"], horizontal=True, key="petrol_chain")
        if sub_channel == "ОМВ":
            st.write("**🧊 Тип излагане:**")
            specific_layout = st.radio("", ["Стандартен", "Гондола 4х11", "Гондола 4х8", "Гондола 4х4"], horizontal=True)

    is_gondola = "Гондола" in specific_layout
    freezer_size, brand = "N/A", "Mix"

    if not is_gondola:
        st.markdown("---")
        st.write("**📐 Размер на фризера:**")
        freezer_size = st.radio("", ["80см", "100см", "120см", "150см", "160см", "180см", "Вертикален"], horizontal=True, key="size")
        
        st.write("**🏷️ Марка:**")
        brand = st.radio("", ["Milka", "Nestlé"], horizontal=True, key="brand")

with col2:
    st.markdown("### 📸 ПРЕГЛЕД")
    
    # Генериране на описание
    if is_gondola:
        current_selection = f"MIX • {specific_layout}"
        search_brand, search_target = "Mix", specific_layout
    else:
        current_selection = f"{brand.upper()} • {sub_channel} • {freezer_size}"
        search_brand, search_target = brand, sub_channel
        
    st.markdown(f"<div class='selection-tag'>📍 {current_selection}</div>", unsafe_allow_html=True)

    # БАЗА ДАННИ
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
            <div style='border: 6px solid white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);'>
                <img src='{image_url}' style='width: 100%; display: block;'>
            </div>
            <a href="{image_url}" target="_blank" class="zoom-btn">🔍 УВЕЛИЧИ СНИМКАТА</a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Липсва планограма за този избор.")

st.markdown("<br><center><p style='color: #7f8c8d; font-size: 0.8rem;'>© 2026 FRONERI SALES TOOL</p></center>", unsafe_allow_html=True)
