from crewai import Task

def get_cto_task(topic, agent):
    return Task(
        description=f"Analyze the technical feasibility for the idea: {topic}. Suggest a basic tech stack and development time.",
        expected_output="A short technical summary.",
        agent=agent
    )

def get_marketing_task(topic, agent):
    return Task(
        description=f"Create a growth and marketing strategy for: {topic}. Identify the target audience.",
        expected_output="A short marketing plan.",
        agent=agent
    )

def get_investor_task(topic, agent):
    return Task(
        description=f"Evaluate the ROI and execution risks for: {topic}.",
        expected_output="A short risk and investment assessment.",
        agent=agent
    )

def get_ceo_task(topic, agent, context):
    return Task(
        description=f"Review the reports from your team and make a final Go/No-Go decision for: {topic}.",
        expected_output="A final executive summary with a clear decision.",
        agent=agent,
        context=context
    )