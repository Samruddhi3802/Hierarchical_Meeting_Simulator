# Hierarchical Meeting Simulator — AI Board Room in Action

An intelligent multi-agent system built with **CrewAI** and **Groq LLaMA** that simulates a realistic corporate board meeting. A CEO agent manages a team of specialized executives (CTO, Marketing Head, Investor) in a **hierarchical process**, producing structured meeting discussions and decisions on any topic.

---

## Live Demo

**Live Link:** _Coming soon — will be updated after deployment_

---

## What It Does

Enter any business topic and watch a full executive board meeting unfold — powered by AI agents playing distinct corporate roles:

| Agent | Role |
|---|---|
|  CEO (Manager) | Leads the meeting, delegates tasks, synthesizes final decisions |
|  CTO | Analyzes technical feasibility & system design |
|  Marketing Head | Crafts marketing strategy & growth plans |
|  Investor | Evaluates ROI, financial risk & investment potential |

The system uses CrewAI's **hierarchical process** — the CEO agent actively delegates to worker agents and synthesizes their responses into a cohesive meeting transcript.

---

## Project Structure

```
Hierarchical_Meeting/
├── app.py               # FastAPI backend server
├── main.py              # Entry point — calls the crew
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── .env.example         # Template for environment variables
├── agents/
│   ├── manager_agent.py # CEO agent definition
│   └── worker_agents.py # CTO, Marketing Head, Investor agents
├── config/
│   └── llm_config.py    # LLM configuration (Groq models)
├── crew/
│   └── meeting_crew.py  # Crew orchestration with hierarchical process
├── tasks/               # Task definitions
├── utils/               # Utility functions
└── static/              # Frontend HTML/CSS/JS files
```

---

## Tech Stack

- **Backend:** FastAPI + Uvicorn
- **AI Framework:** [CrewAI](https://crewai.com/) (Hierarchical Process)
- **LLM Provider:** [Groq](https://groq.com/) (LLaMA 3.3-70B & LLaMA 3.1-8B)
- **Frontend:** Vanilla HTML/CSS/JS (served as static files)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Hierarchical_Meeting
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
```

Open `.env` and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
```

>  Get your free Groq API key at [console.groq.com](https://console.groq.com/)

### 5. Run the Application

```bash
python app.py
```

The server will start at **http://localhost:8001**

Open your browser and navigate to `http://localhost:8001` to use the app.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/simulate` | Simulate a board meeting on a topic |

**Request Body:**
```json
{
  "topic": "Should we expand our SaaS product to enterprise clients?"
}
```

**Response:**
```json
{
  "chat_history": [
    { "role": "CEO", "content": "Let's discuss expanding to enterprise..." },
    { "role": "CTO", "content": "From a technical standpoint..." },
    ...
  ],
  "stats": {
    "total_tokens": 4200,
    "prompt_tokens": 2800,
    "completion_tokens": 1400,
    "successful_requests": 4
  }
}
```

---

## How Hierarchical Process Works

Unlike a sequential crew, the **hierarchical process** gives the CEO full control:

1. CEO receives the topic and decides which executive to consult first
2. CEO delegates specific questions to CTO, Marketing Head, or Investor
3. Worker agents respond concisely from their domain expertise
4. CEO synthesizes all inputs into a final meeting conclusion

This mirrors real corporate decision-making dynamics.

---

## Requirements

- Python 3.9+
- Groq API Key (free tier available)

---

