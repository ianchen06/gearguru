import os

import streamlit as st
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from dotenv import load_dotenv
from openai import OpenAI as OfficialOpenAI

load_dotenv()

tabs = st.tabs(["About", "Campaigns"])

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
    st.header("🚣 GPT Researcher Crew 🚣🏼‍♂️")
    st.markdown("Paste a link to a Protect Our Winters campaign page to get a summary.")
    st.markdown("Our crew of AI experts will perform a detailed analysis of the page and provide a summary.")

    with st.expander("Meet our crew of experts! 🤖🤖🤖"):
        colzz = st.columns(3)
        with colzz[0]:
            st.image("images/ai1.webp", use_column_width=True)
            st.subheader("Politician")
            st.write("I'm a politician who's passionate about the balance of business and climate change.")
        with colzz[1]:
            st.image("images/ai2.webp", use_column_width=True)
            st.subheader("Climate Activist")
            st.write("I'm a climate activist who's been fighting for the environment for over 20 years.")
        with colzz[2]:
            st.image("images/ai3.webp", use_column_width=True)
            st.subheader("Business Leader")
            st.write("I'm a business leader who's been working to make my company more profitable and sustainable.")

    st.markdown("""
- https://protectourwinters.org/campaign/protect-the-ruby-mountains/
    """)
    Settings.llm = OpenAI(temperature=0.0, model="gpt-3.5-turbo-0125")

    urls = ["https://en.wikipedia.org/wiki/Protect_Our_Winters"]
    urls = []

    url = st.text_input("Enter a POW campaign URL:")
    if url:
        urls = [url]

    if urls:
        documents = SimpleWebPageReader(html_to_text=True).load_data(
            urls
        )
        index = SummaryIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        with st.spinner("Generating Summary..."):
            response = query_engine.query("""Give me a detailed summary of the page.""")
            st.title("Summary")
            highlevel_summary = response.response
            st.write(highlevel_summary)
        with st.spinner("Generating Keywords..."):
            response = query_engine.query("""Give me top five most important keywords from the page.""")
            st.title("Keywords")
            st.write(response.response)
        with st.spinner("Analysis..."):
            response = query_engine.query("""
                Give me a comprehensive analysis of the page from the following three perspectives:
                - Politician who's passionate about the balance of business and climate change.
                - Climate activist who's been fighting for the environment for over 20 years.
                - Business leader who's been working to make my company more profitable and sustainable.
                                        
                Please output in bullet point format.
            """)
            st.title("Crew Analysis")
            st.write(response.response)
        with st.spinner("Journalist Summary..."):
            client = OfficialOpenAI(
                # This is the default and can be omitted
                api_key=os.getenv("OPENAI_API_KEY"),
            )

            prompt = f"""
Read the following materials, give me a unbiased journalist summary:

High-level Summary:
{highlevel_summary}                    

Opinions from the three perspectives:                
{response.response}
"""

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo-0125",
            )
            st.title("Journalist Summary")
            st.write(chat_completion.choices[0].message.content
)