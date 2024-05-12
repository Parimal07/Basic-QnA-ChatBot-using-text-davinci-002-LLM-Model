#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import requests
import json


# ### Global variables to store generated question and answer

# In[2]:


generated_question = ""
generated_answer = ""


# ### Function to submit answer

# In[3]:


def submit_answer():
    global generated_question, generated_answer
    user_answer_text = user_answer.get()
    
    if generated_answer is not None and user_answer_text.lower() == generated_answer.lower():
        feedback = "Correct!"
        # If the user's answer matches the generated answer, provide feedback directly
        result_label.config(text=feedback) 
    else:
        # If the user's answer is wrong, check with the LLM model again
        api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTA0N2IxNTctNmRlYy00NWM4LWEyNmItMzFmMDEwNTMyNzM5IiwidHlwZSI6ImFwaV90b2tlbiJ9.5BcSWLEOHTpMi-c5N8AtR_Q09ZMd_b9_oNmEZkIkao8"
        headers = {"Authorization": f"Bearer {api_key}"}
        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "text": f"Is '{user_answer_text}' the correct answer for '{generated_question}'?, If partially yes then how much percent and if no provide correct answer with explaination of one line only",
            "providers": ["openai"],
            "models": ["text-davinci-002"],
            "temperature": 0.9,
            "max_tokens": 50,
            "n": 1,
            "previous_history": [] 
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  
            result = json.loads(response.text)
            generated_text = result.get("openai", {}).get("generated_text", "").strip()

            # Extract the assistant's message
            assistant_message = result.get("openai", {}).get("message", [])
            if assistant_message:
                assistant_response = assistant_message[-1].get("message", "")
                result_label.config(text=assistant_response)
            else:
                result_label.config(text="Failed to get response.")

        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            result_label.config(text="Failed to check answer.")


# ### Function to generate a question based on the selected topic using the LLM model

# In[4]:


def generate_question(*args):
    global generated_question, generated_answer
    topic = selected_topic.get()
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTA0N2IxNTctNmRlYy00NWM4LWEyNmItMzFmMDEwNTMyNzM5IiwidHlwZSI6ImFwaV90b2tlbiJ9.5BcSWLEOHTpMi-c5N8AtR_Q09ZMd_b9_oNmEZkIkao8"
    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "text": f"Generate a very basic question with one word answer only related to {topic}.",
        "providers": ["openai"],
        "models": ["text-davinci-002"],
        "temperature": 0.9,
        "max_tokens": 50,
        "n": 1,
        "previous_history": [] 
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  
        result = json.loads(response.text)
        generated_text = result.get("openai", {}).get("generated_text", "").strip()

        # Extract the question and answer
        question_parts = generated_text.split("?")
        if len(question_parts) > 1:
            generated_question = question_parts[0].strip() + "?"  
            generated_answer = question_parts[-1].strip().split(":")[-1].strip(".!").strip()
        else:
            generated_question = "Failed to generate question."

        # Clear other fields
        question_text.config(state="normal")
        question_text.delete("1.0", tk.END)
        question_text.insert(tk.END, generated_question)
        question_text.config(state="disabled")
        user_answer.delete(0, tk.END)
        result_label.config(text="")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        question_text.config(state="normal")
        question_text.delete("1.0", tk.END)
        question_text.insert(tk.END, "Failed to generate question.")
        question_text.config(state="disabled")


# ### Web UI

# In[5]:


window = tk.Tk()
window.title("Generative AI Q&A")
window.configure(bg="#f0f0f0")
window.geometry("400x350")

# Label and dropdown for topic selection
topic_label = tk.Label(window, text="Select Topic:", bg="#f0f0f0", font=("Arial", 12))
topic_label.pack(pady=(10,5))

topics = ["Geography", "Health", "Sports"]
selected_topic = tk.StringVar()
selected_topic.set(topics[0])  # Set default value
topic_dropdown = ttk.Combobox(window, textvariable=selected_topic, values=topics, state="readonly")
topic_dropdown.pack()
topic_dropdown.bind("<<ComboboxSelected>>", generate_question)

# Label and text box for question display
question_label = tk.Label(window, text="Generated Question:", bg="#f0f0f0", font=("Arial", 12))
question_label.pack(pady=(10,5))

question_text = tk.Text(window, height=5, width=50)
question_text.config(state="disabled", bg="white", bd=2, relief="solid")
question_text.pack()

# Label and entry field for user answer
answer_label = tk.Label(window, text="Your Answer:", bg="#f0f0f0", font=("Arial", 12))
answer_label.pack(pady=(10,5))

user_answer = tk.Entry(window, width=40, bd=2, relief="solid")
user_answer.pack()

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_answer, bg="#4caf50", fg="black", font=("Arial", 12), bd=0, padx=10, pady=5)
submit_button.pack(pady=(10,0))

# Label to display the result
result_label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
result_label.pack(pady=(10,5))

window.mainloop()

