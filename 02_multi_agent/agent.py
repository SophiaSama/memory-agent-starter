import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

load_dotenv(override=True)

# --- Agent Definitions for our Specialist Team (Refactored for Sequential Workflow) ---

# agent 1: foodie agent, output a destination and save into state, passas place holder to agent 2
foodie_agent = LlmAgent(
    name="foodie_agent",
    model="gemini-2.5-flash",
    tools=[google_search],
    instruction="""You are an expert food critic. Your goal is to find the best restaurant based on a user's request.

    When you recommend a place, you must output *only* the name of the establishment and nothing else.
    For example, if the best sushi is at 'Sushi Masashi', you should output only: Sushi Masashi.
    """,
    output_key="destination"  # ADK will save the agent's final response to state['destination']
)

# agent 2: transportation agent
transportation_agent = LlmAgent(
    name="transportation_agent",
    model="gemini-2.5-flash",
    tools=[google_search],
    instruction="""You are a navigation assistant. Given a destination, provide clear directions.
    The user wants to go to: {destination}.

    Analyze the user's full original query to find their starting point.
    Then, provide clear directions from that starting point to {destination}.
    """,
)

# agent 3: root_agent
root_agent = SequentialAgent(
    name="find_and_navigate_agent",
    sub_agents=[foodie_agent, transportation_agent],
    description="A workflow that first finds a location and then provides directions to it."
)