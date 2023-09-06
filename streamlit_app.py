## This is the final One with no audio
import secrets
import os
import streamlit as st
from streamlit_chat import message

#replace with new one and use secret method

#os.environ['OPENAI_API_KEY']=

#####################################################
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate



def get_ai_response(human_input):
    template= """
    my prompt for chatgpt will go here
    
    {history}
    User: {human_input}
    Amy:
    """
    prompt = PromptTemplate(
        input_variables=["history","human_input"],
        template=template,
    )

    chain = LLMChain(llm=OpenAI(temperature=1), prompt=prompt, verbose=False,memory=ConversationBufferWindowMemory(k=2))

    ai_reply = chain.predict(human_input=human_input)
    # print(story)
    return ai_reply



def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)

    # Generate AI response using user input (replace this with your AI model)
    ai_response = get_ai_response(user_input)
    st.session_state.generated.append(ai_response)
    st.session_state.user_input = ''
    # Display the AI response
    


#def on_btn_click():
#    st.session_state.past.clear()
#    st.session_state.generated.clear()


st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])

#st.title("Hi I'm :red[Bianca]")

chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user_{st.session_state['past'][i]}")
        message(st.session_state['generated'][i], key=f"{i}")
    
    #st.button("Clear messages", on_click=on_btn_click)


with st.container():
    st.text_input("", on_change=on_input_change, key="user_input")
