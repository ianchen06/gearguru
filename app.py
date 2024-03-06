from crewai import Crew
from textwrap import dedent
from gear_agents import GearAgents
from gear_tasks import GearTasks
import streamlit as st
import datetime
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_icon="🏂", layout="wide")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

class GearCrew:

  def __init__(self, sport, preferences, sustainability_standards):
    self.sport = sport
    self.preferences = preferences
    self.sustainability_standards = sustainability_standards

  def run(self, update_callback=None):
    agents = GearAgents()
    tasks = GearTasks()
    
    sustainability_expert_agent = agents.sustainability_expert()
    gear_selection_agent = agents.gear_selection_agent()
    eco_conscious_shopper_agent = agents.eco_conscious_shopper()
  
    if update_callback:
        update_callback("Initializing gear selection process...")
    sustainability_task = tasks.evaluate_sustainability(
      sustainability_expert_agent,
      self.sport,
      self.sustainability_standards
    )

    if update_callback:
        update_callback("Agent is gathering information on gear...")
    gear_selection_task = tasks.select_gear(
      gear_selection_agent,
      self.sport,
      self.preferences,
      self.sustainability_standards
    )

    shopping_guide_task = tasks.create_shopping_guide(
      eco_conscious_shopper_agent,
      self.sport,
      self.preferences,
      self.sustainability_standards
    )

    crew = Crew(
      agents=[
        sustainability_expert_agent, gear_selection_agent, eco_conscious_shopper_agent
      ],
      tasks=[sustainability_task, gear_selection_task, shopping_guide_task],
      verbose=True
    )

    result = crew.kickoff()

    if update_callback:
        update_callback("Finalizing gear recommendations...")

    return result

if __name__ == "__main__":
  icon("⛷️ GearAIgent")

  st.info("**Let AI agents help you choose sustainable winter sports gear...**")
  
  today = datetime.datetime.now().date()

  with st.sidebar:
    st.header("👇 Enter your gear preferences")
    with st.form("my_form"):
      sport = st.selectbox("Which winter sport?", ["Skiing", "Snowboarding", "Ice Skating"])
      preferences = st.text_input("What are your preferences?", placeholder="Eco-friendly, durable, budget-friendly")
      sustainability_standards = st.multiselect(
        "Sustainability standards of interest",
        ["Recycled materials", "Eco-certified", "Low carbon footprint"],
        default=["Recycled materials"]
      )

      submitted = st.form_submit_button("Submit")
    
    st.divider()
    
    st.sidebar.info("Seeking sustainable gear options", icon="🌍")
    
    st.sidebar.markdown(
        """
        Inspired by **crewAI** for creating adaptive solutions 🚀
        """,
        unsafe_allow_html=True
    )

def update_status(status_container, message):
    """Callback function for updates"""
    status_container.write(message)

if submitted:
    with st.status("**Analyzing preferences and sustainability standards...**", expanded=True) as status:
      gear_crew = GearCrew(sport, preferences, sustainability_standards)
      result = gear_crew.run(update_callback=lambda msg: update_status(status, msg))
      # Update the status container to indicate completion
      status.update(label="✅ Gear Recommendations Ready!", state="complete", expanded=False)
  
    st.subheader("Here are your sustainable gear recommendations:", anchor=False, divider="rainbow")
    st.markdown(result)
