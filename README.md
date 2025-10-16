# Autogen_Data_Analyzer# 🧠 AutoGen Code Analyst

[![Made with AutoGen](https://img.shields.io/badge/Made%20with-AutoGen-blue?logo=openai)](https://github.com/microsoft/autogen)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)]
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]

A modular, multi-agent system built using **AutoGen** for analyzing and visualizing tabular datasets (CSV/Excel). This project uses AutoGen’s RoundRobinGroupChat to coordinate agent turn-taking between the DataAnalyzerAgent and CodeExecutorAgent. This ensures structured, sequential collaboration where one agent reasons and the other executes—repeating the cycle until the task is complete.

---

## 🧩 System Architecture

```
      [📄 User Uploads CSV]
                │
                ▼
        ┌────────────────────┐
        │   Analyzer Agent   │ ◄──────────── GPT (system message configured)
        └────────────────────┘
                │  (Python logic + plan)
                ▼
        ┌────────────────────┐
        │  Code Executor     │ ◄──────────── Docker sandbox
        └────────────────────┘
                │ (Exec result or error)
                ▼
        ┌────────────────────┐
        │ Structured Output  │
        └────────────────────┘
                │
                ▼
        ┌────────────────────┐
        │ Streamlit Chat UI  │ ◄──────────── Chat frontend
        └────────────────────┘
```

---

## 📁 Project Structure

```
Autogen_Data_Analyzer/
├── agents/
│
├── prompts/
│   ├── data_analyzer_message.py       # System prompt template for DataAnalyzer
│   ├── Data_Analyzer_agent.py         # Creates and registers the analyzer agent
│   └── Code_Executer_agent.py         # Creates and registers the code executor agent
│
├── config/
│   ├── constants.py                   # Global config values
│   └── docker_util.py                 # Utilities to run and manage Docker containers
│
├── models/
│   └── openai_model_client.py         # Wrapper around OpenAI model client
│
├── teams/
│   └── analyzer_gpt.py                # Defines agent teams and interaction logic
│
├── main.py                            # Entry point to launch the agent workflow
├── LICENSE
├── README.md
└── .gitignore

```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Docker (for sandboxed code execution)
- OpenAI API Key (or Claude via Anthropic)

---

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/pkomals/Autogen_Data_Analyzer.git


# Set up virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

---

### 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
```

---

### ▶️ Run the Streamlit App

```bash
streamlit run streamlit/app.py
```

---

## 💬 How the Agents Collaborate
### Team
The multi-agent conversation is orchestrated using AutoGen’s RoundRobinGroupChat, which:

- Automatically alternates turns between DataAnalyzerAgent and CodeExecutorAgent

- Waits for execution feedback before the analyzer proceeds

- Ensures a clean, linear collaboration loop mimicking human teamwork

### 🔍 `Analyzer Agent` (GPT-4)

Follows a system prompt to:
- Outline a **plan** for solving user’s question
- Generate Python code (in a single block)
- Wait for result from executor
- If required libraries are missing:
  - Send a `bash` command to install via pip
- Retry execution
- Save plots as `.png` files in working directory
- End with a detailed explanation and `STOP`

### ⚙️ `Code Executor Agent`

- Receives Python or bash blocks
- Executes code in a sandbox
- Sends output/errors back to the analyzer

---

## 🧪 Sample Prompt (To Analyzer Agent)

```
What are the top 5 categories by total sales?

Plan: I will load the dataset, group by category, sum the sales column, sort descending, and plot a bar chart.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
top_categories = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 5))
top_categories.plot(kind="bar")
plt.title("Top 5 Categories by Sales")
plt.ylabel("Sales")
plt.savefig("top_categories.png")

print("Chart saved successfully.")
```
```

---

## 🌍 Features

- ✅ LLM-generated Python logic from CSV queries
- ✅ Auto-handles missing Python packages
- ✅ Secure code execution in Docker
- ✅ Visual insights with charts saved as PNG
- ✅ Streamlit chat interface for end-to-end flow

---

## 🔮 Future Enhancements

- [ ] SQL agent for DB uploads
- [ ] Support for `.parquet` and `.json` files
- [ ] Voice interaction with Whisper + TTS
- [ ] LangGraph visual agent trace


---

## 📚 References

- [AutoGen by Microsoft](https://github.com/microsoft/autogen)

---

## 🛡 License

MIT License

---

## 🙌 Contributing

Pull requests and agent contributions are welcome! Fork this repo and propose enhancements.

