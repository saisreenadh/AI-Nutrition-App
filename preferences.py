import streamlit as st
import vertexai
from vertexai.preview.language_models import ChatModel
from streamlit_extras.switch_page_button import switch_page

project_id = "melodic-zoo-414700"
location = "us-central1"

# Initialize Vertex AI
vertexai.init(project=project_id, location=location)
chat_model = ChatModel.from_pretrained("chat-bison@002")

# Streamlit page configuration
st.set_page_config(
    page_title="Nutrition Chatbot",
    page_icon="⚙️",
)

st.title("User Preferences")

# Initialize session state variables
if "chat" not in st.session_state:
    st.session_state.chat = chat_model.start_chat()
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 1
if "gender" not in st.session_state:
    st.session_state.gender = "Male"
if "conditions" not in st.session_state:
    st.session_state.conditions = []
if "allergies" not in st.session_state:
    st.session_state.allergies = ""
if "product" not in st.session_state:
    st.session_state.product = ""

# User input fields
st.text_input("What's your name?", key="name")
st.slider('How old are you?', 1, 100, key="age")
st.radio(
    "What was your assigned gender at birth?",
    ["Male", "Female", "Prefer not to disclose"],
    index=0,
    horizontal=True,
    key="gender"
)
st.multiselect(
    'Are any of the following medical conditions applicable to you?',
    ['Acne', 'Anxiety', 'Asthma', 'Diabetes', 'Periodontal Disease', 'Obesity'],
    key="conditions"
)
st.text_input('Please list any food allergies you may have (e.g., milk, eggs, peanuts):', key="allergies")
st.text_input(
    "Which product would you like to learn more about?",
    key="product",
    placeholder="20 oz Mountain Dew Baja Blast Soda Bottle",
    disabled=True
)

# Button to start the chat
button = st.button("Start chat!", type="primary")
if button:
    # Constructing the context for the chat model
    llm_context = (
        f"You are designed to answer questions about food products. "
        f"The product you are being asked about is a 20 oz Mountain Dew® Baja Blast Soda Bottle. "
        f"The person you're addressing is named {st.session_state.name}. "
        f"{st.session_state.name} is {st.session_state.age} years old. "
        f"{st.session_state.name}'s assigned gender is {st.session_state.gender}. "
        f"{st.session_state.name} is affected by {st.session_state.conditions}. "
        f"{st.session_state.name} is allergic to {st.session_state.allergies}."
    )

    # Starting a new chat session with context
    st.session_state.chat = chat_model.start_chat(
        context=llm_context,
        examples=[
            {
                "input_text": "What are the ingredients?",
                "output_text": "A 20 oz Mountain Dew® Baja Blast Soda Bottle contains the following ingredients: Carbonated Water, High Fructose Corn Syrup, Natural and Artificial Flavor, Citric Acid, Sodium Benzoate (Preserves Freshness), Caffeine, Gum Arabic, Sodium Citrate, Calcium Disodium EDTA (To Protect Flavor), Sucrose Acetate Isobutyrate, Yellow 5, and Blue 1."
            },
            {
                "input_text": "Which of the product's ingredients are bad for my health?",
                "output_text": "Excessive amounts of High Fructose Corn Syrup (HFCS) has been linked to metabolic issues, including obesity and insulin resistance. Additionally, Yellow 5 (Tartrazine) may be linked with cancer and behavioral disorders in children, and the dye is currently banned in several European countries."
            },
            # Add more examples as needed...
        ]
    )
    switch_page('chatbot')
