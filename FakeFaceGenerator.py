from thispersondoesnotexist import get_online_person
from  PIL import Image
import asyncio as a
import io
import base64
import streamlit as st 

def Make_new_Face(START=None):
    a.set_event_loop_policy(a.DefaultEventLoopPolicy())#get_event_loop()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    img=Image.open(io.BytesIO(bytedata))
    img.save("face.png")
    # return img.show()
    loop.close()

def show():
    return st.image('face.png')
# def facegen():
#     img= loop.run_until_complete(get_online_person())#.close()

#     img=Image.frombytes(img)
#     img=Image.imshow(img)
if __name__ == "__main__":
    Make_new_Face()
    show()
# facegen()
