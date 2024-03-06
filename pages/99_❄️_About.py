import streamlit as st
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from dotenv import load_dotenv

load_dotenv()

tabs = st.tabs(["About", "Chat"])

with tabs[0]:
    st.markdown("""
    # ❄️ Protect Our Winters
                
    <iframe width="560" height="315" src="https://www.youtube.com/embed/40-XKQa4RBc?si=TlHWVylo9MurbOyL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

    ## History

    - Founded in 2007 by professional snowboarder Jeremy Jones.
    - Grew out of the realization that climate change was directly impacting the snowpack and winter sports Jones and others relied on.
    - Has expanded into a global network with country-specific chapters (US, Canada, UK, France, etc.).

    ## Mission

    POW helps passionate outdoor people protect the places and lifestyles they love from climate change through non-partisan advocacy.

    ## Vision

    A future where the outdoor sports community leads the charge toward positive climate action, protecting outdoor spaces, and securing a healthy planet for all.

    ## How to Contribute

    - **Utilize Your Platform**: Share POW's mission and campaigns through your blog, website, social media, or other channels. Create content that highlights the connection between climate change and the outdoor experience.
    - ***Engage Your Community**: Encourage your followers to become POW members, take action on climate policies, and make sustainable lifestyle choices.
    - **Partner with Local POW Chapter**: If there's a POW chapter in your area, reach out to collaborate on events, content initiatives, and local advocacy efforts.
    - **Become a POW Alliance Member**: Depending on your role, consider joining POW's Athlete Alliance, Creative Alliance, Brand Alliance or the Science Alliance. These offer opportunities to engage in deeper collaboration.
    - **Start a Local Chapter**: If there isn't a POW chapter in your region, explore starting one to lead advocacy and initiatives in your community.

    ## Additional Ideas

    - **Climate Change Impacts**: Document how climate change is impacting your favorite outdoor places.
    - **Interviews**: Connect with POW athletes, scientists, and partners to discuss their work.
    - **Sustainability Tips**: Share simple actions people can take to minimize their environmental impact as outdoor enthusiasts
    - **Advocacy Guides**: Create content explaining how your audience can get their voices heard on climate policy.

    ## Important Links

    - Protect Our Winters Main Website: https://protectourwinters.org/
    - Athlete Alliance: https://protectourwinters.org/pow-alliance/athlete-alliance/
    - Join Team POW: https://protectourwinters.org/join-pow/
    
    ⛷️ Let's protect the places we love! 🏂

    """, unsafe_allow_html=True)

with tabs[1]:
    Settings.llm = OpenAI(temperature=0.0, model="gpt-3.5-turbo-0125")

    urls = ["https://en.wikipedia.org/wiki/Protect_Our_Winters"]

    url = st.text_input("Enter a URL")
    if url:
        urls = [url]

    documents = SimpleWebPageReader(html_to_text=True).load_data(
        urls
    )

    index = SummaryIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query("Give me a summary of the page.")
    st.write(response.response)