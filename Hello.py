
import streamlit as st
import time
from dotenv import load_dotenv
import os
import openai

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages=[{"role":"user","content":prompt}]
    response=openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
  
def perform_classification(context):
    prompt=f"""
    Your task is to classify the intent based on the user utterance,
    For this Problem you can use the following,
    Your task is to classify the intent based on the user utterance,
    For this Problem you can use the following,
    Example1 - user utterance : Make a payment,
            intent : Make Payment
    Example 2 -user utterance : I lost my card yesterday at the suppermarket,
            intent : Lost My Card
    Example 2 - user utterance : I want to connect twith the support center 
            intent : Agent Transfer
            '''{context}'' 
            """
    response=get_completion(prompt)
    return response
  
def generate_summary(context):
    prompt=f"""
    Your task is to generate a short summary.Summarize with 15 words
    ```{context}```
    """
    response=get_completion(prompt)
    return(response)

st.set_page_config(page_title="Research Application" ,layout="wide", initial_sidebar_state="collapsed")

st.title('Research Application')

st.markdown("""
<style>
    /* Target the buttons inside the Streamlit app to expand to full width */
    .stButton>button {
        width: 100%;
    }
            
    [data-testid="collapsedControl"] {
        display: none
    }
    
</style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([3, 1, 3])


with col1:
    user_input = st.text_area("Enter Text Here", height=300)

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    summary_btn = st.button("Summary", key="summary_btn")
    classify_btn = st.button("Classify", key="classify_btn")


def summarize(text):
   return generate_summary(text)
  
    #return text

def classify(text):
    #return "Classified result"
    
    return perform_classification(text)

with col3:

    if summary_btn:
      with st.spinner('Summarizing Text...'):
        summary_result = summarize(user_input)
        st.text_area("Summarized Output", value=summary_result, height=300, key='result')

    elif classify_btn:
      with st.spinner('Classifying Text...'):
        classification_result = classify(user_input)
        st.text_area("Classified Output", value=classification_result, height=300, key='result')

    else:
      st.text_area("Result", height=300, key='result')