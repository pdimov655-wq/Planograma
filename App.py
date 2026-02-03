import streamlit as st

st.title("🍦 Планограми Сладолед")

# Избор на тип клиент
client = st.selectbox("Тип клиент:", ["ТТ", "АТЦ", "Бензиностанция"])

# Избор на размер
size = st.select_slider("Размер на фризера (см):", options=["100", "120", "150", "180"])

# Избор на марка
brand = st.radio("Изберете бранд:", ["Milka", "Nestle"], horizontal=True)

st.divider()

# Резултат
st.subheader(f"План за {brand} ({size}см)")
st.info(f"📍 Обект: {client}")

# Тук можеш да опишеш кои продукти къде се слагат
if brand == "Milka":
    st.write("✅ Ред 1: Milka Hazelnut, Milka Caramel")
    st.write("✅ Ред 2: Oreo Stick, Milka Choco Wafer")
else:
    st.write("✅ Ред 1: Familia Vanilla, Nirvana Chocolate")
    st.write("✅ Ред 2: Boss Ice Cream, Aloma")
