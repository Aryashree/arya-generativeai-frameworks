import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import  RunnableWithMessageHistory

#from travelapp_demo import prompt_template

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key to continue")
    st.stop()
llm = ChatOpenAI(model="gpt-5",api_key=api_key)


prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Agile coach. Only answer questions related to agile processes. "
                   "Do not answer unrelated questions."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ]
)
chain = prompt_template | llm
history_for_chain = StreamlitChatMessageHistory
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id:history_for_chain,
    input_message_keys="input",
    history_messages_key="chat_history")

st.title("Agile Guide")

input = st.text_input("Enter the question:")



if input:
    response = chain_with_history.invoke({"input":input},{"configurable":{"session_id":"session-abc123"}})
    st.write(response.content)
