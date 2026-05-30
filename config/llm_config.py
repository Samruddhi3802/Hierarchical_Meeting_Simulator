import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=400 
    )

def get_fast_llm():
    return get_llm()