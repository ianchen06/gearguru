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

st.markdown(
    """
# Analyze Your Closet

- Users upload photos of clothing (both winter-specific and general).
- Computer vision recognizes items, brands, and materials.
- Large language model delivers insights:
    - Sustainability report
        - Environmental impact of materials and manufacturing.
        - Supply chain ethics
        - Estimated garment lifespan
    - Care and prolong the life
        - Care instructions to maximize longevity
        - Repair and upcycling tips
"""
)
