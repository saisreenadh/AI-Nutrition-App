import streamlit as st
import vertexai
from vertexai.preview.language_models import ChatModel

# Initialize Vertex AI with project details
project_id = "melodic-zoo-414700"
location = "us-central1"
vertexai.init(project=project_id, location=location)

# Set the page configuration
st.set_page_config(
    page_title="Nutrition Chatbot",
    page_icon="💬",
)

st.title("Chat with Products!")

# Retrieve session state variables set in the previous page
age = st.session_state.age
name = st.session_state.name
gender = st.session_state.gender
conditions = st.session_state.conditions
allergies = st.session_state.allergies
product = st.session_state.product

# Ensure the chat model is initialized in the session state
if "chat" not in st.session_state:
    chat_model = ChatModel.from_pretrained("chat-bison@002")
    # Initialize chat with context from the user's preferences
    context = f"""
    You are an AI expert in nutrition.
    The user is {name}, {age} years old, and assigned {gender} at birth.
    They have the following medical conditions: {', '.join(conditions) if conditions else 'None'}.
    They have the following food allergies: {allergies if allergies else 'None'}.
    They are asking about the product: {product}.
    """
    st.session_state.chat = chat_model.start_chat(context=context)

# Initialize messages if not in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user to type a question
if prompt := st.chat_input("Type your question"):
    # Display the user's question
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Get a response from the AI model
    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
