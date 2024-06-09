import streamlit as st

def main():
    st.title("Simple User Interface")

    # Add text
    st.header("Header")
    st.subheader("Subheader")
    st.write("This is a simple text.")

    # Add widgets
    st.checkbox("Checkbox")
    st.radio("Radio", ["Option 1", "Option 2", "Option 3"])
    st.selectbox("Selectbox", ["Option 1", "Option 2", "Option 3"])
    st.multiselect("Multiselect", ["Option 1", "Option 2", "Option 3"])
    st.slider("Slider", min_value=0, max_value=10, value=5)
    st.text_input("Text Input")
    st.number_input("Number Input", value=0)
    st.text_area("Text Area")
    st.date_input("Date Input")
    st.time_input("Time Input")
    st.file_uploader("File Uploader")

    # Add buttons
    if st.button("Button"):
        st.write("Button clicked!")

if __name__ == "__main__":
    main()
