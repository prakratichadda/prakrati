import streamlit as st

# Function to generate AI response
def get_ai_response(user_input):
    # Here you would integrate your AI model to generate a response based on user input
    # For demonstration purposes, let's just echo the user's input as the AI response
    return user_input

# Streamlit UI
def main():
    st.title("Chat with AI")

    user_input = st.text_input("User input:")
    if st.button("Send"):
        ai_response = get_ai_response(user_input)
        st.text("AI response: {}".format(ai_response))

if __name__ == "__main__":
    main()
