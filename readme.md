#  Company Intelligence Agentic System

A multi-agent AI system built using **LangChain**, **Google Gemini 2.0 Flash**, **NewsAPI**, **Alpha Vantage**, and **Streamlit**.  
This application gathers real-time company information—including news & stock performance—and generates intelligent insights, risks, and summaries through LLM-based reasoning.

##  Core Features

###  Multi-Agent Architecture
```bash
| Agent | Responsibility |
|-------|----------------|
| **Data Collector Agent** | Fetches real-time company news & stock market data |
| **Analyst Agent (Gemini 2.5)** | Summarizes data, finds risks, trends, recommendations |
| **Orchestrator Agent** | Coordinates agents, maintains memory using LangChain |
```

###  Streamlit Web Interface
- Enter company name or ticker (e.g., *Google*, *AAPL*)
- Fetch **live news + stock data**
- Get **AI-generated insights**
- Visualize conversation history & decisions
- Simple intuitive interface for research / finance use-cases


##  System Architecture

```bash
            ┌───────────────────┐
            │     User Input    │
            └─────────┬─────────┘
                      │
                      ▼
            ┌───────────────────┐
            │   Orchestrator    │
            │ (Controller Agent)│
            └─────────┬─────────┘
    ┌─────────────────┼──────────────────┐
    ▼                 ▼                  ▼
┌──────────────┐ ┌────────────────┐ ┌────────────────────┐
│Data Collector│ │ Analyst Agent  │ │ Conversation Memory│
│  (Agent 1)   │ │    (Gemini)    │ │ (LangChain Buffer) │
└───────┬──────┘ └────────┬───────┘ └──────────┬─────────┘
        │                 │                    │
        ▼                 ▼                    ▼
 Real News (NewsAPI)  LLM Insights      Maintains Context
 Real Stocks (AV API) Summary & Risks   Across Sessions
```

## 📁 Project Structure

```bash
company_intel_agentic_system/
│── agents/
│   ├── data_collector.py
│   └── analyst.py
│
│── tools/
│   └── fetchers.py
│
│── orchestrator.py
│── streamlit_app.py
│── test_news.py
│── test_stock.py
│── test_orchestrator.py
│── requirements.txt
│── .env
│── README.md
```


##  Installation & Setup

###  Clone the repository

```bash
git clone https://github.com/your-username/company-intel-agentic-system.git
cd company-intel-agentic-system
```

###  Create virtual environment

```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```


##  API Keys (Environment Variables)

Create **.env** file in project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key
NEWSAPI_KEY=your_newsapi_key
ALPHA_VANTAGE_KEY=your_alpha_vantage_key
```

- Get Keys:

```bash
| Service | Link |
|--------|------|
| Gemini | https://aistudio.google.com/app/apikey |
| NewsAPI | https://newsapi.org/ |
| Alpha Vantage | https://www.alphavantage.co/ |
```

##  Testing Backend Agents

```bash
python test_news.py          # Fetch live news
python test_stock.py         # Get stock prices
python test_orchestrator.py  # Full agent pipeline
```

---

##  Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

Then visit:  
 **http://localhost:8501**


 ##  Output Preview

✔ Real-time company financial news  
✔ 7-Day stock trends (with price movement)  
✔ AI-generated summary + investment risk assessment  
✔ Persisting conversation memory  

---

##  Future Improvements

| Feature | Status |
|--------|--------|
| Sentiment scoring for news sources | ⏳ Planned |
| Stock charts with Altair/Matplotlib | ⏳ Planned |
| Dedicated Risk Scoring Agent | ⏳ Planned |
| LangGraph for complex pipelines | ⏳ Planned |
| Response caching to reduce API calls | ⏳ Planned |
| Auto-fetch company profile + logo | ⏳ Planned |

---
