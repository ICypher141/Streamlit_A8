# Name: Kaushik Salunke 
# PRN : 22210126
# Roll no: 391050
# Batch : A-2


import streamlit as st
import random

st.set_page_config(page_title="Fitness Chatbot", page_icon="💪")

st.title("💪 Arnold - Your Fitness Buddy Chatbot")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Hydration tracker
if "water_glasses" not in st.session_state:
    st.session_state.water_glasses = 0

# Sample responses
workouts = {
    "weight loss": ["Try 30 mins of HIIT!", "Include cardio like running or cycling."],
    "muscle gain": ["Do strength training 4x a week.", "Focus on compound lifts like squats and deadlifts."],
    "flexibility": ["Include yoga or pilates in your routine.", "Try 15 mins of morning stretching."],
}

tips = [
    "Consistency beats intensity.",
    "Sleep 7–8 hours to recover better.",
    "Never skip warm-ups and cool-downs.",
    "Hydration is key to performance.",
]

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "It never gets easier, you just get stronger.",
    "Your only limit is you.",
    "Small progress is still progress.",
]

# Response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "workout" in user_input or "exercise" in user_input:
        return "What is your goal? (weight loss / muscle gain / flexibility)"
    elif "weight loss" in user_input:
        return random.choice(workouts["weight loss"])
    elif "muscle gain" in user_input:
        return random.choice(workouts["muscle gain"])
    elif "flexibility" in user_input:
        return random.choice(workouts["flexibility"])
    elif "tip" in user_input:
        return random.choice(tips)
    elif "quote" in user_input or "motivate" in user_input:
        return random.choice(quotes)
    elif "water" in user_input or "drink" in user_input:
        st.session_state.water_glasses += 1
        return f"Great! You've logged {st.session_state.water_glasses} glass(es) of water today."
    elif "hello" in user_input or "hi" in user_input:
        return "Hey! I’m your fitness buddy. Ask me anything about fitness, workouts, or tips!"
    else:
        return "I'm not sure how to respond to that. Ask me for workout tips, motivation, or hydration tracking!"

# User input
user_input = st.chat_input("Ask me anything about fitness...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    response = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", response))

# Chat display
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")

# To run this chatbot the command line is : streamlit run Assignment_9_391050.py