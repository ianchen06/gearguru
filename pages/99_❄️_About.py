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

    - **Membership and Donations**: Joining POW as a member or making a donation is one of the most straightforward ways to support their cause. Financial contributions help fund their advocacy work, educational programs, and climate initiatives.
    - **Volunteering**: POW often seeks volunteers to help with events, campaigns, and other organizational needs. Volunteering is a great way to get involved directly with their efforts and contribute your time and skills.
    - **Participate in Events**: Attend POW events or initiatives in your area. These can range from educational workshops, climate marches, to community clean-up days. Participating helps raise awareness and supports the organization's goals.
    - **Advocacy and Education**: Become a climate advocate by educating yourself and others about climate change and its impact on winter sports and outdoor activities. POW provides resources and tools to help you speak effectively about climate issues, contact legislators, and spread the word within your community.
    - **Corporate Partnerships and Sponsorships**: If you represent a business, consider partnering with POW or sponsoring their initiatives. Corporate partnerships can provide crucial support for POW's projects and help spread their message to a wider audience.
    - **Social Media and Awareness**: Use your social media platforms to raise awareness about POW and climate change. Sharing information about their campaigns, success stories, and how individuals can contribute plays a vital role in growing their movement.
    - **Lifestyle Changes**: Commit to making more sustainable choices in your daily life and outdoor activities. Reducing your carbon footprint, supporting eco-friendly brands, and advocating for environmental policies align with POW's mission.
    
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
    st.header("GPT Researcher")
    st.write("Paste a link to a Protect Our Winters campaign page to get a summary.")

    st.markdown("""
- https://protectourwinters.org/campaign/protect-the-ruby-mountains/
    """)
    Settings.llm = OpenAI(temperature=0.0, model="gpt-3.5-turbo-0125")

    urls = ["https://en.wikipedia.org/wiki/Protect_Our_Winters"]

    url = st.text_input("Enter a POW campaign URL:")
    if url:
        urls = [url]

    documents = SimpleWebPageReader(html_to_text=True).load_data(
        urls
    )

    index = SummaryIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query("Give me a detailed summary of the page.")
    st.write(response.response)