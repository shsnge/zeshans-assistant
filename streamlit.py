from google import genai
import streamlit as st

client = genai.Client(api_key='AIzaSyCM4vIdZylsML_EvYub0ky-ynPuJtYXvUE')


st.title("Talk to Zeeshan's AI Agent")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-2.0-flash', contents=user_input
        )

    st.write(response.text)
