This updated preferences.py script enhances the user experience for the Nutrition Chatbot by utilizing Streamlit and Vertex AI. The application captures user preferences such as name, age, gender, medical conditions, food allergies, and specific products of interest.

## Key Features:

### User Input Collection:
Captures user's name, age (via slider), assigned gender at birth, relevant medical conditions (with a multiselect option), and any food allergies.
Allows users to specify a product they want to learn more about.

### Dynamic Context for Chatbot:
Initializes a chat session with Vertex AI's ChatModel and provides context based on user input to generate relevant responses about food products.

### Seamless Navigation:
Integrates a page-switching feature that directs users to the chatbot interface after entering their preferences.

### Example Queries:
Includes predefined input-output pairs to guide the chatbot in responding to various questions related to nutrition and health, customized to the user's profile.
This script aims to provide a personalized chat experience, ensuring users receive tailored nutritional advice based on their specific needs and conditions.
