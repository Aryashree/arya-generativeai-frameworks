import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Streamlit App Title
st.title("Agile Guide Chatbot")

#  Ask user for OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Stop execution until API key is provided
if not api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# initialize OpenAI LLM (GPT-5 model)
llm = ChatOpenAI(model="gpt-5", api_key=api_key)

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an Agile coach. Only answer questions related to Agile methodology, "
            "Scrum, Kanban, product ownership, sprint planning, and related agile processes. "
            "Do not answer unrelated questions.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ]
)

#Combine prompt → model → parser into one runnable chain
chain = prompt_template | llm | StrOutputParser()

#Initialize Streamlit chat message history
history = StreamlitChatMessageHistory()

#Wrap chain with chat history tracking
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,  # returns the history instance
    input_messages_key="input",
    history_messages_key="chat_history",
)

#User Input
user_input = st.text_input("Ask your Agile question:")

#Run when user submits a question
if user_input:
    response = chain_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "session-abc123"}},
    )

    # Display the response
    st.write(response)
