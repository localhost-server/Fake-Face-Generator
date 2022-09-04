from thispersondoesnotexist import get_online_person
from  PIL import Image
import asyncio as a
import io
import streamlit as st 

def Make_new_Face(name_of_image='face.png'):
    """
    PIL library is used to do manipulation with image data.
    This function calls api and save the generated image.
    The io module deals with various types of I/O in python. There are three main types of I/O: text I/O, binary I/O and raw I/O.
    :param name_of_image : Set to face.png by defalt.
    :return img.save : Our image data from byte format is converted into image format and saved with desired name"""
    a.get_event_loop_policy()#set_event_loop_policy(a.WindowsSelectorEventLoopPolicy)#get_event_loop()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    loop.close()
    img=Image.open(io.BytesIO(bytedata))
    return img.save(name_of_image)
    # return img.show()

def showimage(name_of_image='face.png'):
    """This function will open the saved image by user with cmd mode
    :param name_of_image : Set to face.png by default.
    :return Image.open : Our image will be displayed with the default windows/linux image application"""
    return Image.open('face.png').show()

def aface():
    """This function is for cmd mode and will directly show an image on screen without saving."""
    a.get_event_loop_policy()
    loop=a.new_event_loop()
    bytedata = loop.run_until_complete(get_online_person())
    loop.close()
    #img=Image.open(io.BytesIO(bytedata))
    return Image.open(io.BytesIO(bytedata))#img.show()

def show():
    """This function will display our newly generated image on webpage."""
    return st.image('face.png')
    
def START(START=None):
    """In this function streamlit has been used to give our app a web interface."""
    st.title('Fake Face Generator')
    st.header('This is a computer generated image')
    if st.button('Generate Face'):
        Make_new_Face()
        return show()
START()
