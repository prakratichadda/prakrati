import streamlit as st
st.title("Simple Chatbox")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to display chat history
def display_chat(messages):
    for message in messages:
        st.write(f"{message['role']}: {message['content']}")

# Input for the user
user_input = st.text_input("You: ", "")

# Display chat history
display_chat(st.session_state['messages'])

# Function to handle user input
if st.button("Send"):
    if user_input:
        # Append user's message to the chat history
        st.session_state['messages'].append({"role": "User", "content": user_input})
        
        # Placeholder for bot response - replace with actual bot logic
        bot_response = f"Echo: {user_input}"
        
        # Append bot's response to the chat history
        st.session_state['messages'].append({"role": "Bot", "content": bot_response})
        
        # Clear the input box after sending
        st.experimental_rerun()
