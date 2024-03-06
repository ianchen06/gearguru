import streamlit as st


st.set_page_config(
    page_title="Winter Gear Guru | Eco-Friendly Gear Analysis",
    page_icon="⛷️",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("⛷️ Winter Gear Guru")

st.image("images/home.jpg", use_column_width=True)

st.sidebar.success("Select a page above.")

st.button("Get Eco friendly gear advice", type="primary")
