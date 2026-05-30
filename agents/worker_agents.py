from crewai import Agent
from config.llm_config import get_fast_llm

def get_worker_agents():
    llm = get_fast_llm()

    strict_instruction = "IMPORTANT: You have NO TOOLS. Do NOT use brave_search or any functions. Use ONLY your internal knowledge. Be extremely concise."

    return [
        Agent(
            role="CTO",
            goal="Analyze technical feasibility",
            backstory=f"CTO focused on rapid system design. {strict_instruction}",
            llm=llm,
            max_iter=1,          
            allow_delegation=False,
            memory=False,
            verbose=True
        ),
        Agent(
            role="Marketing Head",
            goal="Create marketing strategy",
            backstory=f"Marketing expert focused on growth. {strict_instruction}",
            llm=llm,
            max_iter=1,
            allow_delegation=False,
            memory=False,
            verbose=True
        ),
        Agent(
            role="Investor",
            goal="Evaluate ROI and risk",
            backstory=f"Investor focused on financial auditing. {strict_instruction}",
            llm=llm,
            max_iter=1,
            allow_delegation=False,
            memory=False,
            verbose=True
        )
    ]