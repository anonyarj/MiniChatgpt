import streamlit as st
import requests


#Set up Streamlit UI

st.set_page_config(page_title="Mini GPT", page_icon="🤖")
st.title("Hey there!!")

#Input field for the user

user_input = st.text_input("Ask me anything..")

#API fetching from Deepseek info

deepseek_API_KEY = "sk-d5661333e1fc4270b1762edff597bd14"
deepseek_AI_URL = "https://api.deepseek.com/v1/chat/completions"

def get_response(prompt):
    headers = {"Authorization": f"Bearer {deepseek_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",  # Use "deepseek-chat" or another available model
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(deepseek_AI_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

# Button to generate response
if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
        st.success(reply)
    else:
        st.warning("Please enter a message!")

