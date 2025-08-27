import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000/chat"

# Page config
st.set_page_config(
    page_title="HR Resource Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
            padding: 20px;
            border-radius: 12px;
            background: #f8f9fa;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .user-msg {
            background: #d1e7dd;
            color: #0f5132;
            padding: 10px 15px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: right;
        }
        .bot-msg {
            background: #e2e3e5;
            color: #41464b;
            padding: 10px 15px;
            border-radius: 12px;
            margin: 8px 0;
            text-align: left;
        }
        .chat-header {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Title
st.markdown('<div class="chat-header">💼 HR Resource Query Chatbot</div>', unsafe_allow_html=True)

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Input box
user_input = st.text_input("💬 Type your question here:")

col1, col2 = st.columns([1, 5])
with col1:
    send_btn = st.button("🚀 Send")
with col2:
    clear_btn = st.button("🗑️ Clear Chat")

# Handle send
if send_btn and user_input:
    st.session_state["messages"].append(("user", user_input))

    try:
        response = requests.get(API_URL, params={"message": user_input})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "⚠️ No reply")
        else:
            bot_reply = f"❌ Error: {response.text}"
    except Exception as e:
        bot_reply = f"⚠️ Backend error: {str(e)}"

    st.session_state["messages"].append(("bot", bot_reply))

# Handle clear
if clear_btn:
    st.session_state["messages"] = []
    st.rerun()

# Display chat history
for sender, msg in st.session_state["messages"]:
    if sender == "user":
        st.markdown(
            f"""
            <div style='background-color:#DCF8C6;padding:10px;border-radius:10px;
                        margin:5px 0;text-align:right;max-width:70%;margin-left:auto;'>
                🧑 <b>You:</b> {msg}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div style='background-color:#F1F0F0;padding:10px;border-radius:10px;
                        margin:5px 0;text-align:left;max-width:70%;margin-right:auto;'>
                🤖 <b>Bot:</b> {msg}
            </div>
            """, unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)
