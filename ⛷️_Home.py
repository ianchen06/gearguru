import streamlit as st


st.set_page_config(
    page_title="Winter Gear Guru | Eco-Friendly Gear Analysis",
    page_icon="⛷️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("⛷️ Winter Gear Guru")

st.image("images/home.jpg", use_column_width=True)

st.sidebar.success("Select a page above.")

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

st.header("Main Features")

cols = st.columns(3)
with cols[0]:
    st.image("images/gear.webp", use_column_width=True)
    st.button("Eco friendly gear analysis", type="primary", on_click=lambda: nav_to("/Gear_Analyzer"))
with cols[1]:
    st.image("images/chat.webp", use_column_width=True)
    st.button("Chat with Gear Guru", type="primary", on_click=lambda: nav_to("/Chat"))
with cols[2]:
    st.image("images/about.webp", use_column_width=True)
    st.button("Learn how to protect our winters", type="primary", on_click=lambda: nav_to("/About"))