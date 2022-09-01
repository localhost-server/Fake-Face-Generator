from thispersondoesnotexist import get_online_person
from  PIL import Image
import asyncio as a
import io
import base64
import streamlit as st 

def Make_new_Face():
    a.get_event_loop_policy()#set_event_loop_policy(a.WindowsSelectorEventLoopPolicy)#get_event_loop()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    loop.close()
    img=Image.open(io.BytesIO(bytedata))
    return img.save("face.png")
    # return img.show()

def show():
    return st.image('face.png')
    
def START(START=None):
    st.title('Fake Face Generator')
    st.header("This is a computer generated image")
    if st.button("Generate Face"):
        Make_new_Face()
        return show()
