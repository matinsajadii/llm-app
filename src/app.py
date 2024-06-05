import streamlit as st
import json
from streamlit_lottie import st_lottie
from utils import call_llama

st.set_page_config(
    page_title='Ollama Chatbot',
    page_icon="🤖",
    layout='centered',
    initial_sidebar_state='collapsed'
    )


@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

col1, col2 = st.columns(2)
with col1:
    st.header(":llama: LLAma3 Chatbot")
    st.markdown("")
    st.write(""" 
    Meet Llama3,
    that transforms ideas into captivating
    content effortlessly.\n
    """)
    
with col2:
    
    lottie11 = load_lottiefile("/mnt/c/Users/Green.PC/Documents/ASAMA/github/matin/llm-app/src/.gitignore/Animation - 1717587429951.json")
    st_lottie(lottie11,key='locMainImage', height=200, width=200)

st.markdown("<hr>", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
   
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    print(st.session_state.messages)

    with st.spinner("Generating response..."):
        response = call_llama(model="llama3", prompt=st.session_state.messages[-1]['content'])
        msg = response['response']
        
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)