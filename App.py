import streamlit as st

# 1. Конфигурация на страницата
st.set_page_config(page_title="Ice Cream Planograms", page_icon="🍦")

# --- ФУНКЦИЯ ЗА ПАРОЛА ---
def check_password():
    """Връща True, ако потребителят е въвел правилната парола."""
    def password_entered():
        if st.session_state["password"] == "ice123": # <--- ТВОЯТА ПАРОЛА ТУК
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Изтриваме паролата от състоянието за сигурност
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Първо показване, въвеждане на парола
        st.text_input("Въведете парола за достъп:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Сгрешена парола
        st.text_input("Грешна парола! Опитайте отново:", type="password", on_change=password_entered, key="password")
        st.error("❌ Достъпът е отказан")
        return False
    else:
        # Паролата е вярна
        return True

# --- ПРОВЕРКА НА ДОСТЪПА ---
if check_password():
    # АКО ПАРОЛАТА Е ВЯРНА, СЕ ПОКАЗВА ПРИЛОЖЕНИЕТО:
    st.title("🍦 Асистент за Планограми")
    
    # Селектори
    client_type = st.selectbox("1. Тип клиент:", ["ТТ", "АТЦ", "Бензиностанция"])
    freezer_size = st.radio("2. Размер на фризера:", ["100см", "120см", "150см", "180см"], horizontal=True)
    brand_choice = st.radio("3. Бранд:", ["Milka", "Nestle"], horizontal=True)

    st.divider()

    # Логика за снимките
    # Замени 'link_to_image' с реалните линкове от GitHub
    planogram_images = {
        ("Milka", "100см"): "https://raw.githubusercontent.com/user/repo/main/milka100.jpg",
        ("Milka", "120см"): "https://raw.githubusercontent.com/user/repo/main/milka120.jpg",
        ("Nestle", "100см"): "https://raw.githubusercontent.com/user/repo/main/nestle100.jpg",
        # Добави останалите тук...
    }

    if st.button("Покажи планограма"):
        image_url = planogram_images.get((brand_choice, freezer_size))
        
        if image_url and "raw.githubusercontent" in image_url:
            st.image(image_url, caption=f"План за {brand_choice} - {freezer_size}")
        else:
            st.warning(f"Снимката за {brand_choice} ({freezer_size}) още не е качена.")
            st.info("След като качиш снимките в GitHub, сложи техните 'Raw' линкове в кода.")

    # Бутон за изход
    if st.sidebar.button("Изход (Logout)"):
        st.session_state["password_correct"] = False
        st.rerun()
