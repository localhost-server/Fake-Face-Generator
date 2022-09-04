def imports():
    """The function get_online_person in library thispersondoesnotexist calls api and collects data from server in byte format""" 
    from thispersondoesnotexist import get_online_person
    """PIL library is used to do manipulation with image data"""
    from  PIL import Image
    """[Check Here](https://docs.python.org/3/library/asyncio.html?highlight=asyncio#module-asyncio)"""
    import asyncio as a
    """The io module deals with various types of I/O in python. There are three main types of I/O: text I/O, binary I/O and raw I/O."""
    import io
    """Streamlit has been used to give our app a web interface."""
    import streamlit as st 

imports()

def Make_new_Face():
    a.get_event_loop_policy()#set_event_loop_policy(a.WindowsSelectorEventLoopPolicy)#get_event_loop()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    loop.close()
    img=Image.open(io.BytesIO(bytedata))
    return img.save("face.png")
    # return img.show()

def showimage():
    return Image.open('face.png').show()

def aface():
    a.get_event_loop_policy()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    loop.close()
    img=Image.open(io.BytesIO(bytedata))
    return img.show()

def show():
    return st.image('face.png')
    
def START(START=None):
    st.title('Fake Face Generator')
    st.header("This is a computer generated image")
    if st.button("Generate Face"):
        Make_new_Face()
        return show()

if __name__ == '__main__':
    START()
