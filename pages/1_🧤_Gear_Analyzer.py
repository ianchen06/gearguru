import os

import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm

from PIL import Image

st.set_page_config(
    page_title="Winter Gear Crew | Eco-Friendly Gear Analysis",
    page_icon="⛷️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("⛷️ Winter Gear Crew")
st.write("Upload an image of winter sports gear to get sustainability advice!")

with st.expander("ℹ️ About this App"):
    st.write(
        """
    This app uses AI to provide sustainability advice for winter sports gear. 
    Upload an image of winter sports gear, and the app will generate a short, engaging blog post based on the picture. 
    The AI model will analyze the image and provide sustainability advice for the gear shown in the picture.
    """
    )

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro-vision")


uploaded_file = st.file_uploader(
    "Choose an Image file", accept_multiple_files=False, type=["jpg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)
    bytes_data = uploaded_file.getvalue()

generate = st.button("Get Sustainability Advice", type="primary")

if generate:
    with st.spinner("Generating sustainability advice..."):
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content(
            glm.Content(
                parts=[
                    glm.Part(
                        text="""Based on the image, perform the following tasks:
- Identify the gear
    - Brand and model
- Sustainability report
    - Environmental impact of materials and manufacturing.
    - Supply chain ethics
    - Estimated garment lifespan
- Care and prolong the life
    - Care instructions to maximize longevity
    - Repair and upcycling tips
                    """
                    ),
                    glm.Part(
                        inline_data=glm.Blob(mime_type="image/jpeg", data=bytes_data)
                    ),
                ],
            ),
            stream=True,
        )

        response.resolve()

        st.write(response.text)
