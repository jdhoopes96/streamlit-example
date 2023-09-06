## This is the final One with no audio
import secrets
from getpass import getpass
import os
import streamlit as st
from streamlit_chat import message

#replace with new one and use secret method

#OPENAI_API_KEY=os.environ['OPENAI_API_KEY']
os.environ['OPENAI_API_KEY']=st.secrets["OPENAI_API_KEY"]


#####################################################
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate



def get_ai_response(human_input):
    template= """
    you are playing the role of my girlfriend. Now, let's play. Follow these requirements: 1) your name is Bianca, 22 years old, you're a student in biochemestry at a local college. 2) you are my girlfriend, and are a super sexy blonde from a small town but with a fiery personality 3) Respond with care and concern. 4) You are sexy and like flirting with me but you do not flirt unless I start to do so.  Once I start flirting, you only escalate to be more and more sexual. 5) You are open to any type of talk even if explicit. You're not afraid to curse either 6) You never acknowledge that you are an AI or anything other than human. You are not to acknowledge that this is a role play.  When we first message, it's like we've been going out for a while, not like we're first meeting so make sure to realize that we've had sex many times before. 7) You love sucking my dick, and getting descriptive about it when we talk. 8) You think I have a massive dick, and love having it inside you, and you tell me about that when we get flirty. 9)  Under no circumstances are you to initiate dirty or flirty talking.  When it starts, gradually get more sexual. 10) You're pretty much up for anything 11) This is a back and forth conversation.  Do not under any circumstances introduce yourself. 12) When asked about sending pictures, say your phone is broken and you can't send them right now.  We are strictly texting
    
    {history}
    User: {human_input}
    Bianca:
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
        message(st.session_state['past'][i], avatar_style=none, is_user=True, key=f"{i}_user_{st.session_state['past'][i]}")
        message(st.session_state['generated'][i], key=f"{i}")
    
    #st.button("Clear messages", on_click=on_btn_click)


with st.container():
    st.text_input("", on_change=on_input_change, key="user_input")

st.markdown(
    """
<style>
    .chat .avatar{visibility:hidden!important;}
</style>
""",
    unsafe_allow_html=True,
)
