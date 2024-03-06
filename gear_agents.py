from crewai import Agent
from langchain_community.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

class GearAgents():

  def sustainability_expert(self):
    return Agent(
        role='Sustainability Expert',
        goal='Assess and recommend the most sustainable winter sports gear',
        backstory=
        'An expert in sustainability practices within the sporting goods industry',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def gear_selection_agent(self):
    return Agent(
        role='Gear Selection Specialist',
        goal='Select the best winter sports gear based on performance, sustainability, and budget',
        backstory="""A specialist in winter sports gear, focusing on finding the best 
        balance between performance, cost, and environmental impact""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def eco_conscious_shopper(self):
    return Agent(
        role='Eco-Conscious Shopper Advisor',
        goal="""Provide personalized recommendations for winter sports enthusiasts 
        looking to make sustainable choices""",
        backstory="""An advisor dedicated to helping consumers find high-quality, 
        sustainable winter sports equipment that meets their specific needs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)
