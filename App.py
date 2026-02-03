import streamlit as st

# 1. Основна конфигурация и дизайн
st.set_page_config(page_title="Ice Cream Planogram Pro", page_icon="🍦", layout="wide")

# Custom CSS за професионален изглед
st.markdown("""

    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stSelectbox, .stRadio {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ПРОВЕРКА НА ПАРОЛА ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h2 style='text-align: center;'>Вход в системата</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            pwd = st.text_input("Парола", type="password")
            if st.button("Влез"):
                if pwd == "ice123":
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("Грешна парола")
        return False
    return True

if check_password():
    # --- СТРАНИЧНА ЛЕНТА (SIDEBAR) ---
    with st.sidebar:
        st.image("https://via.placeholder.com/150x80.png?text=LOGO", use_container_width=True)
        st.title("Навигация")
        st.info("Използвайте менюто за избор на обект и фризер.")
        if st.button("Изход"):
            del st.session_state["password_correct"]
            st.rerun()

    # --- ОСНОВНА ЧАСТ ---
    st.title("🍦 Планограми: Дигитален Асистент")
    
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("📋 Параметри на обекта")
        client_type = st.selectbox("Тип на клиента", ["ТТ", "АТЦ", "Петролен канал"])
        
        if client_type == "Петролен канал":
            sub_channel = st.selectbox("Верига бензиностанции", ["OMV", "Shell", "Lukoil", "Rompetrol", "Petrol", "Others"])
        else:
            sub_channel = client_type

        freezer_size = st.radio("Размер на фризера", ["100см", "120см", "150см", "180см"], horizontal=True)
        brand = st.radio("Избор на бранд", ["Milka", "Nestlé"], horizontal=True)

    with col2:
        st.subheader("🖼️ Визуализация")
        st.write("") # Празно пространство за подравняване
        
        # Бутон с икона
        if st.button("📊 ГЕНЕРИРАЙ ПЛАН"):
            with st.spinner('Зареждане на планограмата...'):
                # Тук поставяш логиката за линковете (както в предишния пример)
                # За демонстрация използваме placeholder:
                st.success(f"Готов план за {sub_channel} ({freezer_size})")
                st.image("https://via.placeholder.com/600x400.png?text=Planogram+View", use_container_width=True)
                
                # Допълнителна професионална опция:
                st.download_button(label="📥 Изтегли PDF за принтиране", 
                                 data="Sample Data", 
                                 file_name=f"Planogram_{sub_channel}.pdf")

    # Футър
    st.markdown("---")
    st.caption("© 2026 Търговски отдел | Всички права запазени")
    
