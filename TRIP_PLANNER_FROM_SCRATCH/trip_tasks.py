from crewai import Task
from textwrap import dedent

# Creating Tasks heat Sheet: 
# — Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve. 
# — Break down the outcome into actionable tasks, assigning each task to the appropriate agent. 
# — Ensure tasks are descriptive, providing clear instructions and expected deliverables. 

# Goal: 
# — Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

# Key Steps for Task Creation: 
# 1. Identify the Desired Outcome: Define what success looks like for your project. 
# - A detailed 7 day travel itenerary 

# 2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute. 
# - Itenerary Planning: develop a detailed plan for each day of the trip. 
# - City Selection: Analyze and pick the best city to visit
# - Locla Tour Guide: Find a local expert to provide insights and recommendations. 
  
# 3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise. 

# 4. Task Description Template: 
# - Use this template as a guide to define each task in your CrewAI application. 
# - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific 


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itenerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Tasks**: Develop a 7-day Travel Itenerary 
            **Description**: Expand this guide into a a full 7-day travel 
            itinerary with detailed per-day plans, including 
            weather forecasts, places to eat, packing suggestions, 
            and a budget breakdown.
            
            You MUST suggest actual places to visit, actual hotels 
            to stay and actual restaurants to go to.
            
            This itinerary should cover all aspects of the trip, 
            from arrival to departure, integrating the city guide
            information with practical travel logistics. 

            **Parameters**:
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler Interests: {interests}

            **Notes**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Tasks**: Identify yje Best City for the Trip
                **Description**:Analyze and select the best city for the trip based 
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses. 
                
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather 
                forecast and attractions.

                **Parameters**:
                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}

                **Notes**: {self.__tip_section()}

        """
            ),
            agent=agent,
        )

    def gather_city_info(self, agent, cities, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Tasks**: Gather in-depth city guide information
                **Description**: As a local expert on this city you must compile an 
                in-depth guide for someone traveling there and wanting 
                to have THE BEST trip ever!
                Gather information about  key attractions, local customs,
                special events, and daily activity recommendations.
                Find the best spots to go to, the kind of place only a
                local would know.
                This guide should provide a thorough overview of what 
                the city has to offer, including hidden gems, cultural
                hotspots, must-visit landmarks, weather forecasts, and
                high level costs.
                
                The final answer must be a comprehensive city guide, 
                rich in cultural insights and practical tips, 
                tailored to enhance the travel experience.

                **Parameters**:
                City Options: {cities}
                Travel Date: {travel_dates}
                Traveler Interests: {interests}

                **Notes**: {self.__tip_section()}

        """
            ),
            agent=agent,
        )
