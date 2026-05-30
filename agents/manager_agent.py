from crewai import Agent
from config.llm_config import get_llm

def get_manager_agent():
    return Agent(
        role="CEO",
        goal="Directly manage the board and synthesize final decisions",
        backstory="""You are a decisive CEO. 
        IMPORTANT: Your team has NO external tools. 
        Do NOT ask them to search the web. 
        Keep your delegations extremely brief and ask for concise responses only.
        Complete the meeting in as few steps as possible.""",
        llm=get_llm(),
        allow_delegation=True,
        max_iter=2,  
        verbose=True
    )