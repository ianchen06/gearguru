from crewai import Task
from textwrap import dedent
from datetime import date


class GearTasks():

  def evaluate_sustainability_task(self, agent, product_list):
    return Task(description=dedent(f"""
        Analyze and evaluate the sustainability of each product in the provided list based 
        on criteria such as materials used, manufacturing process, carbon footprint, and 
        company sustainability practices. This task involves researching and compiling 
        data on the environmental impact of these products, assessing their longevity and 
        recyclability, and understanding the ethical practices of the manufacturers.
        
        Your final answer must be a detailed report on each product, highlighting its 
        sustainability features, areas of concern, and an overall sustainability score. 
        Provide recommendations for the most sustainable choices within different 
        categories of winter sports gear (e.g., jackets, snowboards, boots).

        Product List: {product_list}
        """),
                agent=agent)

  def gear_recommendation_task(self, agent, sport_type, budget):
    return Task(description=dedent(f"""
        Based on the sport type and budget provided, recommend the best winter sports gear 
        options that align with sustainable and ethical manufacturing practices. Focus on 
        products that offer the best balance between performance, sustainability, and price.
        
        Consider factors such as material sustainability, product durability, and the 
        environmental impact of the manufacturing process. Research and suggest gear across 
        various categories relevant to the specified sport, including but not limited to 
        apparel, equipment, and accessories.
        
        Your final answer must include a curated list of gear recommendations, with each 
        item accompanied by a brief justification focusing on its sustainability credentials 
        and how it fits within the budget and sport requirements.

        Sport Type: {sport_type}
        Budget: {budget}
        """),
                agent=agent)

  def personalized_gear_plan_task(self, agent, sport_type, budget, personal_preferences):
    return Task(description=dedent(f"""
        Create a personalized winter sports gear plan that not only fits the specified 
        budget and sport type but also aligns with the personal preferences and sustainability 
        values of the individual. This plan should include a comprehensive gear list, covering 
        all necessary equipment, apparel, and accessories, prioritizing products that are 
        environmentally friendly and ethically produced.
        
        Research and select products that offer longevity, reduce environmental impact, and 
        come from brands committed to sustainable practices. Explain the rationale behind each 
        choice, detailing the sustainability features, how the product meets the individual's 
        preferences, and its value within the overall budget.
        
        Your final answer must be a detailed and personalized gear plan, including product 
        recommendations, sustainability highlights, and a budget breakdown to ensure the 
        individual is fully equipped for their winter sports activities in the most sustainable 
        manner possible.

        Sport Type: {sport_type}
        Budget: {budget}
        Personal Preferences: {personal_preferences}
        """),
                agent=agent)
