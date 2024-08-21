import streamlit as st
import google.generativeai as genai

st.markdown(
    """
    <style>
    .main {
        background-color:#1a0000;
    }

    #text_input_1 {
        border: 1px solid #cc0000;
        border-radius: 5px;
    }
    .st-emotion-cache-15hul6a{
        background-color: #808080;
        color:	#e60000;
    }

    .stTitle {
        text-align: center;
        color: #FFFFFF;
    }

    </style>
    """,
    unsafe_allow_html=True
)

#st.title("Welcome to VioraAI")
st.markdown("<h1 class='stTitle'>Welcome to VioraAI</h1>", unsafe_allow_html=True)

genai.configure(api_key="AIzaSyA31rNdKIYvcr187RLiU9g8wjXuDbVAnFY")

text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Generate"):
    response = chat.send_message(text)
    st.write(response.text)