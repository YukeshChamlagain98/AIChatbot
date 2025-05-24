import streamlit as st
import time # To simulate thinking

# --- Page Configuration ---
st.set_page_config(page_title="Health Chatbot", page_icon="🩺", layout="centered")

# --- Chatbot Logic ---
def get_bot_response(user_input):
    """
    Generates a response from the chatbot based on user input.
    For a prototype, this uses simple keyword matching.
    In a real AI, this would involve NLP/LLM.
    """
    user_input_lower = user_input.lower()
    response = ""

    # Greetings
    if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        response = "Hello there! How can I assist you with your health questions today? Remember, I'm an AI assistant and not a substitute for professional medical advice. 😊"
    # Basic Symptom Queries
    elif "headache" in user_input_lower:
        response = "I understand you're experiencing a headache. Common causes can include stress, dehydration, or lack of sleep. For persistent or severe headaches, please consult a doctor."
    elif "fever" in user_input_lower:
        response = "A fever can be a sign of an infection. It's important to monitor your temperature and stay hydrated. If the fever is high or persists, please see a healthcare professional."
    elif "cough" in user_input_lower:
        response = "A cough can be due to various reasons like a cold, flu, or allergies. Rest and fluids can help. If your cough is severe, prolonged, or accompanied by other symptoms like shortness of breath, please consult a doctor."
    elif "symptom" in user_input_lower or "feel" in user_input_lower:
        response = "Please describe your symptoms in more detail. However, remember that for any medical diagnosis or treatment, it's essential to consult a qualified healthcare provider."
    # Diet/Nutrition
    elif "diet" in user_input_lower or "nutrition" in user_input_lower or "healthy food" in user_input_lower:
        response = "A balanced diet rich in fruits, vegetables, lean proteins, and whole grains is key for good health. Are you looking for information on a specific aspect of diet or nutrition?"
    # Exercise
    elif "exercise" in user_input_lower or "workout" in user_input_lower:
        response = "Regular physical activity is beneficial for both physical and mental health. The general recommendation is at least 150 minutes of moderate-intensity aerobic exercise per week. What kind of exercise are you interested in?"
    # Thank you
    elif "thank you" in user_input_lower or "thanks" in user_input_lower:
        response = "You're welcome! Is there anything else I can help you with? Please remember to consult a doctor for serious medical concerns."
    # Default/Fallback
    else:
        response = "I'm still learning and may not have information on that specific topic. I can provide general health information. For specific medical advice, diagnosis, or treatment, please consult a qualified healthcare professional."

    # Always add a disclaimer
    if "consult a doctor" not in response.lower() and "professional medical advice" not in response.lower() and "healthcare provider" not in response.lower():
        response += " Remember, I am an AI assistant and this information is not a substitute for professional medical advice. Always consult with a doctor for medical concerns."
        
    return response

# --- Streamlit UI ---
st.title("🩺 Healthcare AI Chatbot Prototype")

st.markdown("""
**Disclaimer:** Ring triple zero **000** if it's an emergency. This chatbot is a prototype for informational purposes only.
It does **not** provide medical advice, diagnosis, or treatment.
Always consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health. 
""")
st.markdown("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your AI Health Assistant. How can I help you today? Ask me about general health topics, symptoms, or healthy habits. (e.g., 'What are symptoms of a cold?', 'Tell me about healthy eating.')"}
    ]

# Button to clear conversation
if st.sidebar.button("🗑️ Clear Conversation"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Conversation cleared. How can I help you now?"}
    ]
    st.rerun()

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me about your health... (e.g., 'symptoms of flu')"):
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."): # Simulate AI thinking
            time.sleep(0.5) # Simulate a small delay
            bot_response = get_bot_response(prompt)
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# footer note
st.markdown("---")
st.caption("ℹ️ This is a prototype. For actual medical advice, please consult a doctor.")