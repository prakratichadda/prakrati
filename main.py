import asyncio
import streamlit as st
from ollama import AsyncClient
from langchain_community.chat_models import ChatOllama
from retrieval_grader import retrieve_and_grade
from metadata_filter import metadata_filter


async def chat(content: str, message_placeholder):
    """
    Stream a chat from Llama using the AsyncClient.
    """
    llm = ChatOllama(model="llama3", format="json", temperature=0 , num_thread=16)
    filter = metadata_filter(llm, content)
    context = retrieve_and_grade(llm, content, filters=filter)
    message = {
        "role": "system",
        "content": f"You are system to provide answers on the query {content} on basis of the context {context}",
    }
    response = ""
    async for part in await AsyncClient().chat(
        model="llama3", messages=[message], stream=True
    ):
        response += part["message"]["content"]
        message_placeholder.markdown(response)
    return response


if "llama_model" not in st.session_state:
    st.session_state["llama_model"] = "llama3"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = asyncio.run(chat(prompt, message_placeholder))
        message_placeholder.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
