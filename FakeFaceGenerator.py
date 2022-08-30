from thispersondoesnotexist import get_online_person
from  PIL import Image
import asyncio as a
import io
import base64
import streamlit as st 

def Make_new_Face(START=None):
    a.set_event_loop_policy(a.WindowsSelectorEventLoopPolicy())#get_event_loop()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    img=Image.open(io.BytesIO(bytedata))
    img.save("face.png")
    st.image('face.png')
    # return img.show()
    loop.close()
# def facegen():
#     img= loop.run_until_complete(get_online_person())#.close()

#     img=Image.frombytes(img)
#     img=Image.imshow(img)
if __name__ == "__main__":
    Make_new_Face()
# facegen()
