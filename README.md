# Agile Coach Chatbot — Streamlit + LangChain + GPT-5

An interactive AI chatbot built using **Streamlit**, **LangChain**, and **OpenAI GPT-5** that acts as an **Agile Coach**.  
It can answer questions about **Agile methodology**, **Scrum**, **Kanban**, **sprint planning**, and more — while remembering the context of your conversation.

---

## Features

✅ Built with **Streamlit** for an easy-to-use web UI  
✅ Uses **LangChain** to manage prompts and message flow  
✅ Integrates **GPT-5** via `langchain-openai`  
✅ Includes **chat memory** — remembers what you’ve said during the session  
✅ Enforces **domain restrictions** (only answers Agile-related questions)  

---

## How It Works

1. The app asks for your **OpenAI API key**.
2. You type a question related to Agile.
3. LangChain builds a prompt using:
   - A **system message** (defines the role and rules),
   - Your **chat history** (previous exchanges),
   - Your **latest input**.
4. The **GPT-5 model** generates an answer.
5. The response and your message are saved in **Streamlit’s chat history**, so the model can use them next time.

---

## Project Structure

arya-generativeai-frameworks/
│
├── chatHistory-demo.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/arya-generativeai-frameworks.git
cd arya-generativeai-frameworks

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

📦 Requirements

Here’s what your requirements.txt should include:

streamlit>=1.36.0
langchain>=0.3.0
langchain-openai>=0.2.0
langchain-community>=0.3.0
openai>=1.44.0
tiktoken>=0.7.0

▶️ Run the App

Start the Streamlit app:

streamlit run chatHistory-demo.py

Usage

Enter your OpenAI API key when prompted.

Type a question such as:

What are the roles in Scrum?


The chatbot will respond and remember your conversation.

You can continue the discussion with follow-up questions like:

Who facilitates sprint retrospectives?


How It Works Internally
Component	Description
ChatPromptTemplate	Defines the structure of the chat messages (system + user + history).
StreamlitChatMessageHistory	Stores chat messages within Streamlit session.
RunnableWithMessageHistory	Wraps the chain to automatically manage conversation memory.
chain_with_history	The final pipeline that handles user input, context, and model responses.


🧰 Tech Stack

Python 3.10+

Streamlit – Front-end interface

LangChain – Prompt & chat orchestration

OpenAI GPT-5 – Core LLM

tiktoken – Token handling

🧑‍💻 Author

Arya
Built as part of the Generative AI Frameworks exploration using Streamlit + LangChain + OpenAI.


⚖️ License

This project is open-source and available under the MIT License.

🧭 Future Enhancements

🔄 Add persistent memory (save chat history even after reload)

💾 Store sessions in a database (SQLite, Firebase, etc.)

🗣️ Add voice input/output

🌐 Deploy on Streamlit Cloud or Hugging Face Spaces

