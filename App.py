import streamlit as st

# Конфигурация на страницата
st.set_page_config(page_title="Ice Cream Planograms", page_icon="🍦")

# --- ФУНКЦИЯ ЗА ПАРОЛА ---
def check_password():
    def password_entered():
        if st.session_state["password"] == "ice123": # <--- ТВОЯТА ПАРОЛА
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Въведете парола за достъп:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Грешна парола! Опитайте отново:", type="password", on_change=password_entered, key="password")
        st.error("❌ Достъпът е отказан")
        return False
    else:
        return True

# --- ОСНОВНО ПРИЛОЖЕНИЕ ---
if check_password():
    st.title("🍦 Асистент за Планограми")
    
    # 1. Тип клиент (Заменено с Петролен канал)
    client_type = st.selectbox(
        "1. Изберете тип на клиента:",
        ["ТТ", "АТЦ", "Петролен канал"]
    )

    # 2. ПОДМЕНЮ ЗА БЕНЗИНОСТАНЦИИ (Показва се само при избор на Петролен канал)
    sub_channel = None
    if client_type == "Петролен канал":
        sub_channel = st.selectbox(
            "Изберете верига:",
            ["OMV", "Shell", "Lukoil", "Rompetrol", "Petrol", "Others"]
        )

    # 3. Размер на фризера
    freezer_size = st.radio("2. Размер на фризера:", ["100см", "120см", "150см", "180см"], horizontal=True)

    # 4. Бранд
    brand_choice = st.radio("3. Изберете марка:", ["Milka", "Nestlé"], horizontal=True)

    st.divider()

    # Потвърждение на избора
    selection_text = f"{brand_choice} | {freezer_size} | {client_type}"
    if sub_channel:
        selection_text += f" ({sub_channel})"
    
    st.info(f"📍 Избран план: **{selection_text}**")

    # --- ЛОГИКА ЗА СНИМКИТЕ ---
    # Тук можеш да добавиш специфични снимки дори за отделните вериги
    if st.button("ВИЖ ПЛАНОГРАМА"):
        # Примерна логика: ако е OMV, можеш да заредиш специална снимка
        if sub_channel == "OMV" and brand_choice == "Milka":
            st.warning("Показване на специфична планограма за OMV...")
            # st.image("link_to_omv_milka_image")
        else:
            st.info("Зареждане на стандартна планограма за канала...")
            # Тук ще бъде твоят стандартен механизъм със снимките, който обсъдихме
            st.image("https://via.placeholder.com/800x400.png?text=Planogram+Placeholder", 
                     caption=selection_text)

    # Logout бутон в страничното меню
    if st.sidebar.button("Изход"):
        st.session_state["password_correct"] = False
        st.rerun()
