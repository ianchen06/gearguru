import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_carousel import carousel



st.set_page_config(
    page_title="Winter Gear Guru | Eco-Friendly Gear Analysis",
    page_icon="⛷️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("⛷️ Winter Gear Guru")

# st.image("images/home.jpg", use_column_width=True)
interval = 2000
test_items = [
    dict(
        title="",
        text="",
        interval=interval,
        img="https://i.imgur.com/tMjs2gB.jpeg",
    ),
    dict(
        title="",
        text="",
        interval=interval,
        img="https://i.imgur.com/QlkPJwP.jpeg",
    ),
    dict(
        title="",
        text="",
        interval=interval,
        img="https://i.imgur.com/cLl406G.jpeg",
    ),
    dict(
        title="",
        text="",
        interval=interval,
        img="https://i.imgur.com/geeh6wN.jpeg",
    ),
]

carousel(items=test_items, width=1)

st.sidebar.success("Select a page above.")


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (
        url
    )
    st.write(nav_script, unsafe_allow_html=True)


st.header("Main Features")

st.markdown(
    """
  <style>

    /*the main div*/
    .element-container {
        text-align: center;
    }
  
  </style>
""",
    unsafe_allow_html=True,
)
cols = st.columns(3)
with cols[0]:
    with stylable_container(
        key="features-container",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/gear.webp", use_column_width=True)
    st.button(
        "Eco friendly gear analysis",
        type="primary",
        on_click=lambda: nav_to("/Gear_Analyzer"),
    )
with cols[1]:
    with stylable_container(
        key="features-container2",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/chat.webp", use_column_width=True)
    st.button("Chat with Gear Guru", type="primary", on_click=lambda: nav_to("/Chat"))
with cols[2]:
    with stylable_container(
        key="features-container3",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/about.webp", use_column_width=True)
    st.button(
        "Learn how to protect our winters",
        type="primary",
        on_click=lambda: nav_to("/About"),
    )
