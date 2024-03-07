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

st.subheader("⛷️ Winter Gear Guru")

cols = st.columns([6, 6])
with cols[0]:
    st.markdown("<div><br><br></div>", unsafe_allow_html=True)
    st.markdown("# Sustainable Winter Sports Essentials with AI Precision")
    st.write(
        "Empower Your Adventures with Eco-Friendly Choices - Smart, Sustainable, and Supported by AI Technology"
    )
    st.markdown("<div><br></div>", unsafe_allow_html=True)
    colz = st.columns([1, 1, 1])
    colz[0].button(
        "Gear Analysis",
        type="primary",
        on_click=lambda: nav_to("/Gear_Analyzer"),
    )
    colz[1].button("Chat with Gear Guru", on_click=lambda: nav_to("/Chat"))
    colz[2].button(
        "Learn More",
        on_click=lambda: nav_to("/About"),
    )


with cols[1]:
    with stylable_container(
        key="top-right-container",
        css_styles="""img {border-radius: 25px;}""",
    ):
        st.image("images/sber.webp", use_column_width=True)

st.sidebar.success("Select a page above.")


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (
        url
    )
    st.write(nav_script, unsafe_allow_html=True)


st.divider()

st.header("Eco-Friendly Gear Guide")
st.markdown("Combining cutting-edge AI with a commitment to sustainability, our app revolutionizes how you choose winter sports equipment.")
st.markdown("<div><br><br></div>", unsafe_allow_html=True)

cols = st.columns(3)
with cols[0]:
    with stylable_container(
        key="features-container",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/gear.webp", use_column_width=True)
    with stylable_container(
        key="features-container",
        css_styles="""{text-align: center;}""",
    ):
        st.button(
            "Eco friendly gear analysis",
            key="gear-analyzer",
            type="primary",
            on_click=lambda: nav_to("/Gear_Analyzer"),
        )
with cols[1]:
    with stylable_container(
        key="features-container2",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/chat.webp", use_column_width=True)
    with stylable_container(
        key="features-container",
        css_styles="""{text-align: center;}""",
    ):
        st.button(
            "Chat with Gear Guru", type="primary", on_click=lambda: nav_to("/Chat")
        )
with cols[2]:
    with stylable_container(
        key="features-container3",
        css_styles="""img {border-radius: 50%;}""",
    ):
        st.image("images/about.webp", use_column_width=True)
    with stylable_container(
        key="features-container",
        css_styles="""{text-align: center;}""",
    ):
        st.button(
            "Learn how to protect our winters",
            type="primary",
            on_click=lambda: nav_to("/About"),
        )

st.divider()


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


carousel(items=test_items, height=600, width=1)