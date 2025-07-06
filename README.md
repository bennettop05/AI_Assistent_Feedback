# 🤖 AI Agent with Feedback & Tool Tracing

An interactive Streamlit app where a GPT-powered assistant answers your questions, optionally uses tools (like image captioning), logs its internal reasoning process (trace), and lets users give feedback (thumbs up/down). Everything is stored and visualized — making the agent **transparent, explainable, and upgradable**.

---

## 🚀 Features

- 🔍 **Ask Questions** — and get GPT-powered answers.
- 🧠 **Agent Thought Tracing** — see what the agent thought before answering.
- 🧰 **Tool Usage** — uses an image captioning tool if the question involves images.
- 👍👎 **Feedback Logging** — log what users think about each answer.
- 📊 **Dashboard** — see feedback stats and recent traces in one view.

---

## 📦 Folder Structure

AI_Assistent_Feedback/
├── app.py # Main Streamlit app
├── .env.example # Sample .env file for API keys
├── trace_logger.py # Logs agent's internal thought/tool/output
├── tools/
│ └── tool_image_caption.py # Image captioning tool (BLIP)
├── prompts/
│ └── base_prompt.txt # Prompt template with {question}
├── trace_log.json # Saved agent traces (auto-generated)
└── requirements.txt # All required packages

yaml
Copy
Edit

---

## 🧠 Agent Flow

1. User types a question (and optionally uploads an image).
2. Agent decides:
   - If tool is needed → runs it (like BLIP for image captioning).
   - If not → directly sends prompt to GPT.
3. Agent saves:
   - Thought process
   - Tool used (if any)
   - Final answer
4. User can react with 👍 or 👎
5. All feedback & traces are stored and shown on dashboard.

---

## 🖼️ Screenshots

*Add your screenshots here once app is running locally or deployed.*

---

## ⚙️ Tech Stack

- [Streamlit](https://streamlit.io) — for the UI
- [OpenAI API](https://platform.openai.com/) — GPT-3.5-turbo model
- [Hugging Face BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) — Image Captioning tool
- Python, JSON, Matplotlib, dotenv, pandas

---

## 🔧 Setup Instructions

1. **Clone the repo**  
```bash
git clone https://github.com/bennettop05/AI_Assistent_Feedback.git
cd AI_Assistent_Feedback
Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .env file

env
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
Run the app

bash
Copy
Edit
streamlit run app.py
