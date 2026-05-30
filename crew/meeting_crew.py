from crewai import Crew, Process
from agents.manager_agent import get_manager_agent
from agents.worker_agents import get_worker_agents
from tasks.meeting_tasks import get_cto_task, get_marketing_task, get_investor_task, get_ceo_task

def run_hierarchical_meeting(topic):

    manager = get_manager_agent()
    workers = get_worker_agents()
    
    cto = next(w for w in workers if w.role == "CTO")
    marketing = next(w for w in workers if w.role == "Marketing Head")
    investor = next(w for w in workers if w.role == "Investor")

    t1 = get_cto_task(topic, cto)
    t2 = get_marketing_task(topic, marketing)
    t3 = get_investor_task(topic, investor)
    t4 = get_ceo_task(topic, manager, context=[t1, t2, t3])

    crew = Crew(
        agents=workers,
        tasks=[t1, t2, t3, t4],
        process=Process.hierarchical,
        manager_agent=manager,
        verbose=True,
        cache=True,
        max_rpm=3
    )

    result = crew.kickoff()

    print(f"\n{'='*30}")
    print(f"TOKEN USAGE: {result.token_usage}")
    print(f"{'='*30}\n")

    chat = []
    chat.append({"role": "CEO", "message": f"Team, let's analyze the idea: {topic}"})
    
    for task_output in result.tasks_output:
        agent_role = task_output.agent if hasattr(task_output, 'agent') else "System"
        role_display = agent_role.split('(')[0].strip() 
        chat.append({"role": role_display, "message": task_output.raw})

    return chat, result.token_usage