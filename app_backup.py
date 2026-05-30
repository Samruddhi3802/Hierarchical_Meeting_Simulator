import streamlit as st
from main import simulate_meeting

st.set_page_config(page_title="AI Meeting Chat", layout="wide")

st.title("AI Business Meeting Simulator")
st.markdown("Hierarchical AI Agents having a live discussion")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "usage" not in st.session_state:
    st.session_state.usage = None

topic = st.text_input("Enter Business Idea:")

if st.button("Start Meeting"):
    if topic.strip() == "":
        st.warning("Please enter a topic!")
    else:
        st.session_state.chat_history = []  
        st.session_state.usage = None

        with st.spinner("Meeting in progress (Hierarchical Process)..."):
            chat, usage = simulate_meeting(topic)
            st.session_state.chat_history = chat
            st.session_state.usage = usage


if st.session_state.usage:
    with st.sidebar:
        st.header("Meeting Stats")
        st.metric("Total Tokens", st.session_state.usage.total_tokens)
        st.metric("Prompt Tokens", st.session_state.usage.prompt_tokens)
        st.metric("Completion Tokens", st.session_state.usage.completion_tokens)
        st.write(f"Successful Requests: {st.session_state.usage.successful_requests}")


for msg in st.session_state.chat_history:
    role = msg["role"]
    message = msg["message"]
    
    with st.chat_message("assistant"):
        st.markdown(f"{role} : {message}")